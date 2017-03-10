.. title: Выпущены RFRemix 21 и RFRemix 20.1
.. slug: Выпущены-rfremix-21-и-rfremix-201
.. date: 2014-12-10 19:01:14
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Итак, одновременно с выпуском Fedora 21 вышел RFRemix 21, ремикс,
основанный на репозиториях Fedora, RPM Fusion и Russian Fedora. Нынешний
релиз Fedora разделён на три продукта: Workstation, Server и Cloud.

RFRemix состоит только из варианта Workstation и содержит образ Live и
образ сетевой установки. Также есть live-образы с различными рабочими
столами. В качестве Server и Cloud разумнее использовать варианты из
Fedora.


RFRemix 21 включает KDE 4.14, GNOME 3.14, MATE 1.8, Firefox 34, Kernel
3.17.4, LibreOffce 4.3.4, Chromium 39, Adobe и Pepper Flash, поддержку
мультимедиа из коробки. В репозитории есть также Viber, Skype, драйвера
Nvidia и много чего ещё. Краткий обзор новых фич Fedora 21 `доступен по
ссылке <https://www.opennet.ru/opennews/art.shtml?num=41221>`__.


| 

.. raw:: html

   <div align="center">

|Cinnamon|

.. raw:: html

   </div>

**Что нового по сравнению с RFRemix 20**

#. Пакеты, в которых изменено брендирование на RFRemix, вынесены в
   отдельный репозиторий
   `branding <http://mirror.yandex.ru/fedora/russianfedora/russianfedora/branding/fedora/development/21/source/SRPMS/>`__.

   В fixes остались лишь пакеты с багфиксами различными патчами
   (например fontconfig и freetype). Поэтому для обновления 20-й версии
   через команду ``yum --releasever=21 distro-sync`` необходимо сперва
   установить пакет
   `russianfedora-branding-release <http://mirror.yandex.ru/fedora/russianfedora/russianfedora/branding/fedora/development/21/i386/os/russianfedora-branding-release-21-1.R.noarch.rpm>`__
   (`#1385 <http://redmine.russianfedora.pro/issues/1385#change-7689>`__);
#. Исправлена проблема с `нелокализованным дисплейным менеджером
   sddm <https://github.com/RussianFedora/sddm/commit/b10428f6a8d294781dcfbda0573a0b4da3763eb3>`__
   (сборка KDE);
#. Исправлено имя продукта, чтобы можно было отправлять ошибки в
   Bugzilla через abrt;
#. Установочного образа DVD больше нет, есть только образ с сетевой
   установкой;
#. Появился live-образ с рабочим столом Cinnamon.


Для обновления с предыдущих версий RFRemix **рекомендуется использовать
команду** ``rfremix-upgrade`` из одноименного пакета. Это
модифицированный скрипт fedora-upgrade.


-  RFRemix Workstation [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/21/Workstation/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/21/Workstation/x86_64/iso/>`__
   ]
-  Образы Live [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/21/Live/i386>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/21/Live/x86_64/>`__
   ]
-  Торренты [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/21/torrents/i386/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/21/torrents/x86_64>`__
   ]

Ошибки можете сообщать в багтрекер
`redmine.russianfedora.pro <http://redmine.russianfedora.pro>`__ или
jabber-конференцию fedora@conference.jabber.ru.


**Также выпущен релиз RFRemix 20.1.** Это полностью штатные обновления,
накопленные почти за год, и исправления некоторых ошибок, включая
отправку ошибок через ABRT в bugzilla Red Hat.


-  Установочные диски [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20.1/RFRemix/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20.1/RFRemix/x86_64/iso/>`__
   ]
-  Образы Live [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20.1/Live/i686>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20.1/Live/x86_64/>`__
   ]
-  Торренты [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20.1/torrents/i386/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/20.1/torrents/x86_64>`__
   ]

И остаётся надеяться, что Fedora 22 выйдет через полгода, а не через
год. А там уже обещают по умолчанию Wayland.


.. |Cinnamon| image:: http://tigro.info/wp/wp-content/uploads/2014/11/QEMU_050.png
   :class: aligncenter size-full wp-image-3036
   :width: 760px
   :height: 567px
   :target: http://tigro.info/wp/wp-content/uploads/2014/11/QEMU_050.png
