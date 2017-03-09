.. title: Планы GNOME на Wayland
.. slug: Планы-gnome-на-wayland
.. date: 2013-08-06 10:35:36
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| На прошедшем `GUADEC <https://www.guadec.org/>`__ были пересмотрены и
  скорректированы ближайшие планы GNOME по поддержке Wayland, о чем нам
  `рассказывает <http://blogs.gnome.org/mclasen/2013/08/05/gnome-wayland-plans/>`__
  в своем блоге `Matthias
  Clasen <https://fedoraproject.org/wiki/User:Mclasen>`__. Запланировано
  следующее:

-  К версии 3.10 будет доступно технологическое превью GNOME shell на
   Wayland.

-  GNOME shell будет Wayland-композитором, и будет работать на базе KMS,
   а не как X11 nested приложение (`как сейчас по умолчанию работает
   Weston в
   Fedora <https://www.linux.org.ru/gallery/screenshots/8602816>`__).

-  Довольно значительные изменения приходится вносить в Mutter. Пока
   изменения для Wayland будут в отдельном бранче.

-  В дистрибутивах будет два бинарника gnome-shell - для X11 и для
   Weston.

-  Будет работать конфигуратор дисплея.

-  Система ввода в 3.10 не будет переведена на Wayland (в будущих
   релизах будет использоваться специально модифицированная IBus)
-  Возможно GDM не будет модифицирован в срок, и gnome-shell придется
   запускать вручную из init 3.

| 
| Очень интересно обратить внимание на то, что точно не будет работать в
  3.10 (touchpad, специальные возможности, кое-какие полноэкранные
  функции, буфер обмена и т.п.) - с полным списком текущих регрессий
  `можно ознакомиться на специальной
  странице <https://wiki.gnome.org/ThreePointNine/Features/WaylandSupport>`__.

| В это же время проводится работа по портированию отдельных компонентов
  GNOME на Wayland. Недавно было анонсировано, что `GNOME System Monitor
  3.9.5 работает с
  Wayland <http://news.softpedia.com/news/GNOME-System-Monitor-3-9-5-Works-in-Wayland-373112.shtml>`__.

