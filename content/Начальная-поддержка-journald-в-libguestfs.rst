.. title: Начальная поддержка journald в libguestfs
.. slug: Начальная-поддержка-journald-в-libguestfs
.. date: 2013-08-02 15:35:54
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Rich W.M. Jones <http://people.redhat.com/~rjones/>`__ сообщил в своем
блоге, что `libguestfs теперь поддерживает journald в гостевых
системах <https://rwmj.wordpress.com/2013/07/30/journal-support-in-libguestfs/>`__.

Пока поддержка, скажем сразу, не впечатляет по возможностям (сначала
журнал копируется на рабочую машину, а там уже просматривается), но Rich
уже задумался о реализации команды journal в guestfish.

