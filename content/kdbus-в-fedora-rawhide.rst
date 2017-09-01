.. title: kdbus в Fedora Rawhide
.. slug: kdbus-в-fedora-rawhide
.. date: 2015-07-30 22:58:16
.. tags: kdbus
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

После `включения поддержки kdbus в сборках ядра для Fedora
Rawhide </content/kdbus-включили-в-fedora-rawhide>`__, он `стал доступен
и в
userspace-приложениях <https://thread.gmane.org/gmane.linux.redhat.fedora.devel/209922>`__!
Для тестирования пока нужно добавить строчку *"kdbus=1"* к параметрам
ядра, и он загрузится systemd автоматически.

Наши участники `уже начали находить ошибки в новой
конфигурации <https://bugzilla.redhat.com/1248783>`__.

