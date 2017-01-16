.. title: RFRemix 20-Beta и RFRemix 19.1
.. slug: rfremix-20-beta-и-rfremix-191
.. date: 2013-11-12 17:01:24
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Сегодня в один день мы выпускаем два дистрибутива. Бета-версию RFRemix
20 и обновление 19-й версии RFRemix 19.1. Оба дистрибутива основаны на
официальных репозиториях Fedora, RPM Fusion и Russian Fedora. Как обычно
из коробки доступны мультимедиа кодеки, Adobe Flash и некоторые
дополнительные пакеты. В RFRemix 20-Beta браузер Chromium убран с диска
для экономии места.


**Изменения RFRemix 20-Beta:**

#. Возвращена возможность использования VPN в инсталляторе. В 19-й
   версии это было не возможно;
#. Поддержка репозиториев RPM Fusion и Russian Fedora в установщике;
#. Исправлена установка минимальных режимов для GNOME и KDE;
#. FreeType собран с поддержкой **subpixel rendering** и **subpixel
   hinting**;
#. Fontconfig использует **патчи из Ubuntu** для лучшего отображения на
   LCD мониторах;
#. Taglib 1.9 пропатчен **исправленным патчем от rusxmms** (патч
   отправлен автору, спасибо Taurus), что позволяет некоторым плеерам
   (vlc, qmmp) корректно отображать mp3 файлы с тегами в CP1251. На
   Gstreamer это сейчас не распространяется;
#. Unzip правильно **обрабатывает кириллицу**.

Для загрузки доступны DVD образы, образы сетевой установки, а также
Live-образы с GNOME, KDE, XFCE, LXDE и MATE. Загрузка образов возможна
через torrent.


-  Установочные диски [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/RFRemix/20-Beta/RFRemix/i386/iso/>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/RFRemix/20-Beta/RFRemix/x86_64/iso/>`__
   ]
-  Образы Live [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/RFRemix/20-Beta/Live/i686>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/RFRemix/20-Beta/Live/x86_64/>`__
   ]
-  Торренты [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/20-Beta/RFRemix/i386/torrents/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/20-Beta/RFRemix/x86_64/torrents/>`__
   ]

**Изменения RFRemix 19.1:**

#. Актуальные обновления на 9 ноября 2013;
#. Исправлена установка минимальных режимов для GNOME и KDE;
#. Пропатченный taglib доступен в репозитории;
#. Исправлена установка Eclipse с диска;
#. На диск с KDE minimal добавлен конфигуратор тачпанели;
#. И как всегда пересобранные Freetype, Fontconfig и unzip с поддержкой
   кириллицы.


Для загрузки доступны DVD образы, образы сетевой установки, образы
delta, а также Live-образы с GNOME, KDE, XFCE, LXDE, MATE и KDE-minimal.

Загрузка образов возможна через torrent.


-  Установочные диски [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/19.1/RFRemix/i386/iso/>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/19.1/RFRemix/x86_64/iso/>`__
   ]
-  Образы Live [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/19.1/Live/i686>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/19.1/Live/x86_64/>`__
   ]
-  Торренты [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/19.1/RFRemix/i386/torrents/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/19.1/RFRemix/x86_64/torrents/>`__
   ]

Все найденные ошибки просьба отправлять в наш
`redmine.russianfedora.pro <http://redmine.russianfedora.pro>`__.

Срочную поддержку можно получить в конференции
**fedora@conference.jabber.ru**.

Выпуск финальной версии RFRemix 20 ожидается одновременно с выпуском
Fedora 20 в декабре.

