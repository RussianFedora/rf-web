.. title: Новости RISC-V
.. slug: novosti-risc-v
.. date: 2017-01-19 18:26:43 UTC+03:00
.. tags: riscv, fedora, gcc
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

`Положительно завершается процесс добавления поддержки архитектуры RISC-V в GCC <https://gcc.gnu.org/ml/gcc/2017-01/msg00148.html>`_. К сожалению, процесс был сильно заторможен юристами, поэтому не факт, что успепют в срок для GCC 7. Дело в том, что разработка шла в университете Беркли, и `их юристы были потив того, чтобы копирайт на работу был передан FSF <https://groups.google.com/a/groups.riscv.org/forum/#!topic/sw-dev/Kb0f6ETkR0Y>`_. Пришлось даже `переписать все с чистого листа <https://gcc.gnu.org/ml/gcc-patches/2017-01/msg00776.html>`_.

Нам это все интересно, потому что сравнительно недавно наш коллега, Rich W.M. Jones <http://people.redhat.com/~rjones/>`_, объявил о том, что `он работает над поддержкой RISC-V в Fedora </content/Новости-secondary-arch-в-fedora/>`_. Он использовал для сборки первый, заблокированный юристами, порт GCC, и с ним добился видимого прогресса - `готовы образы Fedora для загрузки в эмуляторе <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/4XIC2ZKIFGXSP6FDXFLBRFSQZV4RJMQN/>`_. В качестве эмулятора можно использовать Qemu, а `можно и более экзотичный RISCVEMU <https://rwmj.wordpress.com/2016/12/20/fabrice-bellards-riscvemu-supports-fedorarisc-v/>`_. В процессе пересборки Rich был вынужден вносить патчи для самых разных компонентов, таких, как `RPM <https://github.com/rpm-software-management/rpm/pull/81>`_ и `systemd <https://github.com/systemd/systemd/commit/171b533>`_. Текущее состояние дел можно узнать на `странице рабочей группы RISC-V в Fedora <https://fedoraproject.org/wiki/Architectures/RISC-V>`_

Для любопытствующих, вот так примерно и выглядит разработка и продвижение новой микропроцессорной архитектуры. Сравните, например, с отечественными экспериментами разработки микропроцессоров, которые проводятся неизвестно кем, неизвестно где, и с неясными перспективами.
