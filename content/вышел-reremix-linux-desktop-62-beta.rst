.. title: Вышел RERemix Linux Desktop 6.2 Beta
.. slug: вышел-reremix-linux-desktop-62-beta
.. date: 2012-02-07 15:14:58
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Итак, спустя три месяца с момента выхода Alpha версии доступен для
загрузки RERemix Linux Desktop 6.2 Beta. RERemix основан на репозиториях
Scientific Linux 6.2 (6rolling на данный момент), EPEL, ELRepo,
`PUIAS <http://puias.math.ias.edu/>`__ и Russian Fedora. Дистрибутив в
первую очередь представляет десктопное решение на базе GNOME и KDE
(также поддерживается урезанная версия XFCE) с долгосрочной поддержкой.

Из коробки доступна поддержка мультимедиа и flash-plugin, новые версии
популярных программ. По сравнению с 6 Alpha перестал использоваться
репозиторий RPM Forge (из-за совместимости с другими репозиториями).

Поэтому лучше устанавливать бета-версию с нуля, чтобы не было
конфликтов. Многие фичи были портированы из дистрибутивов RFRemix:

#. Быстрая установка GNOME, KDE, XFCE;
#. Поддержка всех используемых сетевых репозиториев во время установки
   по сети;
#. Поддержка VPN во время установки;
#. Firstboot с дополнительными опция (настройка GNOME, режим работы sudo
   и др.);
#. Выбор различных клавиатурных комбинация для смены русской раскладки и
   индикаторы в панелях GNOME и KDE;
#. Freetype пересобран с запатентованными компонентами.


В RERemix 6.2 Beta обновлены:

#. Firefox, Thunderbird до версии 10.0
#. LibreOffice 3.4.5 вместо OpenOffice.org
#. В репозитории Russian Fedora доступны psi-plus, qbittotrrent, djvu
   backend для evince, deluge, deadbeef, плагины к qmmp, skype, opera и
   др.

#. Добавлены программы для управления pulseaudio (paman, paprefs,
   pavucontrol, pavumeter).


Для загрузки доступны образы DVD, netinstall и Live с GNOME и KDE. На
Live KDE по умолчанию идёт плеер VLC.


.. raw:: html

   <div align="center">

|image0|

.. raw:: html

   </div>

.. raw:: html

   <div align="center">

|image1|

.. raw:: html

   </div>

-  Установочные диски [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/6.2-Beta/RERemix/i386/iso/>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/6.2-Beta/RERemix/x86_64/iso/>`__
   ]
-  Live-образы [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/6.2-Beta/Live/i686/>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/6.2-Beta/Live/x86_64/>`__
   ]
-  Список пакетов [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/6.2-Beta/RERemix/i386/os/Packages/>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/test/6.2-Beta/RERemix/x86_64/os/Packages/>`__
   ]

Чем вы можете помочь?
^^^^^^^^^^^^^^^^^^^^^

Нам не хватает майнтейнеров для пакетов. Например XFCE сейчас не
содержит привычных плагинов, есть только базовые компоненты. Ели вы
хотите помочь, то прочитайте `этот
документ <http://wiki.russianfedora.ru/index.php/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%B0_%D0%B2_%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_RussianFedora>`__.

Все найденные ошибки следует отправлять в багтрекер
`redmine.russianfedora.ru <http://redmine.russianfedora.ru>`__.

Финальная версия RERemix Linux Desktop 6.2 должна появиться очень скоро,
сразу после официального выхода Scientific Linux 6.2.

.. |image0| image:: http://tigro.info/wp/wp-content/uploads/2012/02/Выделение_052-600x452.png
   :width: 600px
   :height: 467px
.. |image1| image:: http://tigro.info/wp/wp-content/uploads/2012/02/Выделение_047-600x450.png
   :width: 600px
   :height: 450px
