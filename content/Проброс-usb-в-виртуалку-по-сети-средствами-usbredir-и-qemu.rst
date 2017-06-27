.. title:  Проброс USB в виртуалку по сети средствами usbredir и qemu
.. slug: Проброс-usb-в-виртуалку-по-сети-средствами-usbredir-и-qemu
.. date: 2015-08-20 14:44:47
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Есть интересная и довольно прибыльная задача - пробрасывать физические
  USB-устройства в виртуальную машину с Windows, так, чтобы та считала,
  что они подключены непосредственно к ней. Некоторые используют
  проприетарные и глючные продукты для ее решения, но на самом деле
  стоит попробовать открытый и надежный продукт нашего коллеги, `Hans de
  Goede <https://github.com/jwrdegoede>`__ -
  `usbredir <https://github.com/SPICE/usbredir>`__. С его помощью можно
  как раз пробросить [STRIKEOUT:USB-ключ для 1С] произвольное
  USB-устройство в виртуалку. Отрадно, что появляются `хаутушки по этой
  теме <https://habrahabr.ru/post/265065/>`__:

    Проброс USB в виртуалку по сети средствами usbredir и qemu

    .. raw:: html

       <div class="hubs">

    `Системное
    администрирование <https://habrahabr.ru/hub/sys_admin/>`__\ \*,
    `Виртуализация <https://habrahabr.ru/hub/virtualization/>`__\ \*,
    `Open source <https://habrahabr.ru/hub/open_source/>`__\ \*,
    `\*nix <https://habrahabr.ru/hub/nix/>`__\ \*

    .. raw:: html

       </div>

    .. raw:: html

       <div class="content html_format">

    |image0|
    На сегодняшний день существет довольно много способов пробросить
    USB-устройство на другой компьютер или виртуалку по сети.

    Из наиболее популярных — железячные такие как AnywhereUSB и чисто
    програмные продукты, из тех что я попробовал сам: USB Redirector и
    USB/IP.

    Я бы хотел рассказать вам еще об одном интересном способе, который
    работает непосредственно с эмулятором qemu.

    Он так же является частью проекта spice, официально поддерживаемым
    RedHat.

    usbredir, это открытый протокол для проброса usb-устройств по tcp на
    удаленный виртуальный сервер, разработанный при поддержке RedHat в
    рамках проекта spice. Но как оказалось им можно вполне успешно
    пользоваться и без spice. В роли сервера выступает usbredirserver,
    который шарит usb-устройство на определенный порт, а в качестве
    клиента сам qemu, который эмулирует подключение экспортированного
    usb-устройства в определенный usb-контроллер вашей виртуальной
    машины. Благодаря такому подходу в качестве гостевой системы может
    использоваться абсолютно любая ОС, так как она даже не знает, что
    устройство является проброшенным удаленно, а вся логика ложится на
    qemu. ` <>`__
    .. rubric:: Для начала несколько слов о вышеперчисленных решениях
       :name: для-начала-несколько-слов-о-вышеперчисленных-решениях

    -  AnywhereUSB — довольно неплохое решение, но дорогое, и имеет
       неприятние глюки, например бывает если расшаренная флешка
       отваливается, то переподключить ее обратно можно только физически
       вынув и вставив ее.

    -  USB/IP — OpenSource проект. Вроде как был заброшен. По факту
       глючит довольно сильно. При разрыве соединения, машина частенько
       уходит в полнейший freezee, а windows показывает BSOD
    -  USB Redirector — Замечательная софтина. Для расшаривания
       устройств с linux на linux бесплатна, во всех остальных случаях
       уже стоит денег, не так много как AnywhereUSB, но и не бесплатно
       как хотелось бы :)

    Как видно есть из чего выбрать, но давайте же наконец попробуем еще
    один способ — usbredir?
    .. rubric:: Настройка виртуальной машины
       :name: настройка-виртуальной-машины

    Для того что бы было куда подключать экспортированные устройства, на
    виртуальной машине нужно создать необходимые usb-контроллеры:

    -  uhci — для USB1.0
    -  ehci — для USB2.0
    -  xhci — для USB3.0

    .. rubric:: Для qemu (без libvirt)
       :name: для-qemu-без-libvirt

    Скачайте конфиг
    `ehci-uhci.cfg <https://cgit.freedesktop.org/spice/qemu/plain/docs/ich9-ehci-uhci.cfg>`__,
    положите его в /etc/qemu/
    ::

        $ curl https://cgit.freedesktop.org/spice/qemu/plain/docs/ich9-ehci-uhci.cfg --create-dirs -o /etc/qemu/ehci-uhci.cfg

    И добавьте следующие опции в команду запуска виртуальной машины:
    ::

        -readconfig /etc/qemu/ich9-ehci-uhci.cfg
        -chardev spicevmc,name=usbredir,id=usbredirchardev1
        -device usb-redir,chardev=usbredirchardev1,id=usbredirdev1,debug=3
        -chardev spicevmc,name=usbredir,id=usbredirchardev2
        -device usb-redir,chardev=usbredirchardev2,id=usbredirdev2,debug=3
        -chardev spicevmc,name=usbredir,id=usbredirchardev3
        -device usb-redir,chardev=usbredirchardev3,id=usbredirdev3,debug=3

    .. rubric:: Для libvirt
       :name: для-libvirt

    Можно использовать такой конфиг.

    В исходном файле конфигурации виртуальной машины в узле <devices>
    удаляем все USB контроллеры и добавляем следущий блок:
    ::

        <controller type='usb' index='0' model='ich9-ehci1'>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x7'/>
        </controller>
        <controller type='usb' index='0' model='ich9-uhci1'>
        <master startport='0'/>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x0' multifunction='on'/>
        </controller>
        <controller type='usb' index='0' model='ich9-uhci2'>
        <master startport='2'/>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x1'/>
        </controller>
        <controller type='usb' index='0' model='ich9-uhci3'>
        <master startport='4'/>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x2'/>
        </controller>
        <redirdev bus='usb' type='spicevmc'> 
        <address type='usb' bus='0' port='3'/>
        </redirdev>
        <redirdev bus='usb' type='spicevmc'>
        <address type='usb' bus='0' port='4'/>
        </redirdev>
        <redirdev bus='usb' type='spicevmc'>
        <address type='usb' bus='0' port='5'/>
        </redirdev>
        <redirdev bus='usb' type='spicevmc'>
        <address type='usb' bus='0' port='6'/>
        </redirdev>

    Но у меня он почему-то не заработал, и я решил пойти другим путем, а
    именно явно указть libvirt с какими опциями запускать qemu:
    Этот блок рамещается перед тегом </domain>:
    ::

        <qemu:commandline>
        <qemu:arg value="-readconfig"/>
        <qemu:arg value="/etc/qemu/ich9-ehci-uhci.cfg"/>
        <qemu:arg value="-chardev"/>
        <qemu:arg value="spicevmc,name=usbredir,id=usbredirchardev1"/>
        <qemu:arg value="-device"/>
        <qemu:arg value="usb-redir,chardev=usbredirchardev1,id=usbredirdev1,bus=ehci.0,debug=3"/>
        <qemu:arg value="-chardev"/>
        <qemu:arg value="spicevmc,name=usbredir,id=usbredirchardev2"/>
        <qemu:arg value="-device"/>
        <qemu:arg value="usb-redir,chardev=usbredirchardev2,id=usbredirdev2,bus=ehci.0,debug=3"/>
        <qemu:arg value="-chardev"/>
        <qemu:arg value="spicevmc,name=usbredir,id=usbredirchardev3"/>
        <qemu:arg value="-device"/>
        <qemu:arg value="usb-redir,chardev=usbredirchardev3,id=usbredirdev3,bus=ehci.0,debug=3"/>
        </qemu:commandline>

    Не забудьте так же скачать конфиг
    `ehci-uhci.cfg <https://cgit.freedesktop.org/spice/qemu/plain/docs/ich9-ehci-uhci.cfg>`__,
    и сохранить его в /etc/qemu/ как в случае с qemu без libvirt
    Кстати, после данной настройки, если вы используете spice, станет
    возможен проброс usb-устройств с клиента spice на сервер.

    Заводим виртуалку, теперь все готово для осуществления проброса.

    .. rubric:: Запуск сервера
       :name: запуск-сервера

    Пакет usbredirserver можно найти в стандартных репозиториях
    практически во всех популярных дистрибутивах linux.

    Вставляем флешку в компьютер, смотрим вывод usb-устройств:
    ::

        $ lsusb
        ...
        Bus 003 Device 011: ID 125f:c82a A-DATA Technology Co., Ltd. 
        ...

    Видим что пара vendorid:prodid равна 125f:c82a, а ядро определило
    флешке 003-001 usbbus-usbaddr соотвественно.

    Теперь давайте расшарим ее на 4000 порт:
    ::

        # Используя пару vendorid:prodid
        $ usbredirserver -p 4000 125f:c82a
        # Используя пару usbbus-usbaddr
        $ usbredirserver -p 4000 003-011

    .. rubric:: Подключение устройства к виртуальной машине
       :name: подключение-устройства-к-виртуальной-машине

    Заходим на гипервизор и в qemu-monitor нашей машины выполняем
    следующие команды:
    ::

        # Добавляем наше устройство
        chardev-add socket,id=usbredirchardev1,port=4000,host=192.168.1.123
        # Подключем его в ehci контроллер (USB-2.0)
        device_add usb-redir,chardev=usbredirchardev1,id=usbredirdev1,bus=ehci.0,debug=4

    Что бы отключить флешку достаточно такой команды:
    ::

        device_del usbredirdev1

    Если у вас libvirt, то команды в qemu-monitor можно отправить
    следующим образом:
    ::

        $ virsh qemu-monitor-command --hmp one-73 'chardev-add socket,id=usbredirchardev1,port=4000,host=192.168.1.123'
        $ virsh qemu-monitor-command --hmp one-73 'device_add usb-redir,chardev=usbredirchardev1,id=usbredirdev1,bus=ehci.0,debug=4'
        $ virsh qemu-monitor-command --hmp one-73 'device_del usbredirdev1'

    На этом все, после данных шагов ваша ВМ увидит вашу флешку и сможет
    с ней нативно работать.

    .. rubric:: Если устройств много и все они одинаковые
       :name: если-устройств-много-и-все-они-одинаковые

    Вот тут появилась интересная задачка, как пробросить несколько
    одинаковых девайсов на разные ВМ?
    При этом, стоит отметить, все устройства имеют одинаковую пару
    vendorid:prodid, а пара usbbus-usbaddr совсем не постоянна, стоит
    только вынуть и вставить устройство, так оно сразу поменяет свой
    usbaddr.

    Для себя я решил ее при помощи udev, и небольшого скрипта.

    Кстати если вы не совсем понимаете как работает udev, на Debian Wiki
    есть классная `статья о udev <https://wiki.debian.org/ru/udev>`__
    И так приступим:
    Для начала узнаем серийник нашего устройства, по которому и будем
    идентифицировать его в udev:
    ::

        $ udevadm info -a -n /dev/bus/usb/003/011 | grep '{serial}'
            ATTR{serial}=="11C130317234004B"
            ATTRS{serial}=="0000:00:14.0"

    Теперь создадаим файл /etc/udev/rules.d/99-usb-serial.rules и
    запишем в него следующее правило:
    ::

        SUBSYSTEM=="usb", ATTRS{idVendor}=="125f", ATTRS{idProduct}=="c82a", ATTR{serial}=="11C130317234004B", SYMLINK+="usbdevices/token1"

    Перезагрузим udev-правила:
    ::

        $ udevadm control --reload-rules

    Теперь, при подключении нашей флешки, в /dev/usbdevices/token1 на
    нее появится симлинк.

    Я написал небольшой скрипт, который использует этот симлинк, для
    того что бы узнать настоящую пару usbbus-usbaddr устройства и
    расшарить его на нужный порт
    usbredirserver-by-symlink.sh
    ::

        #!/bin/bash
        keys="${@:1:${#}-1}"
        usblink="${@: -1}"
        if [ -L $usblink ] && [ $# != 0 ]; then
            usbbus=`udevadm info -a -n $usblink | awk -F== '/ATTR{busnum}/ { gsub(/"/,"",$2);print $2 }'`
            usbaddr=`udevadm info -a -n $usblink | awk -F== '/ATTR{devnum}/ { gsub(/"/,"",$2);print $2 }'`
            if [ "$usbbus" != "" ] && [ "$usbaddr" != "" ]; then
                usbredirserver $keys $usbbus-$usbaddr
            else
                echo "This is not usb device"
                exit 1
            fi
        else
            echo "Usage: usbredirserver-by-symlink.sh [-p|--port <port>] [-v|--verbose <0-5>] /dev/usbdevice"
            exit 1
        fi

    К сожалению от смены пары usbbus-usbaddr после расшаривания
    устройства этот скрипт не спасет, так как usbredirserver не
    отваливается, если устройство вынуть или если такое устройство
    вообще не существует. Но он облегчит путь и поможет не запутаться
    при расшаривании нужного устройства на нужные ВМ.

    В дальнейшем его можно будет использовать, для написания следующего
    скрипта, который будет мониторить подключение/отключение устройств,
    расшаривать нужные и автоматически подключать/отключать их на
    удаленной ВМ.

    .. rubric:: Источники:
       :name: источники

    `umvirt.ru/node/82 <http://umvirt.ru/node/82>`__
    `opennebula.org/opennebula-for-virtual-desktops <http://opennebula.org/opennebula-for-virtual-desktops/>`__
    `opennet.ru/opennews/art.shtml?num=30773 <http://opennet.ru/opennews/art.shtml?num=30773>`__
    `lists.gnu.org/archive/html/qemu-devel/2013-07/msg05244.html <http://lists.gnu.org/archive/html/qemu-devel/2013-07/msg05244.html>`__

    .. raw:: html

       </div>

.. |image0| image:: https://habrastorage.org/files/e6a/1bc/05d/e6a1bc05d70c460399d3276fdec28d2c.png

