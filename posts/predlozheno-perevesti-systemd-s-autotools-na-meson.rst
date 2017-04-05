.. title: Предложено перевести systemd с autotools на Meson
.. slug: predlozheno-perevesti-systemd-s-autotools-na-meson
.. date: 2017-04-05 16:53:48 UTC+03:00
.. tags: meson, systemd, autotools
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Похоже, что `система сборки Meson <http://mesonbuild.com/>`_ потихоньку
взлетает. Не так давно было `предложено перевести на Meson сборку libdrm
<https://lists.freedesktop.org/archives/dri-devel/2017-March/135889.html>`_,
затем `Eric Anholt <https://github.com/anholt>`_ попробовал `перевести на
сборку с Meson X.org <http://anholt.livejournal.com/52574.html?nojs=1>`_, и вот
совсем недавно `Zbigniew Jędrzejewski-Szmek
<https://fedoraproject.org/wiki/User:Zbyszek>`_ предложил `cобирать systemd с
помощью Meson <https://github.com/systemd/systemd/pull/5704>`_.

Жаль, что CMake даже не упоминают, хотя у него синтаксис нравится не всем.
