.. title: Вышел RFRemix 26 Beta
.. slug: vyshel-rfremix-26-beta
.. date: 2017-06-13 17:22:32 UTC+03:00
.. tags: rfremix
.. category: RFRemix
.. link: 
.. backlinks: none
.. description: 
.. type: text
.. author: Tigro

Вышел RFRemix 26 Beta, основанный на репозиториях Fedora, RPM Fusion, и Russian Fedora. Для загрузки доступны Live-образы KDE, LXQt, LXDE, XFCE, MATE, Cinnamon, а также Workstation версия с GNOME 3.24. Доступна Серверная редакция, образы сетевой установки. Также доступны образы Cloud и Docker.

.. image:: /images/LXQt.png
   :align: center

Основные отличия
================

* Freetype пересобран с subpixel rendering.
* Fontconfig содержит патчи Ubuntu для LCD мониторов (в общем сломали шрифты как всегда).
* В образы Workstation по умолчанию для GNOME Shell (не для GTK) используется тема Korora из одноименного проекта. Также опционально добавлены темы Adapta и EvoPop для GTK и иконки EvoPop. Все отключается и включается в gnome-tweak-tool.
* В KDE добавлен LibreOffice вместо офиса KDE, а также изменена загрузочная тема Плимута на breeze.
* Доступна поддержка вымирающего Flash.
* В репозитории доступен клиент для WhatsApp и Wire, а также старый Skype (который почти уже умер), Viber и Telegram.
* В Live-образы в выключенном состоянии добавлены официальные репозитории с Google Chrome, Yandex Browser, MEGAsync, Skype, Slack, VirtualBox, Cloud Mail.ru, VK мессенджер и Yandex Disk.
* Chromium пересобран с поддержкой кодеков.
* Taglib собран с патчем ruxmms, для поддержки тегов в кодировке win1251.
* Telepathy Gabble собран с патчем, позволяющим подключение к Jabber серверу Cisco.
* В репозитории доступен клиент s3fs-fuse и distributed key/value storage Elliptics.
* Доступен новый Live-образ LXQt.
* Для Live-образов доступна опция загрузки образа в память (rd.live.ram).
* На все Live-образы добавлен по умолчанию Telegram.

Ссылки для скачивания
=====================

* RFRemix Cloud [ `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/CloudImages/i386/images/>`__ ] [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/CloudImages/x86_64/images/>`__ ]
* RFRemix Docker [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/Docker/x86_64/images/>`__ ]
* RFRemix Server [ `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/Server/i386/iso/>`__ ] [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/Server/x86_64/iso/>`__ ]
* RFRemix Workstation [ `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/Workstation/i386/iso/>`__ ] [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/Workstation/x86_64/iso>`__ ]
* Образы Live [ `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/Spins/i686/>`__ ] [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/26_Beta/Spins/x86_64>`__ ]

Куда сходить спросить, пожаловаться
===================================

* `Баг-трекер <http://redmine.russianfedora.pro/>`_
* `Группа в Telegram <https://telegram.me/russianfedora>`_

Обновление
==========

Для обновления с предыдущих версий RFRemix нужно отдать команду:::

        dnf --releasever=26 distro-sync --nogpgcheck
