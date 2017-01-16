.. title: И опять новые "фичи" Fedora 18
.. slug: И-опять-новые-фичи-fedora-18
.. date: 2012-07-10 12:44:27
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| На прошедшем заседании FESCo `одобрили новые
  фичи <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/166519/focus=166532>`__
  Fedora 18:

-  В Fedora 18 будут `новые нескучные 256-цветные
   терминалы <https://fedoraproject.org/wiki/Features/256_Color_Terminals>`__.

   Пользователи Mac OS X, которые работают на Linux-машинах через ssh
   будут особенно рады.

-  `CIM
   Management <https://fedoraproject.org/wiki/Features/CIMManagement>`__
   - еще одна фича, предназначенная для т.н. систем "энтерпрайз"-уровня.

-  `Обновление fontconfig до версии
   2.10 <https://fedoraproject.org/wiki/Features/Fontconfig2.10>`__
-  `Обновление Ruby on Rails до версии
   3.2 <https://fedoraproject.org/wiki/Features/Rails_3.2>`__
-  `Обновление Perl до версии
   5.16 <https://fedoraproject.org/wiki/Features/perl5.16>`__
-  Новая суб-архитектура для PowerPC - `Power7
   (ppc64v7) <https://fedoraproject.org/wiki/Features/Power7Subarch>`__.

   Теперь их будет три - ppc, ppc64 и ppc64v7.


| 
| Временно отложили голосование по переработке `системы управления
  display
  manager'ми <https://fedoraproject.org/wiki/Features/DisplayManagerRework>`__,
  которую планируют сделать полностью основанной на systemd (все
  Fedora/Red Hat специфичные скрипты и настройки, такие , как
  /etc/X11/prefdm, будут удалены). Решили рассмотреть принятие после
  другой довольно спорной фичи - `преднастроенные профили
  сервисов <https://fedoraproject.org/wiki/Features/PackagePresets>`__.

  Раньше то, будет-ли запущен сервис после установки записывалось в нем,
  в секции %post spec-файла. А в рамках этого нововведения предлагают
  игнорировать ту информацию и использовать настройки профилей - типа
  "веб-сервер", "рабочая станция", "почтовый сервер", "Fedora Electronic
  Lab" и т.п.
