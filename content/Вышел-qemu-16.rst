.. title: Вышел Qemu 1.6
.. slug: Вышел-qemu-16
.. date: 2013-08-16 09:53:45
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Инженер IBM и разработчик Qemu/KVM, `Anthony
  Liguori <https://www.openhub.net/accounts/aliguori>`__ только что
  `анонсировал <http://thread.gmane.org/gmane.comp.emulators.qemu/228260>`__
  выход новой версии Qemu 1.6.0. `Среди
  новинок <http://wiki.qemu.org/ChangeLog/1.6>`__:

-  Миграция по RDMA.

-  Поддержка aarch64 в TCG (tiny code generator).

-  Поддержка Mac OS X для PowerPC, как гостевых систем.

-  Поддержка "thin provisioning" для qcow2 образов. Теперь команда
   "discard" будет перенаправляться на уровень хостовой файловой
   системы, как раньше уже было задействовано для raw дисков.

-  Qemu предоставляет полный набор ACPI-таблиц в гостевую систему.

-  Поддержка миграции для гостевых систем pSeries.


| 
| И много чего еще. Ждем, когда `будет пересобрано в
  Fedora <http://koji.fedoraproject.org/koji/packageinfo?packageID=3685>`__.

