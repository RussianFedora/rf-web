.. title: Коммьюнити Haskell делает первые шаги навстречу systemd
.. slug: Коммьюнити-haskell-делает-первые-шаги-навстречу-systemd
.. date: 2013-10-23 11:20:13
.. tags: haskell, systemd, golang, coreos, etcd
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Fedora Haskell SIG <https://fedoraproject.org/wiki/Haskell_SIG>`__
приветствует появление `библиотеки для использования systemd socket
activation в
Haskell <https://github.com/sakana/haskell-socket-activation>`__. Это,
без всякого сомнения, поможет в разработке высокоинтегрированных в
систему сервисов на этом популярном языке, использующемся, например, в
Facebook, финансовых и телекоммуникационных компаниях стран ЕС, и еще
`двумя российскими программистами для написания однострочных
скриптов <https://www.linux.org.ru/news/conference/9703341>`__.

В других языках программирования ситуация тоже улучшается - есть `бранч
PHP <https://github.com/systemd/php-src>`__, поддерживающий socket
activation, `в Ruby реализовать socket activation оказалось проще
простого <http://ku1ik.com/2012/01/21/systemd-socket-activation-and-ruby.html>`__,
существуют биндинги для Journald для разных языков, но наверное самый
впечатляющий прогресс был достигнут для языка `Go /
Golang <http://golang.org/>`__. После нескольких разрозненных попыток
(`github.com/philips/go-systemd <https://github.com/philips/go-systemd>`__,
`github.com/3M3RY/go-systemd <https://github.com/3M3RY/go-systemd>`__,
`github.com/lemenkov/systemd.go <https://github.com/lemenkov/systemd.go>`__,
`github.com/icub3d/go-systemd-logger <https://github.com/icub3d/go-systemd-logger>`__),
участниками CoreOS была создана общая библиотека для работы с systemd в
golang - `go-systemd <https://github.com/coreos/go-systemd>`__, и
проекты потихоньку начинают переключаться на ее использование. На
использование systemd для работы `постепенно переходит
etcd <https://github.com/coreos/etcd/pull/198>`__, ключевой компонент
CoreOS, о котором `вы уже
слышали </content/coreos-новый-дистрибутив-на-базе-chromeos>`__, и `уже
перешел eclus <https://github.com/goerlang/eclus/pull/2>`__, заменитель
стандартного `Erlang port mapping
daemon <http://www.erlang.org/doc/man/epmd.html>`__. На очереди еще
несколько системных демонов.

