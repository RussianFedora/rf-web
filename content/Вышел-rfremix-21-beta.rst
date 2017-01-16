.. title: Вышел RFRemix 21-Beta
.. slug: Вышел-rfremix-21-beta
.. date: 2014-11-17 14:40:57
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


На этот раз мы немного запоздали с Beta версией. Почти на две недели
позже. Но ничего страшного. На этот раз Beta версия уже почти совсем
похожа на релиз. GNOME так вообще вылечился от детских проблем. Перестал
крашится на двухмониторных конфигурациях и стал вполне себе стабильным.

Также как и Chromium.


Итак. RFRemix включает GNOME 3.14(.2), KDE 4.14(.3), Firefox 33.1, ядро
3.17, LibreOffice 4.3.2.2.

| 

.. raw:: html

   <div align="center">

|gnome-menu|

.. raw:: html

   </div>

**Что нового**

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
   установкой.


**Загрузка**

-  Установочные диски [
   `i686 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/21-Beta/Workstation/i386/iso/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/21-Beta/Workstation/x86_64/iso/>`__
   ]
-  Образы Live [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/21-Beta/Live/i386>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/21-Beta/Live/x86_64/>`__
   ]
-  Торренты [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/21-Beta/torrents/i386/>`__
   ] [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/test/RFRemix/21-Beta/torrents/x86_64>`__
   ]

Релиз намечен на конец года. Ошибки можете сообщать в багтрекер
`redmine.russianfedora.pro <http://redmine.russianfedora.pro>`__ или
jabber-конференцию fedora@conference.jabber.ru.


На следующей неделе будет также выпущен RFRemix 20.1.

.. |gnome-menu| image:: http://tigro.info/wp/wp-content/uploads/2014/11/gnome-menu-1024x584.png
   :class: aligncenter size-large wp-image-3028
   :width: 720px
   :height: 410px
   :target: http://tigro.info/wp/wp-content/uploads/2014/11/gnome-menu.png
