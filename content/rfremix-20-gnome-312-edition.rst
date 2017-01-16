.. title: RFRemix 20 GNOME 3.12 Edition
.. slug: rfremix-20-gnome-312-edition
.. date: 2014-04-07 17:44:40
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Не так давно для Fedora 20 (как впрочем и для 19, и для RHEL 7),
появился `репозиторий <http://copr.fedoraproject.org/coprs/rhughes/>`__
с GNOME 3.12. В результате мы собрали Live образ RFRemix с новым рабочим
столом GNOME. Для загрузки доступны `32-х и 64-х битные
образы <http://mirror.yandex.ru/fedora/russianfedora/stage/20-GNOME-3-12-LIVE/>`__.

Загрузить можно через torrent. В будущем, по мере выпуска GNOME 3.12.1,
3.12.2 и т. д., образы будут обновляться. На данный момент что-то
конечно подглючивает, но пользоваться вполне можно.


.. raw:: html

   <div align="center">

|Рабочий стол GNOME 3.12|

.. raw:: html

   </div>

Что нужно знать, используя этот образ:

#. GNOME 3.12 берётся из репозитория
   `rhughes <http://copr.fedoraproject.org/coprs/rhughes/f20-gnome-3-12/>`__.

   Это пакеты пересобранные под Fedora 20 из rawhide. Пакеты
   пересобирались в системе сборки copr и не подписаны. Поддерживать
   репозиторий обещают до выхода Fedora 21;
#. Реопзиторий rhughes местами конфликтует с RPM Fusion, например, пакет
   mpv. Для разрешения подобных проблем, был создан репозиторий
   `rfr20-gnome <http://koji.russianfedora.pro/kojifiles/repos/rfr20-gnome-build/latest/>`__
   на `koji.russianfedora.pro <http://koji.russianfedora.pro>`__;
#. Образ можно обновлять yum-ом. Все нужные репозитории подключены.


Известные проблемы:

#. GNOME Initial Setup окончательно испортили. Он теперь игнорирует
   наличие нескольких раскладок и пытается воткнуть нужную по своему
   разумению. Таймзону ищет исключительно латиницей. Из-за путаницы с
   раскладками может упасть на создании пароля. Чтобы с ним не мучится,
   создайте пользователя в инсталляторе в процессе установки. Есть и
   положительные качества. Initial Setup не стартует после первого входа
   в систему;
#. Сломали индикаторы клавиатуры, которые можно было использовать при
   смене раскладки. Есть и плюс. Починили горячие клавиши если раскладка
   не английская.


.. |Рабочий стол GNOME 3.12| image:: http://tigro.info/wp/wp-content/uploads/2014/04/Выделение_298-1024x616.png
   :class: aligncenter size-large wp-image-2938
   :width: 720px
   :height: 433px
   :target: http://tigro.info/wp/wp-content/uploads/2014/04/Выделение_298.png
