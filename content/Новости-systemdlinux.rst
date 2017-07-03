.. title: Новости systemd/Linux
.. slug: Новости-systemdlinux
.. date: 2016-08-24 18:39:49
.. tags: systemd, coreos, facebook, redhat, canonical, kdbus 
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

`Сформирована программа
<https://cfp.systemd.io/en/systemdconf_2016/public/schedule>`__ конференции
`systemd.conf 2016 </content/Анонсирован-systemdconf-2016>`__. Среди
выступающих как представители крупных корпоративных пользователей systemd
(Bosch, n:stack / StackHut, NixOS, Facebook, например), так и
компаний-разработчиков (например, Red Hat, Endocode, ProFUSION, Pengutronix,
CoreOS, Canonical, Kinvolk). Интересно, остались ли те, кто считает, что
systemd "ненужно" и "закопать"?

После `выявления проблем с производительностью </content/Новости-systemd-3>`__
и после `включения </content/kdbus-в-fedora-rawhide>`__ и `поспешного
отключения </content/Неожиданно-отключили-kdbus-в-fedora>`__ kdbus в Fedora
Rawhide, разработка была свернута в пользу совершенно нового проекта - `bus1
<https://github.com/bus1>`__. И вот, наконец-то, `анонсировали его первую
публичную версию
<https://lists.linuxfoundation.org/pipermail/ksummit-discuss/2016-July/003047.html>`__.

Разработчики резко упростили реализуемый функционал перепозиционировав проект,
как n-to-n шина сообщений с поддержкой multicast и unicast и с системой
безопасности на базе capabilities. Это было бы аналогом Binder из Android, если
бы тот умел multicast. Из-за поддержки multicast пришлось добавить функционал
неизменности порядка сообщений, т.е. если сторона (или стороны) отправила пакет
A, а затем B, то независимо от того, unicast это или multicast, адресат получит
сначала A, затем B.

Neil Brown уже написал `статью на LWN <https://lwn.net/Articles/697191/>`__,
под которой началось интересное обсуждение. Учитывая фиаско с kdbus, наверное
не стоит ожидать быстрого включения функционала bus1 в дистрибутивы, но пока мы
сохраняем осторожный оптимизм.

Ну и из смешного - `в systemd включили systemd-mount
<https://github.com/systemd/systemd/commit/29272c0>`__. `Напоминаем
<https://www.linux.org.ru/news/linux-general/7646275#comment-7646591>`__:

    Если кто не в курсе, то идеи, что в systemd надо включить управление
    сетью, wpa\_supplicant, минимальный shell, минимальный текстовый
    редактор (для работы с конфигами), **монтирование**, управление
    логинами, и пр. высказываются регулярно. Люди вокруг тут-же начинают
    шутить про emacs, а вот Lennart сразу-же задумывается и даже
    забывает про бокал пива в руке.
