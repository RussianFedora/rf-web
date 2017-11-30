.. title: Новости nbdkit
.. slug: novosti-nbdkit
.. date: 2017-11-30 18:10:05 UTC+03:00
.. tags: nbdkit, nbd
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

`Rich W.M. Jones <http://people.redhat.com/~rjones/>`_ анонсировал нововведения
в nbdkit, фреймворке для создания NBD-серверов.

Во-1, `в nbdkit появилась поддержка TLS <https://github.com/libguestfs/nbdkit/commit/c5e7649>`_. К сожалению, для настройки TLS в ndbkit требуется `прочитать длинную инструкцию <https://github.com/libguestfs/nbdkit/blob/master/docs/nbdkit.pod#TLS>`_. Хорошо, что `инструкция по подключению Qemu через TLS к ndbkit <https://www.berrange.com/posts/2016/04/05/improving-qemu-security-part-5-tls-support-for-nbd-server-client/>`_ получилась короче. Но, если вам надо, то разберетесь.

Во-2, `полностью параллельная обработка клиентских запросов <https://www.redhat.com/archives/libguestfs/2017-November/msg00146.html>`_.

В-3, `nbdkit теперь может использовать как бэкенды другие NBD-серверы <https://www.redhat.com/archives/libguestfs/2017-November/msg00079.html>`_.

Готов для десктопа!
