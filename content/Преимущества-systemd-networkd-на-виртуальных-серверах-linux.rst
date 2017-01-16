.. title: Преимущества systemd-networkd на виртуальных серверах Linux
.. slug: Преимущества-systemd-networkd-на-виртуальных-серверах-linux
.. date: 2016-09-02 13:33:59
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| `Вышла новая статья о преимуществах использования systemd для
  администрирования
  серверов <https://habrahabr.ru/company/ruvds/blog/309010/>`__. В этот
  раз про systemd-networkd.


    | Обычно на десктопах Linux для управления сетевыми настройками
      используется NetworkManager, поскольку он отлично справляется со
      своей работой и имеет GUI фронтенды для всех популярных
      графических окружений. Однако на серверах Linux его использование
      не целесообразно: он потребляет много ресурсов. NetworkManager
      занимает в оперативной памяти около 20 Мб, в то время как
      systemd-networkd и systemd-resolvd вместе меньше 2 Мб. По этой
      причине, по умолчанию серверные дистрибутивы
      `Linux <https://ruvds.com/linux>`__ часто используют различные
      собственные демоны.

    | |image0|
    | Таким образом возникает целый зоопарк скриптов и утилит: демон
      networking под Debian, который управляет конфигурацией сети через
      ifupdown, использующий файлы конфигурации хранящиеся в
      /etc/networing/interfaces.d и файл /etc/networking/interfaces, под
      CentOS network, который использует скрипты ifup и ifdown и,
      конечно же, свои файлы конфигурации находящиеся в
      /etc/sysconfig/network-scripts, netctl под ArchLinux. Всем
      известно, что Linux — конструктор, но почему бы такой простой и
      общей для самых различных систем вещи как настройка сети не иметь
      одинаковый вид?
    | ` <>`__
    | Мы предлагаем начать использовать быстрый и простой
      демон\ `systemd-networkd <https://wiki.archlinux.org/index.php/systemd-networkd_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)>`__,
      особенно в свете того, что многие дистрибутивы уже перешли на
      systemd, поэтому переключение на systemd-networkd не составит
      труда. На текущий момент systemd-networkd может заменить собой
      множество утилит и поддерживает, настройку сети как по DHCP
      (клиент и сервер) так и со статическими IP-адресами, мосты,
      туннели, VLANs, беспроводные сети (используя при этом
      wpa\_supplicant).

    | В статье мы рассмотрим, как активировать systemd-networkd и начать
      его использовать и в чем его основные преимущества перед
      остальными демонами.


    .. rubric:: Запуск systemd-networkd
       :name: запуск-systemd-networkd

    | 
    | Несмотря на страсти кипевшие вокруг внедрения
      `systemd <https://www.archlinux.org/packages/?name=systemd>`__,
      многие популярные дистрибутивы Linux стали использовать этот
      менеджер служб и поставлять его по умолчанию. Поэтому, вероятно,
      ваша система уже содержит всё необходимое для включения
      systemd-networkd. Необходим systemd версии 210 и выше.

    | Проверить версию можно с помощью команды:

    ::

        $ systemctl --version

    | 
    | Чтобы использовать, запустите следующие две службы и включите их
      работу при загрузке системы (отключив при этом другие демоны
      управляющие конфигурацией сети):

    ::

        $ systemctl enable systemd-networkd
        $ systemctl start systemd-networkd
        $ systemctl enable systemd-resolved
        $ systemctl start systemd-resolved

    | 

    .. rubric:: Конфигурирование
       :name: конфигурирование

    | 
    | В качестве примера переключения рассмотрим перенос конфигурации
      сети по умолчанию в CentOS (/etc/rc.d/init.d/network initscript)
      на systemd-networkd.

    | Полностью аналогичо переезд можно осуществить для Fedora и, с
      небольшими изменениями, для других дистрибутивов. Конфигурационные
      файлы systemd-networkd находятся в директории
      /etc/systemd/network. Доступны следующие типы:

    -  .link – описывают физические параметры каждого интерфейс: имя,
       MAC, MTU и другие
    -  .network – описывают параметры сети: IP, маршруты, DNS и другие
    -  .netdev – описывают виртуальные интерфейсы, мосты

    | 
    | Конфигурация для примера: два интерфейса со статическим IP в LAN и
      WAN.


    ::

        $ ip addr
        1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
            link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
            inet 127.0.0.1/8 scope host lo
               valid_lft forever preferred_lft forever
            inet6 ::1/128 scope host
               valid_lft forever preferred_lft forever
        2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
            link/ether 04:01:40:23:1f:01 brd ff:ff:ff:ff:ff:ff
            inet 188.166.46.238/18 brd 188.166.63.255 scope global eth0
               valid_lft forever preferred_lft forever
            inet6 2a03:b0c0:2:d0::69:7001/64 scope global
               valid_lft forever preferred_lft forever
            inet6 fe80::601:40ff:fe23:1f01/64 scope link
               valid_lft forever preferred_lft forever
        3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
            link/ether 04:01:40:23:1f:02 brd ff:ff:ff:ff:ff:ff
            inet 10.133.248.54/16 brd 10.133.255.255 scope global eth1
               valid_lft forever preferred_lft forever
            inet6 fe80::601:40ff:fe23:1f02/64 scope link
               valid_lft forever preferred_lft forever

    | 
    | Конфигурационные файлы для CentOS (или Fedora): можно найти в
      директории /etc/sysconfig/network-scripts

    ::

        $ cat /etc/sysconfig/network-scripts/ifcfg-eth0
        DEVICE='eth0'
        TYPE=Ethernet
        BOOTPROTO=none
        ONBOOT='yes'
        HWADDR=04:01:40:23:1f:01
        IPADDR=188.166.46.238
        NETMASK=255.255.192.0
        GATEWAY=188.166.0.1
        NM_CONTROLLED='yes'
        IPV6INIT=yes
        IPV6ADDR=2A03:B0C0:0002:00D0:0000:0000:0069:7001/64
        IPV6_DEFAULTGW=2A03:B0C0:0002:00D0:0000:0000:0000:0001
        IPV6_AUTOCONF=no
        DNS1=2001:4860:4860::8844
        DNS2=2001:4860:4860::8888
        DNS3=8.8.8.8

    | 
    | Необходимо создать 4 файла в директории /etc/systemd/network/

    ::

        $ cat /etc/systemd/network/90-external.link
        [Match]
        MACAddress=04:01:40:23:1f:01
        [Link]
        Name=eth-outer

        $ cat /etc/systemd/network/90-internal.link
        [Match]
        MACAddress=04:01:40:23:1f:02
        [Link]
        Name=eth-inner

        $ cat eth-external.network
        [Match]
        Name= eth-outer
        [Network]
        DHCP=no
        Adress=188.166.46.238/18
        Adress=2A03:B0C0:0002:00D0:0000:0000:0000:0069:7001/64
        Gateway=188.166.0.1
        Gateway= 2A03:B0C0:0002:00D0:0000:0000:0000:0000:0001
        DNS=2001:4860:4860:8844
        DNS=2001:4860:4860:8888
        DNS=8.8.8.8

        $ cat eth-internal.network
        [Match]
        Name=eth-inner
        [Network]
        Address=10.133.248.54/16

    | 
    | Вот и всё: конфигурация сети завершена. Теперь можно перезапустить
      сервис:

    ::

        systemctl restart systemd-networkd

        $ networkctl
        IDX LINK             TYPE               OPERATIONAL SETUP
          1 lo               loopback           n/a         n/a
          2 eth-outer        ether              routable    configured
          3 eth-inner        ether              routable    configured

    | 
    | Другие типы сетей:
    | **DHCP**
    | В данном примере сконфигурируем DHCP IPv4 и IPv6; IPv6 если не
      нужен, можно исключить.


    ::

        $ cat /etc/systemd/network/wired-dhcp.network
        [Match]
        Name=eth*

        [Network]
        DHCP=ipv4
        DHCP=ipv6

    | 
    | **Подключение типа «Мост»**
    | Сначала создает конфигурацию виртуального интерфейса:

    ::

        $ cat /etc/systemd/network/bridge.netdev
        [NetDev]
        Name=br0
        Kind=bridge

        $ cat /etc/systemd/network/bridge.network
        [Match]
        Name=br0

        [Network]
        DHCP=ipv4

    | 
    | И настраиваем интерфейс для подключения:

    ::

        $ cat /etc/systemd/network/wired.network
        [Match]
        Name=eth*

        [Network]
        Bridge=br0

    | 

    .. rubric:: Недостатки (не актуальны, по большему счету, для
       серверов)
       :name: недостатки-не-актуальны-по-большему-счету-для-серверов

    | 
    | **1.** Не будет работать без systemd.

    | **2.** Нет ни CLI ни GUI фронтендов. И NetworkManager, и netctl не
      страдают таким недостатком. Например, для подключения к WiFi вам
      понадобится командная строка. Не совсем актуально для сервера.

    | **3.** Для первого подключения к WiFi необходимы root права.

      Однако это не совсем недостаток, так как в будущем к этой
      беспроводной сети подключение будет происходить автоматически.

    | **4.** Если быть не осторожным, то пароль от WiFi может храниться
      в открытом виде в истории команд. но этого можно легко избежать
      несколькими способами: временно отключить запись команд в историю
      (для bash: set +o history, set -o history), использовать shell не
      запоминающий историю (например dash) или просто вручную удалить
      пароль из истории.


    .. rubric:: Бенчмарк
       :name: бенчмарк

    | 
    | Тестируется скорость получения адресов по DHCP, Network manager
      and dnsmasq отключены.

    | Софт:

        — CentOS 7
        — kernel-3.10.0-327.28.3.el7
        — systemd 219
        — ISC DHCP client daemon and dhclient-script 4.2.5

    | 

    .. rubric:: systemd-networkd
       :name: systemd-networkd

    | 

    ::

        $ systemctl start systemd-networkd
        $ journalctl -u systemd-networkd.service
        Sep 01 13:04:41 localhost systemd[1]: Starting Network Service...
        Sep 01 13:04:41 localhost systemd-networkd[4085]: Enumeration completed
        Sep 01 13:04:41 localhost systemd[1]: Started Network Service.

        Sep 01 13:04:41 localhost systemd-networkd[4085]: eth0: DHCPv4 address 192.168.1.114/24 via 192.168.1.1
        Sep 01 13:04:41 localhost systemd-networkd[4085]: eth0: Configured

    | 
    | Меньше чем за секунду.


    .. rubric:: ISC DHCP
       :name: isc-dhcp

    | 

    ::

        $ time dhclient -v eth0
        Interface up - dhclient
        Internet Systems Consortium DHCP Client 4.2.5
        Copyright 2004-2013 Internet Systems Consortium.

        All rights reserved.

        For info, please visit https://www.isc.org/software/dhcp/

        Listening on LPF/enp2s0/94:de:80:1a:da:af
        Sending on   LPF/enp2s0/94:de:80:1a:da:af
        Sending on   Socket/fallback
        DHCPREQUEST on eth0 to 255.255.255.255 port 67 (xid=0x5b763f4d)
        DHCPACK from 192.168.1.1 (xid=0x5b763f4d)
        bound to 192.168.1.115 -- renewal in 20662 seconds.


        real        0m2.243s
        user        0m0.042s
        sys        0m0.216s

    | 
    | Среднее время после нескольких попыток составило 2.5 секунд.


    .. rubric:: Заключение
       :name: заключение

    | 
    | В виду активного использования systemd различными топовыми
      дистрибутивами Linux можно заключить, что, всё же, сообщество
      стремится к унификации основных системных функций. К ним
      относится, в том числе, конфигурирование сети, а systemd, в свою
      очередь, предлагает удобное, быстрое и функциональное решение. И
      пусть пока это решение сталкивается с проблемой отсутствия GUI для
      десктопных систем, но для `Linux
      серверов <https://ruvds.com/linux>`__ оно, возможно, станет
      стандартом «де-факто» и заменит кучу легаси демонов и отдельных
      утилит. Это сделает Linux гораздо более удобным для
      контейнеризации и использования на виртуальных машинах.


Приятно видеть, что предлагаемый функционал systemd оценивается по
достоинству, и им активно пользуются.


.. |image0| image:: https://habrastorage.org/files/fd0/889/577/fd088957790e4dac8d74c96807af3185.png
   :target: https://habrahabr.ru/company/ruvds/blog/309010/
