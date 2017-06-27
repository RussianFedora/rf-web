.. title: Поддержка протокола kdbus для Wireshark
.. slug: Поддержка-протокола-kdbus-для-wireshark
.. date: 2014-03-11 23:26:55
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Разработчик Linux, systemd, PulseAudio и ряда других проектов, `Daniel
Mack <https://www.openhub.net/accounts/zonque>`__, в своей ленте Google+
анонсировал `диссектор протокола kdbus для
Wireshark <https://plus.google.com/115882966144514285637/posts/3fdZwYbh2pR>`__
(см. также `"пишем плагин-диссектор для
Wireshark" <https://habrahabr.ru/post/121990/>`__). Пока диссектор еще не
предложен в апстрим для включения, но очень возможно, что вскоре он
будет добавлен. Наша практика показывает, что появление диссектора
протокола в Wireshark резко упрощает дальнейшую разработку ПО,
работающего с этим протоколом, и вот именно поэтому мы, когда
разрабатываем новые протоколы, стараемся
`побыстрее <http://lists.sip-router.org/pipermail/sr-users/2013-November/080414.html>`__
`добавить <http://openser.org/pipermail/devel/2014-February/013672.html>`__
их поддержку в WIreshark. Поэтому мы не сомневаемся, что не станет
исключением и kdbus, хотя прямо сейчас он выглядит не очень готовым к
использованию.

Появление поддержки D-Bus в Wireshark было непростым делом. От `так и не
материализовавшейся
идеи <https://thread.gmane.org/gmane.network.wireshark.devel/19214>`__ до
`ее реализации совершенно другими
людьми <https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5502>`__
прошло почти полтора года. Еще год ушел на добавление `поддержки захвата
сообщений D-Bus в
libpcap <https://sourceforge.net/p/libpcap/feature-requests/18/>`__ (что
интересно, `dbus-dump <https://github.com/mvidner/dbus-dump>`__,
сторонняя утилита для создания таких pcap-файлов была написана
участником коммьюнити openSUSE, Martin Vidner, ранее `2010
года <http://mvidner.blogspot.com/2010/11/dbus-dump.html>`__). Хотелось
бы верить, что с kdbus дела пойдут побыстрее, т.к. `таскать с пару дюжин
out-of-tree патчей и бэкпортить их
туда-сюда <https://src.fedoraproject.org/cgit/wireshark.git/tree/>`__,
это не самое приятное времяпровождение.

