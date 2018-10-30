.. title: Вышел RFRemix 29
.. slug: vyshel-rfremix-29
.. date: 2018-10-30 16:00:00 UTC+01:00
.. tags: rfremix
.. category: RFRemix
.. link: 
.. backlinks: none
.. description: 
.. type: text
.. author: RussianFedora Team

Есть такая традиция два раза в год выпускать RFRemix. На это раз это уже RFRemix 29, 19 релиз RFRemix (хотя должен быть конечно же 20-й, но 22 не было) – набор образов с различными изменениями и дополнениями (мультимедия, репозитории, шрифты и т. п). Образы доступны для архитектуры x86_64. Доступно ядро 4.18, GNOME 3.30, KDE Plasma 5.13, XFCE 4.13, MATE 1.20, Cinnamon 3.8, LxQT 0.13, LibreOffice 6.1, Firefox 63, Chromium 69.

.. image:: /images/rfremix29.png
   :align: center

Основные отличия
================
* Freetype пересобран с subpixel rendering.
* Fontconfig содержит патчи Ubuntu для LCD мониторов (в общем сломали шрифты как всегда).
* В образы Workstation по умолчанию для GNOME Shell используется тема Korora из одноименного проекта.
* В KDE добавлен LibreOffice вместо офиса KDE, а также изменена загрузочная тема Плимута на breeze.
* Доступна поддержка все ещё вымирающего Flash.
* В Live-образы в выключенном состоянии добавлены официальные репозитории с Google Chrome, Yandex Browser, MEGAsync, Skype, Slack, VirtualBox, Cloud Mail.ru, VK мессенджер и Yandex Disk.
* Chromium пересобран с поддержкой кодеков. Сейчас эта опция также доступна в RPM Fusion, но пока мы не планируем отказываться от собственной сборки.
* Taglib собран с патчем ruxmms, для поддержки тегов в кодировке win1251.
* Telepathy Gabble собран с патчем, позволяющим подключение к Jabber серверу Cisco.
* Для Live-образов доступна опция загрузки образа в память (rd.live.ram).
* Во все Live-образы добавлен по умолчанию Telegram.

Ссылки для скачивания
=====================

* RFRemix Workstation [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/29/Workstation/x86_64/>`__ ]
* RFRemix Server [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/29/Server/x86_64/iso/>`__ ]
* Образы Live [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/29/Spins/x86_64>`__ ]
* Торренты [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/29/Torrents/x86_64>`__ ]

Куда сходить спросить, пожаловаться
===================================

* `Баг-трекер <http://redmine.russianfedora.pro/>`_
* `Группа в Telegram <https://t.me/russianfedora>`_
* `Канал в Matrix <https://matrix.to/#/#russianfedora:matrix.org>`_

Обновление
==========

Для обновления с предыдущих версий RFRemix нужно открыть терминал и выполнить:::

        sudo dnf upgrade --refresh 
        sudo dnf install dnf-plugin-system-upgrade
        sudo dnf system-upgrade download --releasever=29
        sudo dnf system-upgrade reboot
