.. title: Новости DNF 3.0
.. slug: novosti-dnf-30
.. date: 2018-04-05 16:21:21 UTC+03:00
.. tags: dnf, rpm, python, cpp, golang, rust
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Официально `объявили о начале разработки DNF версии 3 <https://rpm-software-management.github.io/announcement/2018/03/22/dnf-3-announcement/>`_. Целями этой версии поставили ускорение работы и консолидация кода из PackageKit, DNF и libdnf в самой libdnf. Уже сейчас получены интересные результаты:

.. image:: https://rpm-software-management.github.io/img/performance_libdnf_0.9.1_to_0.13.0.svg
   :align: center

Библиотека libdnf будет переведена на другой язык, c ANSI C на C++. До этого
Yum переводили с Python на ANSI C, когда выносили часть функционала в сторонние
библиотеки libsolv и hawkey, поэтому можно считать, что это уже второй раз.
Вообще, `выбор языка удивил некоторых наших коллег
<https://www.mail-archive.com/devel@lists.fedoraproject.org/msg122110.html>`_.
Сейчас модно переписывать `сразу на Go
<https://getstream.io/blog/switched-python-go/>`_ или `даже Rust
<http://psychopath.io/switching-from-c-to-rust/>`_ - видимо, это будет
следующий шаг после C++.

Из других интересных новостей про управление пакетами - `OpenMandriva переходит
обратно на RPM <https://forum.openmandriva.org/t/switching-to-rpmv4/1702>`_.
Раньше они переходили на RPM5. В последнее время от них поступали
`пулл-реквесты на GitHub
<https://github.com/rpm-software-management/rpm/pull/417>`_ и вопросы, поэтому
мы что-то такое подозревали, и сильно не удивились. А кто еще остался на своем
форке RPM?
