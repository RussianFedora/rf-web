.. title: Вышел RFRemix 20
.. slug: Вышел-rfremix-20
.. date: 2013-12-17 17:59:18
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Как обычно в день релиза новой версии дистрибутива Fedora 20 мы
анонсируем RFRemix 20. Это уже одиннадцатый ремикс, выпущенный Russian
Fedora. Первый был RFRemix 10, выпущенный в 2008 году. Ремикс основан на
репозиториях Fedora, RPM Fusion и Russian Fedora. Как обычно из коробки
доступны мультимедиа кодеки, Adobe Flash и некоторые дополнительные
пакеты.


**Основные изменения в RFRemix 20 относительно Fedora:**

#. Поддержка репозиториев RPM Fusion и Russian Fedora в установщике;
#. Исправлена установка минимальных режимов GNOME и KDE;
#. FreeType собран с поддержкой **subpixel rendering** и **subpixel
   hinting**;
#. Fontconfig использует **патчи из Ubuntu** для лучшего отображения на
   LCD мониторах;
#. Taglib 1.9 пропатчен **исправленным патчем от rusxmms** (патч
   отправлен автору, спасибо Taurus), что позволяет некоторым плеерам
   (vlc, qmmp) корректно отображать mp3 файлы с тегами в CP1251;
#. Unzip правильно **обрабатывает кириллицу**;
#. `Исправлены проблемы с горячими
   клавишами <https://github.com/RussianFedora/gnome-settings-daemon/blob/f20/fixes/non-eng-hotkeys.patch>`__
   в некоторых приложениях (например LibreOffice), когда раскладка не
   английская. **Спасибо ROSA**;
#. `Исправлены проблемы с разворачиванием
   flash <https://github.com/RussianFedora/mutter/blob/f20/fixes/mutter-3.8.3-fullscreen-flash-player.patch>`__
   на полный экран. **Спасибо ROSA**.

Для загрузки доступны DVD образы, образы сетевой установки, файлы разниц
относительно Fedora 20, а также Live-образы с GNOME, KDE, KDE-minimal,
XFCE, LXDE и MATE. Загрузка образов возможна через http (ftp, rsync -
просто поменяйте протокол), torrents и jigdo.


-  Установочные диски [
   `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20/RFRemix/i386/iso/>`__
   ] [
   `x86\_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20/RFRemix/x86_64/iso/>`__
   ]
-  Образы Live [
   `i686 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20/Live/i686>`__
   ] [
   `x86\_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20/Live/x86_64/>`__
   ]
-  Торренты [
   `i386 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20/RFRemix/i386/torrents/>`__
   ] [
   `x86\_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20/RFRemix/x86_64/torrents/>`__
   ]
-  Jigdo [
   `i386 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20/RFRemix/i386/jigdo/>`__
   ] [
   `x86\_64 <https://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20/RFRemix/x86_64/jigdo/>`__
   ]

Все найденные ошибки просьба отправлять в наш
`redmine.russianfedora.pro <http://redmine.russianfedora.pro>`__.

Срочную поддержку можно получить в конференции
**fedora@conference.jabber.ru**.

Для обновления с RFRemix 20-Beta достаточно просто обновить систему. Для
обновления с RFRemix 19 (19.1) можно воспользоваться утилитой
rfremix-upgrade.


Что касается планов на будущее, как обычно весной будут следующие версии
RFRemix, 20.1 и 21-Beta, но также возможно мы опять вернёмся к RERemix
на базе 7 CentOS.

