.. title: Пакеты Russian Fedora в GNOME Software
.. slug: Пакеты-russian-fedora-в-gnome-software
.. date: 2014-06-25 12:58:59
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Не так давно Игорь Гнатенко поднял
`вопрос <https://lists.fedoraproject.org/pipermail/ru-users/2014-June/000053.html>`__
о том, что пакеты из репозиториев Russian Fedora никак не отображаются в
приложении GNOME Software (вы понятное дело его не используете, потому
что YUM и консоль, но тем не менее). Проблема заключалась в том, что для
отображения пакетов нужно сгенерировать специальные xml и картинки к
ним.


| 

.. raw:: html

   <div align="center">

|GNOMEsoftware|

.. raw:: html

   </div>

В Fedora это решалось поставкой специального пакета ``appstream-data``.
Мы же подумали и, сгенерив всё необходимое, добавили иконки и xml файлы
к пакетам ``russianfedora-free-release`` и
``russianfedora-nonfree-release``. Теперь самые важные пакеты, например,
Chromium, deadbeef, Sauerbraten и др. можно искать и устанавливать через
GNOME Software. Данная фича доступна в RFRemix 20 и вот прям скоро будет
в Rawhide. Вам нужно будет только обновиться.


| 

.. raw:: html

   <div align="center">

|GNOMEsoftwareChromium|

.. raw:: html

   </div>

.. |GNOMEsoftware| image:: http://tigro.info/wp/wp-content/uploads/2014/06/Снимок-экрана-из-2014-06-25-123842-1024x581.png
   :class: aligncenter size-large wp-image-2981
   :width: 720px
   :height: 408px
   :target: http://tigro.info/wp/wp-content/uploads/2014/06/Снимок-экрана-из-2014-06-25-123842.png
.. |GNOMEsoftwareChromium| image:: http://tigro.info/wp/wp-content/uploads/2014/06/Снимок-экрана-из-2014-06-25-123837-1024x581.png
   :class: aligncenter size-large wp-image-2982
   :width: 720px
   :height: 408px
   :target: http://tigro.info/wp/wp-content/uploads/2014/06/Снимок-экрана-из-2014-06-25-123837.png
