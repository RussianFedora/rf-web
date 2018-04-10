.. title: RISC-V в Fedora - текущее состояние
.. slug: risc-v-v-fedora-tekushchee-sostoianie
.. date: 2018-04-09 09:59:01 UTC+03:00
.. tags: riscv
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Наш коллега, `Richard W.M. Jones <http://people.redhat.com/~rjones/>`_,
сообщил, что `готовы пакеты и дисковые образы Fedora для 64-битной архитектуры
RISC-V
<https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/WZRKOMQAMOH56V5QK6OLBUHVN6N3ZIGS/>`_.
Теперь Fedora можно запустить в Qemu, а с небольшими дополнительными движениями
и на вскоре выходящей в свободную продажу девборде, `HiFive Unleashed
<https://www.sifive.com/products/hifive-unleashed/>`_. За последнюю придется
заплатить почти 0.15 биткойна (примерно 1000 долларов в устаревших валютах), не
считая доставки.

Самое время, потому что и `Debian тоже добавил поддержку этой архитектуры
<https://groups.google.com/a/groups.riscv.org/forum/#!topic/sw-dev/u4VcUtB9r94>`_.
Собственно, все рванулись как раз после FOSDEM, `когда нам сказали <https://fosdem.org/2018/schedule/event/riscv/>`_, что все,
надо работать над дистрибутивами Linux. Теперь это можно, потому что вся важная
часть уже в upstream (Linux, Binutils, GCC, Glibc).

.. image:: /images/hifive_riscv_fedora.jpg
   :align: center
   :width: 90.0%

.. class:: align-center

Fedora запущена на HiFive Unleashed!

.. image:: /images/hifive_riscv_fedora-2.jpg
   :align: center
   :width: 90.0%

.. class:: align-center

Так выглядит все в сборе.

.. image:: /images/hifive_riscv_fedora-3.jpg
   :align: center
   :width: 90.0%

.. class:: align-center

Fedora обновляется!
