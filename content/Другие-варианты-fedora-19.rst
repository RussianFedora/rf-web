.. title: Другие варианты Fedora 19
.. slug: Другие-варианты-fedora-19
.. date: 2013-07-04 10:55:24
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Сборками Fedora под архитектуру x86/x86\_64 для USB-флэшек список не
  исчерпывается. Одновременно с выходом Fedora 19 стала доступна `сборка
  Fedora 19 для
  PPC64 <http://thread.gmane.org/gmane.linux.redhat.fedora.devel.announce/1101>`__.

  К сожалению, больше нет установочных образов для 32-битной
  архитектуры, только для 64-битного PPC64, хотя обновление на 32-битных
  PowerPC-платформах до последней Fedora все еще возможно:

::

    sulaco ~: uname -a
    Linux sulaco.local 3.10.0-0.rc3.git0.1.fc20.ppc #1 Wed Jun 12 07:34:58 MST 2013 ppc ppc ppc GNU/Linux
    sulaco ~: cat /etc/redhat-release 
    Fedora release 20 (Rawhide)
    sulaco ~:

| 
| Одновременно стала доступна `сборка Fedora 19 для
  ARM <http://thread.gmane.org/gmane.linux.redhat.fedora.arm/6232>`__.

  Как вы знаете, у `Fedora ARM
  SIG <https://fedoraproject.org/wiki/Architectures/ARM>`__ есть
  перспективный план `сделать ARM первичной архитектурой для
  Fedora </content/планы-fedora-arm>`__, наравне с x86 и x86\_64. К
  сожалению, против этого плана ранее был выдвинут очень серьезный
  аргумент - люди выражали сомнения в возможности Fedora ARM SIG
  выпустить релиз одновременно с двумя другими первичными архитектурами.

  И действительно, используя не слишком мощные ARM-машинки было просто
  невозможно скомпилировать все дерево пакетов одновременно с, например,
  x86\_64. Все изменилось, когда `Red Hat заменил старый кластер из
  машинок с 256-512 мегабайтами памяти на мощные системы
  Calxeda </content/Новости-fedora-arm-sig-0>`__. Теперь стало возможным
  сократить отставание до пренебрежимо малого, и теперь для ARM открыт
  путь в список основных архитектур.

| Для счастливых пользователей Google Chromebook `Jon
  Disnard <http://fedoraproject.org/wiki/User:Parasense>`__ `собрал
  rootfs на базе Fedora 19 для
  ARM <https://plus.google.com/u/0/104641385617978618363/posts/NPWaJSnTrbd>`__,
  но официально Fedora еще не поддерживает этот перспективный лэптоп.

  Надо отметить, что инструкция по установке `заметно
  сократилась <https://fedoraproject.org/wiki/Architectures/ARM/Samsung_Chromebook_2012>`__
  с прошлого раза.

| К сожалению, участники `Fedora s390
  SIG <http://fedoraproject.org/wiki/Architectures/s390x>`__ не
  уложились в срок, и не выпустили сборку Fedora 19 одновременно с
  основными архитектурами. Заметим, что `Fedora 18 для
  s390 </content/fedora-18-для-s390-и-ppc64>`__ и `Fedora 17 для
  s390 </content/fedora-17-для-s390x>`__ тоже были выпущены с
  опозданиями.

| Список вариантов установки Fedora не исчерпывается разными
  микропроцессорными архитектурами. Начиная с Fedora 19 появились
  официальные `образы для развертывания в
  облаках <http://fedoraproject.org/en/get-fedora-options#clouds>`__. На
  выбор предоставляется возможность запустить готовую систему в облаке
  Amazon EC2, либо можно скачать образы, которые подходят для
  развертывания в OpenStack, Eucalyptus, CloudStack. Конкретнее, `о
  способе быстро развернуть эти образы в
  OpenStack <http://www.blog.sandro-mathys.ch/2013/07/fedora-19-released-now-with-official.html>`__,
  в своем блоге рассказывает инженер швейцарской компании
  `SystemsX <http://www.systemsx.ch/>`__ `Sandro
  Mathys <http://www.sandro-mathys.ch/p/about-me.html>`__.

