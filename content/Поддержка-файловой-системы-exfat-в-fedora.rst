.. title: Поддержка файловой системы exFAT в Fedora
.. slug: Поддержка-файловой-системы-exfat-в-fedora
.. date: 2012-07-11 11:34:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Vascom

**Это архивная статья**


По нашему
`запросу <https://bugzilla.redhat.com/show_bug.cgi?id=822046>`__ юристы
Fedora проверили легальность включения поддержки файловой системы
`exFAT <https://ru.wikipedia.org/wiki/ExFAT>`__ в дистрибутив и
репозитории. К сожалению `открытая
реализация <http://code.google.com/p/exfat/>`__ данной ФС **не
допускается** в основной Fedora. `Tom "spot"
Callaway <https://fedoraproject.org/wiki/User:Spot>`__: "Upon review,
implementations of exfat are not permitted in Fedora."

Однако необходимые пакеты (fuse-exfat и exfat-utils) останутся доступны
из репозитория `russianfedora <http://russianfedora.ru/repository>`__.

