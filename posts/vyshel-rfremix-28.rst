.. title: Вышел RFRemix 28
.. slug: vyshel-rfremix-28
.. date: 2018-05-04 17:37:23 UTC+03:00
.. tags: rfremix
.. category: RFRemix
.. link: 
.. backlinks: none
.. description: 
.. type: text
.. author: Tigro

Невероятный случай, первый же RC признали релизом, так что мы немного задержались. Но вот сейчас всё готово. RFRemix 28 доступен для скачивания. Всё как обычно, образы, мультимедия, репозитории, шрифты и т. п. Образы доступны только для архитектуры x86_64. Доступно ядро 4.16, GNOME 3.28, KDE Plasma 5.12, XFCE 4.12, MATE 1.20, Cinnamon 3.6, LibreOffice 6, Firefox 59, Chromium 66.

.. image:: /images/rfremix28.png
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
* На все Live-образы добавлен по умолчанию Telegram.
* Добавлены патчи для улучшения работы pulseaudio и bluetooth устройств.

Ссылки для скачивания
=====================

* RFRemix Cloud [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/28/CloudImages/x86_64/images/>`__ ]
* RFRemix Docker [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/28/Docker/x86_64/images/>`__ ]
* RFRemix Workstation [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/28/Workstation/x86_64/iso>`__ ]
* RFRemix Server [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/28/Server/x86_64/iso>`__ ]
* Образы Live [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/28/Spins/x86_64>`__ ]
* Торренты [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/28/Torrents/x86_64>`__ ]

Куда сходить спросить, пожаловаться
===================================

* `Баг-трекер <http://redmine.russianfedora.pro/>`_
* `Группа в Telegram <https://telegram.me/russianfedora>`_

Обновление
==========

Для обновления с предыдущих версий RFRemix нужно отдать команду:::

        dnf --releasever=28 distro-sync --nogpgcheck
