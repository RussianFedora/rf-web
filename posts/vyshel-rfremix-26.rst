.. title: Вышел RFRemix 26
.. slug: vyshel-rfremix-26
.. date: 2017-07-11 16:48:23 UTC+03:00
.. tags: rfremix
.. category: RFRemix
.. link: 
.. backlinks: none
.. description: 
.. type: text
.. author: Tigro

Итак сегодня вышла Fedora 26 и по традиции RFRemix 26, основанный на репозиториях Fedora, RPM Fusion, и Russian Fedora. Для загрузки доступны Live-образы KDE, LXQt, LXDE, XFCE, MATE, Cinnamon, а также Workstation версия с GNOME 3.24. Доступна Серверная редакция, образы сетевой установки. Также доступны образы Cloud и Docker.

Russian Fedora внезапно попала под украинские санкции (так как хостится на mirror.yandex.ru), поэтому появилось новое зеркало в Германии: `http://ftp.russianfedora.pro/fedora/russianfedora/">http://ftp.russianfedora.pro/fedora/russianfedora/ <http://ftp.russianfedora.pro/fedora/russianfedora/">`__.

.. image:: /images/MATE.png
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
* Chromium пересобран с поддержкой кодеков. Сейчас эта опция также доступна в RPM Fusion, но пока мы не планируем отказываться от собственной сборки.
* Taglib собран с патчем ruxmms, для поддержки тегов в кодировке win1251.
* Telepathy Gabble собран с патчем, позволяющим подключение к Jabber серверу Cisco.
* В репозитории доступен клиент s3fs-fuse и distributed key/value storage Elliptics.
* Доступен новый Live-образ LXQt.
* Для Live-образов доступна опция загрузки образа в память (rd.live.ram).
* На все Live-образы добавлен по умолчанию Telegram.
* Исправлен `баг <https://bugzilla.redhat.com/show_bug.cgi?id=1465138">`__ баг в связке WPA_Supplocant+OpenSSL при подключении к Wi-FI EAT-TLS.

Ссылки для скачивания
=====================

* RFRemix Cloud [ `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/CloudImages/i386/images/>`__ ] [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/CloudImages/x86_64/images/>`__ ]
* RFRemix Docker [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/Docker/x86_64/images/>`__ ]
* RFRemix Server [ `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/Server/i386/iso/>`__ ] [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/Server/x86_64/iso/>`__ ]
* RFRemix Workstation [ `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/Workstation/i386/iso/>`__ ] [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/Workstation/x86_64/iso>`__ ]
* Образы Live [ `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/Spins/i686/>`__ ] [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/26/Spins/x86_64>`__ ]

Куда сходить спросить, пожаловаться
===================================

* `Баг-трекер <http://redmine.russianfedora.pro/>`_
* `Группа в Telegram <https://telegram.me/russianfedora>`_

Обновление
==========

Для обновления с предыдущих версий RFRemix нужно отдать команду:::

        dnf --releasever=26 distro-sync --nogpgcheck
