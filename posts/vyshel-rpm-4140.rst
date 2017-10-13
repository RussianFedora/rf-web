.. title: Вышел RPM 4.14.0
.. slug: vyshel-rpm-4140
.. date: 2017-10-13 15:06:02 UTC+03:00
.. tags: rpm, lmdb
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

`Вышел RPM версии 4.14.0
<http://lists.rpm.org/pipermail/rpm-announce/2017-October/000059.html>`_. В
этой версии debuginfo-пакеты можно устанавливать параллельно, и они теперь
разбиваются на пакеты, а не идут монолитным блоком. Помимо этого добавили
поддержку RISCV-64, но самое для нас главное - в этой версии появился еще один
бэкенд для хранения метаданных (напомним `недавнюю историю
</posts/prodolzhenie-istorii-pro-rpm-i-novyi-bekend-khraneniia-dannykh>`_)!

Этот бэкенд написали не с помощью наколеночной базы данных, а с использованием
LMDB <https://github.com/rpm-software-management/rpm/pull/291>`_, которая
неоднократно `показывала чудеса скорости
<http://www.lmdb.tech/bench/microbench/>`_. Самое для нас интересное, что его
разработал еще один непростой человек, `Jeff Johnson
<https://github.com/n3npq>`_, известный больше, как мэйнтейнер RPM5 и один из
первоначальных авторов RPM.

Сама библиотека LMDB разрабатывается тоже непростыми людьми в рамках проекта
OpenLDAP, но, к счастью, для нее есть замена, `libmdbx
<https://github.com/leo-yuriev/libmdbx>`_, которую разрабатывает и использует в
энтерпрайзе, продакшене и хайлоаде наш соотечественник Леонид Юрьев.

.. vimeo:: 235962287
   :align: center
   :height: 320
   :width: 480
