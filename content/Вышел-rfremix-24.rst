.. title: Вышел RFRemix 24
.. slug: Вышел-rfremix-24
.. date: 2016-06-22 09:11:10
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Доступен для загрузки RFRemix 24. На этот раз с небольшим запозданием,
так как RPM Fusion всё-таки решили выложить свои пакеты для 24-й версии
в updates-testing. Из-за этого пришлось в спешном порядке переделывать
образы. **Но будьте внимательны, пакеты в RPM Fusion Free Updates
Testing не подписаны**. Такая воль kwizard'а. Вообще для Fedora 24
сейчас есть `testing репозиторий
Free <http://download1.rpmfusion.org/free/fedora/updates/testing/24/>`__,
а в качестве `NonFree можно использовать репозиторий от Fedora
23 <http://download1.rpmfusion.org/nonfree/fedora/releases/23/Everything/>`__.


| 

.. raw:: html

   <div align="center">

|gnome|

.. raw:: html

   </div>

**Что у нас нового и старого**

-  Для загрузки доступны две большие редакции RFRemix Server и
   Workstation (включая сетевые установки), а также Live-образы с
   различными рабочими столами;
-  Для поддержки мультимедии используется всё ещё RPM Fusion, у которого
   зашевелилась инфраструктура. Вообще вероятность что он будет жить
   намного выше, чем у проекта
   `unitedrpms.github.io; <https://unitedrpms.github.io/>`__
-  Для RPM Fusion используются немного измененные release-пакеты с
   подключением nonfree от Fedora 23 (для 24-й этого репозитория просто
   нет). Они должны обновиться на оригинальные автоматически, когда RPM
   Fusion будет полностью готов (что как раз и произошло в Fedora 23);
-  Многие пакеты из репозиториев Russian Fedora доступны из приложения
   GNOME Software (Программы);
-  Так же у нас пересобран freetype с subpixel rendering и subpixel
   hinting;
-  Fontconfig содержит патчи Ubuntu для LCD мониторов (в общем сломали
   шрифты как всегда);
-  Пакет fontconfig-infinality был выпилен по просьбам;
-  В образы Workstation (GNOME 3.20) по умолчанию для GNOME Shell (не
   для GTK) используется тема Korora из `одноименного
   проекта <https://kororaproject.org/>`__. Также опционально добавлены
   темы Adapta и EvoPop для GTK и иконки EvoPop. Все отключается и в
   ключается в ``gnome-tweak-tool``;
-  В репозитории содержится почти всевозможный набор мессенджеров:
   skype, viber, telegram-desktop. Также есть Chromium с pepper-flash,
   полный набор Opera и обычный flash-plugin.


**Образы**

Для загрузки доступны Live образы Workstation, KDE (Plasma 5), LXDE,
XFCE, MATE и Cinnamon. DVD и netinstall образ RFRemix Server и
netinstall образ RFRemix Workstation.


-  RFRemix Server [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/24/Server/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/24/Server/x86_64/iso/>`__
   ]
-  RFRemix Workstation [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/24/Workstation/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/24/Workstation/x86_64/iso>`__
   ]
-  Образы Live [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/24/Live/i686/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/24/Live/x86_64>`__
   ]

**Куда сходить спросить, пожаловаться**

-  `Баг-трекер <http://redmine.russianfedora.pro/>`__
-  Jabber-конференция fedora@conference.jabber.ru
-  `Группа в Telegram <https://telegram.me/russianfedora>`__

**Обновление**

В принципе обновление с RFRemix 23 не должно составить проблем. Сперва
полностью обновите текущую систему, а затем отдайте команду:

| ``dnf --releasever=24 distro-sync --nogpgcheck``

**Планы на RFRemix 25**

Так как RPM Fusion пока не оправдывает никаких надежд, у нас появилось
огромное желание собрать всё нужно у себя. Одним словом сделать свой
собственный велосипед. Эта идея не нова, но по крайней мере мы будем
иметь всё что нужно и не зависеть от внешних репозиториев. Так что ждите
RFRemix 25 осенью этого года.


.. |gnome| image:: http://tigro.info/wp/wp-content/uploads/2016/06/gnome-1024x768.png
   :class: aligncenter size-large wp-image-3240
   :width: 600px
   :height: 450px
   :target: http://tigro.info/wp/wp-content/uploads/2016/06/gnome.png
