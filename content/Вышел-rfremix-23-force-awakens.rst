.. title: Вышел RFRemix 23 (The Force Awakens)
.. slug: Вышел-rfremix-23-force-awakens
.. date: 2015-11-03 20:18:58
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Что ж, RFRemix 23 всё-таки вышел. Казалось, что 21-я версия будет
последней, но нет. Но самое интересное, это всё было не трудно. Похоже
Fedora (особенно та часть, которую делают в Red Hat) и впрямь стала
стабильной. Помнится 14-ю версию `приходилось делать до раннего
утра <http://tigro.info/wp/?p=1968>`__.


.. raw:: html

   <div align="center">

|RFRemix Workstation|

.. raw:: html

   </div>

**Что было переделано.**

-  Для начала полностью изменен подход к формированию сценариев для
   сборки образов (kickstart-файлы). Это позволило использовать
   оригинальные файлы от Fedora и `дополнять их файлами
   RFRemix <https://github.com/Tigro/spin-kickstarts-rfremix/tree/f23/master>`__;
-  Добавлены окружения RFRemix Server и RFRemix Workstation, которые
   устанавливаются в соответствующих образах по умолчанию. Здесь
   пришлось исправлять пакеты fedora-productimg-server и
   fedora-productimg-workstation, а также comps файлы в репозитории;
-  На данный момент с RPM Fusion [STRIKEOUT:не]\ большая беда. Они
   пытаются по быстрому собрать пакеты для 23-й Fedora, но на данный
   момент есть только часть. Хорошая новость в том, что к 23-й Fedora
   подходят пакеты из 22-й. В RFRemix на данный момент подключены как
   репозитории 22-й, так и development и updates-testing репозитории
   23-й Fedora. С выходом правильных release пакетов ситуация должна
   исправиться автоматически;
-  Так же у нас пересобран freetype с subpixel rendering и subpixel
   hinting;
-  Fontconfig содержит патчи Ubuntu для LCD мониторов (в общем сломали
   шрифты);
-  Есть пакет fontconfig-infinality, но возможно он делает не то, что
   ожидается;
-  В образы Workstation (GNOME 3.18) добавлена поддержка некоторых тем,
   Ozon для GNOME Shell, EvoPop для GTK и иконок. Как и все хорошие
   начинания, они почти не поддерживаются, поэтому только опционально;
-  В репозитории содержится почти всевозможный набор мессенджеров:
   skype, viber, telegram-desktop. Также есть Chromium с pepper-flash,
   полный набор Opera и обычный flash-plugin.


**Образы**

Для загрузки доступны Live образы Workstation, KDE (Plasma 5), LXDE,
XFCE, MATE и Cinnamon. DVD и netinstall образ RFRemix Server и
netinstall образ RFRemix Workstation.


-  RFRemix Server [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/23/Server/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/23/Server/x86_64/iso/>`__
   ]
-  RFRemix Workstation [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/23/Workstation/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/23/Workstation/x86_64/iso-EFI-FIX/>`__
   ]
-  Образы Live [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/23/Live/i686/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/23/Live/x86_64-EFI-FIX>`__
   ]

**Обновление**

Для обновления с RFRemix 21/22 можно воспользоваться плагином для dnf
dnf-plugin-system-upgrade. Это замена fedup. Принцип работы довольно
простой и надёжный. Сперва закачиваются пакеты, а ставятся они после
перезагрузки системы. Но как обычно всё может сломаться, плюс следует
внимательно отнестись к разрешению зависимостей, особенно RPM Fusion.


**Куда сходить спросить, пожаловаться**

-  `Баг-трекер <http://redmine.russianfedora.pro/>`__
-  Jabber-конференция fedora@conference.jabber.ru

.. |RFRemix Workstation| image:: http://tigro.info/wp/wp-content/uploads/2015/11/QEMU_037-1024x766.png
   :class: aligncenter size-large wp-image-3124
   :width: 720px
   :height: 539px
   :target: http://tigro.info/wp/wp-content/uploads/2015/11/QEMU_037.png
