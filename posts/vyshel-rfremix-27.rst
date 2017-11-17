.. title: Встречайте RFRemix 27
.. slug: vyshel-rfremix-27
.. date: 2017-11-16 12:21:12 UTC+03:00
.. tags: rfremix
.. category: RFRemix
.. link: 
.. backlinks: none
.. description: 
.. type: text
.. author: Tigro

На этот раз немножечко задержались, но всё таки выпустили RFRemix 27, ремикс, основанный на репозиториях Fedora, RPM Fusion, и Russian Fedora. Для загрузки доступны Live-образы KDE, LXQt, LXDE, XFCE, MATE, Cinnamon, а также Workstation версия с GNOME 3.26, образ сетевой установки, образы Cloud и Docker. RFRemix Server будет позже (возможно будет), так как Fedora Server ожидается аж в январе. На то есть причины – новая модульная структура.

Образы собраны только под архитектуру x86_64, как и в Fedora.

.. image:: /images/rfremix27.png
   :align: center

Основные отличия
================
* Freetype пересобран с subpixel rendering.
* Fontconfig содержит патчи Ubuntu для LCD мониторов (в общем сломали шрифты как всегда).
* В образы Workstation по умолчанию для GNOME Shell используется тема Korora из одноименного проекта. Также опционально добавлены темы Adapta и EvoPop для GTK и иконки EvoPop. Все отключается и включается в gnome-tweak-tool.
* В KDE добавлен LibreOffice вместо офиса KDE, а также изменена загрузочная тема Плимута на breeze.
* Доступна поддержка вымирающего Flash.
* В Live-образы в выключенном состоянии добавлены официальные репозитории с Google Chrome, Yandex Browser, MEGAsync, Skype, Slack, VirtualBox, Cloud Mail.ru, VK мессенджер и Yandex Disk.
* Chromium пересобран с поддержкой кодеков. Сейчас эта опция также доступна в RPM Fusion, но пока мы не планируем отказываться от собственной сборки.
* Taglib собран с патчем ruxmms, для поддержки тегов в кодировке win1251.
* Telepathy Gabble собран с патчем, позволяющим подключение к Jabber серверу Cisco.
* Для Live-образов доступна опция загрузки образа в память (rd.live.ram).
* На все Live-образы добавлен по умолчанию Telegram.

Ссылки для скачивания
=====================

* RFRemix Cloud [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/27/CloudImages/x86_64/images/>`__ ]
* RFRemix Docker [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/27/Docker/x86_64/images/>`__ ]
* RFRemix Workstation [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/27/Workstation/x86_64/iso>`__ ]
* Образы Live [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/27/Spins/x86_64>`__ ]
* Торренты [ `x86_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/27/Torrents/x86_64>`__ ]

Куда сходить спросить, пожаловаться
===================================

* `Баг-трекер <http://redmine.russianfedora.pro/>`_
* `Группа в Telegram <https://telegram.me/russianfedora>`_

Обновление
==========

Для обновления с предыдущих версий RFRemix нужно отдать команду:::

        dnf --releasever=27 distro-sync --nogpgcheck
