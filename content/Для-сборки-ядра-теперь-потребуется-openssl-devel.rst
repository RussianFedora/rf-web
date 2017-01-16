.. title: Для сборки ядра теперь потребуется openssl-devel
.. slug: Для-сборки-ядра-теперь-потребуется-openssl-devel
.. date: 2015-09-09 09:46:06
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Известный хулиган и матершинник, Linus Torvalds,
`одобрил <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=b793c00>`__
включение в ядро
`пары <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=bc1c373>`__
`патчей <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=3f1e1be>`__,
благодаря которым для сборки ядра с цифровыми подписями модулей теперь
потребуется openssl-devel. Т.к. Linus использует Fedora, то он проверял
лишь с openssl-devel, а в Debian и Ubuntu надо использовать libssl-dev
или что-то типа того. Конечно, туда современные ядра добавят с
традиционной задержкой, так что волноваться не о чем.

