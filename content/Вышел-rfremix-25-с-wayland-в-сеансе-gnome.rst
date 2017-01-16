.. title: Вышел RFRemix 25 - с Wayland в сеансе GNOME
.. slug: Вышел-rfremix-25-с-wayland-в-сеансе-gnome
.. date: 2016-11-22 17:45:47
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro


Доступен для загрузки RFRemix 25, ремикс основанный на репозиториях
Fedora, RPM Fusion и Russian Fedora. На этот раз RPM Fusion оправился от
всех своих болячек и сделал все свои репозитории в срок. Fedora/RFRemix
25 - это первый релиз, в котором рабочий стол GNOME по-умолчанию
использует Wayland. Одни говорят, что это хорошо, у других не всё так
гладно, но начало положено.

**Что у нас нового и старого**

-  Для загрузки доступны две большие редакции RFRemix Server и
   Workstation (включая сетевые установки), а также Live-образы с
   различными рабочими столами;
-  Различные мультимедиа-кодеки, которых нет в оригинальной Fedora, а
   также Flash доступны из коробки;
-  Многие пакеты из репозиториев Russian Fedora доступны из приложения
   GNOME Software (Программы);
-  Так же у нас пересобран freetype с subpixel rendering;
-  Fontconfig содержит патчи Ubuntu для LCD мониторов (в общем сломали
   шрифты как всегда) и навсегда выкинули infinality, который не
   работал;
-  В образы Workstation (GNOME 3.22) по умолчанию для GNOME Shell (не
   для GTK) используется тема Korora из `одноименного
   проекта <https://kororaproject.org/>`__. Также опционально добавлены
   темы Adapta и EvoPop для GTK и иконки EvoPop. Все отключается и
   включается в ``gnome-tweak-tool``;
-  В репозитории содержится почти всевозможный набор мессенджеров:
   skype, viber, telegram-desktop. Также есть Chromium с pepper-flash,
   полный набор Opera и обычный flash-plugin.

-  Хромиум пересобран с поддержкой GTK3 и правильных кодеков;
-  Также мы обновили систему сборки. Теперь Live-образы максимально
   схожи с апстримовскими.


Как было сказано по умолчанию GNOME использует Wayland. Если вам такое
поведение не подходит, то можно переключиться на Xorg в меню выбора
сеанса.


**Образы**

Для загрузки доступны Live образы Workstation (GNOME), KDE (Plasma 5),
LXDE, XFCE, MATE и Cinnamon. DVD и netinstall образ RFRemix Server и
netinstall образ RFRemix Workstation.


-  RFRemix Server [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/25/Server/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/25/Server/x86_64/iso/>`__
   ]
-  RFRemix Workstation [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/25/Workstation/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/25/Workstation/x86_64/iso>`__
   ]
-  Образы Live [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/25/Spins/i386/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/25/Spins/x86_64>`__
   ]
-  Торренты [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/25/Torrents/i386/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/25/Torrents/x86_64>`__
   ]

**Куда сходить спросить, пожаловаться**

-  `Баг-трекер <http://redmine.russianfedora.pro/>`__
-  `Группа в Telegram <https://telegram.me/russianfedora>`__

**Обновление**

Для обновления с предыдущих версий желательно сперва обновить текущую
систему, а затем отдайте команду:

::

    dnf --releasever=25 distro-sync --refresh --nogpgcheck

.. image:: http://tigro.info/wp/wp-content/uploads/2016/11/Выделение_024.png
   :width: 408px
   :height: 306px
   :target: http://tigro.info/wp/wp-content/uploads/2016/11/Выделение_024.png
   :align: center
