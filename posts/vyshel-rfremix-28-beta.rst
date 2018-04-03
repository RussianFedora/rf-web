.. title: Вышел RFRemix 28 Beta
.. slug: vyshel-rfremix-27
.. date: 2018-04-03 21:55:10 UTC+03:00
.. tags: rfremix
.. category: RFRemix
.. link: 
.. backlinks: none
.. description: 
.. type: text
.. author: Tigro

Как обычно, в один день с выходом Fedora 28 Beta мы выпускаем и одноименную версию RFRemix. Всё как обычно, образы, мультимедия, репозитории, шрифты и т. п. Бета версия готова для тестирования. Образы доступны только для архитектуры x86_64. Доступно ядро 4.16, GNOME 3.28, KDE Plasma 5.12, XFCE 4.12, MATE 1.20, Cinnamon 3.6, LibreOffice 6, Firefox 59, Chromium 65.

.. image:: /images/rfremix28-beta.png
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

Ссылки для скачивания
=====================

* RFRemix Cloud [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/28_Beta/CloudImages/x86_64/images/>`__ ]
* RFRemix Docker [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/28_Beta/Docker/x86_64/images/>`__ ]
* RFRemix Workstation [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/28_Beta/Workstation/x86_64/iso>`__ ]
* RFRemix Server [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/28_Beta/Server/x86_64/iso>`__ ]
* Образы Live [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/28_Beta/Spins/x86_64>`__ ]
* Торренты [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/28_Beta/Torrents/x86_64>`__ ]

Куда сходить спросить, пожаловаться
===================================

* `Баг-трекер <http://redmine.russianfedora.pro/>`_
* `Группа в Telegram <https://telegram.me/russianfedora>`_

Обновление
==========

Для обновления с предыдущих версий RFRemix нужно отдать команду:::

        dnf --releasever=28 distro-sync --nogpgcheck
