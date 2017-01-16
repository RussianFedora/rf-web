.. title: Вышел RFRemix 25 Beta
.. slug: Вышел-rfremix-25-beta
.. date: 2016-10-12 21:53:26
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Для загрузки доступен RFRemix 25 Beta. Всё как обычно, как и раньше. Для
загрузки доступны Live-образы KDE, LXDE, XFCE, MATE, Cinnamon, а также
Workstation версия с GNOME 3.22. Доступна Серверная редакция, образы
сетевой установки и установочный DVD образ Workstation (не известно
зачем, но в Fedora решили тоже его собирать).


| 

|25|

RFRemix основан на репозиториях Fedora, RPM Fusion, **который за полгода
стал живее всех живых, вот что делает с проектами нормальная
инфраструктура**, и на репозиториях Russian Fedora. Fedora с каждым
релизом становится всё лучше и лучше и всё меньше изменений требуется
вносить в образы.


**Основные отличия**

-  Freetype пересобран с subpixel rendering.

-  Fontconfig содержит патчи Ubuntu для LCD мониторов (в общем сломали
   шрифты как всегда).

-  В образы Workstation по умолчанию для GNOME Shell (не для GTK)
   используется тема Korora из `одноименного
   проекта <https://kororaproject.org/>`__. Также опционально добавлены
   темы Adapta и EvoPop для GTK и иконки EvoPop. Все отключается и
   включается в ``gnome-tweak-tool``.
-  В репозитории содержится почти всевозможный набор мессенджеров:
   skype, viber, telegram-desktop. Также есть Chromium с pepper-flash,
   полный набор Opera и обычный flash-plugin.

-  Мы продолжаем провайдить Chromium, так как тот что в репозитории
   Fedora очень плохо работает с видео.

-  Telegram теперь собирается из исходников.


-  RFRemix Server [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/test/releases/RFRemix/25_Beta/Server/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/25_Beta/Server/x86_64/iso/>`__
   ]
-  RFRemix Workstation [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/test/releases/RFRemix/25_Beta/Workstation/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/25_Beta/Workstation/x86_64/iso>`__
   ]
-  Образы Live [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/25_Beta/Live/i686/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/25_Beta/Live/x86_64>`__
   ]

**Куда сходить спросить, пожаловаться**

-  `Баг-трекер <http://redmine.russianfedora.pro/>`__
-  Jabber-конференция fedora@conference.jabber.ru
-  `Группа в Telegram <https://telegram.me/russianfedora>`__

**Обновление**

Для обновления с предыдущих версий RFRemix нужно сперва полностью
обновить текущую систему, а затем отдайте команду:

::

    dnf --releasever=25 distro-sync --nogpgcheck

Релиз RFRemix 25 намечен на 15 ноября одновременно с релизом Fedora.


.. |25| image:: http://tigro.info/wp/wp-content/uploads/2016/10/25-1024x768.png
   :class: aligncenter size-large wp-image-3293
   :width: 600px
   :height: 450px
   :target: http://tigro.info/wp/wp-content/uploads/2016/10/25.png
