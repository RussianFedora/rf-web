.. title: В systemd включили возможность сборки с Meson
.. slug: v-systemd-vkliuchili-vozmozhnost-sborki-s-meson
.. date: 2017-04-25 17:03:01 UTC+03:00
.. tags: systemd, meson
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Разработчики systemd `одобрили pull-request
<https://github.com/systemd/systemd/pull/5704/commits>`_, в котором добавлялась
`возможность сборки с Meson
</posts/predlozheno-perevesti-systemd-s-autotools-na-meson/>`_. PR состоял из
80 коммитов, и потребовал уйму усилий, о чем `с гордостью пишет
<https://in.waw.pl/~zbyszek/blog/systemd-meson.html>`_ автор, `Zbigniew
Jędrzejewski-Szmek <https://fedoraproject.org/wiki/User:Zbyszek>`_, в своем
блоге.

Из плюсов Meson, Zbigniew особо отмечает на порядок возросшую скорость сборки,
и понятный синтаксис. Ничего не поделать, Autotools, с его юниксвэем, и
поддержкой всех компиляторов в мире и юникс-систем из 1980х, не может
конкурировать по производительности с современными средствами конфигурирования
и сборки.
