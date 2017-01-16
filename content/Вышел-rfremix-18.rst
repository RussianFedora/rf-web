.. title: Вышел RFRemix 18
.. slug: Вышел-rfremix-18
.. date: 2013-01-15 17:32:19
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


После невероятно долгого периода разработки одновременно с Fedora 18
вышел **RFRemix 18**. Ремикс базируется на репозиториях Fedora, RPM
Fusion и Russian Fedora. Установочные образы содержат ядро 3.6.10, glibc
2.16, GNOME 3.6.2, KDE 4.9.4, XFCE 4.10, LXDE, LibreOffice 3.6.3,
Firefox 17, Chromium 24, мультимедийные кодеки, поддержку Adobe Flash и
др. пакеты.


**Основные изменения по сравнению с предыдущими версиями RFRemix.**

#. Произошёл отказ от специальных установочных репозиториев (из-за
   изменениях в файла групп приходилось делать собственные репозитории.

   Как следствие во время сетевой установки могли не находиться
   некоторые пакеты, если переиндескация не поспела за обновлением
   основного репозитория). Новая структура comps-файлов позволяет не
   изменять оригиналы. Теперь для сборки и сетевой установки
   используются оригинальные репозитории Fedora и RPM Fusion. Все
   необходимые изменения базируются только в репозиториях Russian
   Fedora;
#. Убраны сценарии быстрой установки в инсталляторе. Новая Анаконда
   делает всё параллельно, что в принципе и так "быстро".

**Основные отличия от оригинальной Fedora**

#. В инсталляторе добавлена возможность установки минимального
   количества пакетов для GNOME и KDE;
#. Поддержка репозиториев RPM Fusion и Russian Fedora в установщике;
#. Выполнена автоматическая настройка раскладок и их переключателя в
   GNOME при первом запуске системы;
#. В Firstboot добавлен дополнительный экран для быстрой настройки
   системы (выбор между KDM и GDM, включение некоторых полезных настроек
   в GNOME), а так же возможность выбора режима работы sudo. Добавлена
   опция для принудительной переиндексации метаданных yum раз в час;
#. Пакет Freetype собран с поддержкой subpixel rendering;
#. Fontconfig использует патчи из Ubuntu для более качественного
   отображения на LCD мониторах;
#. На диски добавлена стабильная версия Chromium 24.0.1312.52;
#. Собраны Live-образы с окружениями MATE и минимальным набором пакетов
   KDE;
#. Unzip правильно обрабатывает кириллицу;
#. Плееры, использующие gstreamer, правильно отображают теги в кодировке
   cp1251;
#. Добавлены мультимедийные кодеки и Adobe Flash.


**Загрузка**

Для загрузки доступны DVD образы, образы сетевой установки, а также
Live-образы с GNOME, KDE, XFCE, LXDE, MATE и KDE-minimal. Загрузить
образы можно с зеркал, при помощи торрентов и jigdo. Также доступны
delta-образы, позволяющие сделать из DVD образа Fedora RFRemix.


-  Установочные диски [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/18/RFRemix/i386/iso/>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/18/RFRemix/x86_64/iso/>`__
   ]
-  Образы Live [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/18/Live/i686>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/18/Live/x86_64/>`__
   ]
-  Торренты [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/18/RFRemix/i386/torrents/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/18/RFRemix/x86_64/torrents/>`__
   ]

**Обновление**

Для обновления дистрибутива была создана новая утилита fedup. Она
позволяет обновить Fedora/RFRemix 17 до 18-й версии. Обновление с 16-й
версии не поддерживается. Для обновления необходимо выполнить следующие
команды (для 32-х битных систем вместо x86\_64 укажите в url i386):

`` # yum install fedup # fedup-cli --network 18 --debuglog fedupdebug.log --instrepo=http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/18/RFRemix/x86_64/os/``
**Поддержка**

-  `Баг-трекер <http://redmine.russianfedora.ru/>`__
-  `Форум <http://forum.russianfedora.ru/>`__
-  Jabber-конференция fedora@conference.jabber.ru

Следующая версия RFRemix 19 ожидается в мае одновременно с Fedora 19
(Schrödinger's Cat). Помимо этого незадолго до выхода Fedora 18-Beta
выйдет обновление RFRemix 18.1.
