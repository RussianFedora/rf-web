.. title: Новости systemd за прошедшие полтора месяца.
.. slug: Новости-systemd-за-прошедшие-полтора-месяца
.. date: 2013-06-24 11:11:26
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Из-за радиомолчания мы пропустили ряд новостей об этой системе
инициализации (уже нет - см. чуть ниже), но еще не поздно упомянуть о
них.

В конце мая наш агент под прикрытием, гентушник Michał Górny, объявил о
`переводе systemd в ряд стабильных систем загрузки в
gentoo <https://bugs.gentoo.org/show_bug.cgi?id=465870>`__.

Русскоязычные анонимные аналитики в этот раз воздержались от привычного
"закопать", "скинемся на киллера", зато высказали предположение, что
`пора переходить на
Debian <https://www.linux.org.ru/forum/talks/9198145#comment-9199627>`__.

У нас для этих ретроградов плохие новости - в Debian `уже более года
обсуждают </content/altlinux-постепенно-переходит-на-systemd>`__, на что
переходить с SysVinit - на Upstart или на systemd. Для Debian жизненно
необходимо дружить с единственно успешным проектом на своей пакетной
базе, Ubuntu, где используется Upstart, поэтому все-еще есть интрига.

Однако в последнее время разработчики Upstart лишь копипастят куски
systemd (причем даже то, что раньше критиковали), тем самым расписываясь
во вторичности своего проекта, поэтому неудивительно, что `участники
Debian заинтересовались оригиналом, и стрелка качнулась в правильную
сторону <http://www.opennet.ru/opennews/art.shtml?num=37032>`__. Сейчас
Michael Stapelberg пытается разуверить скептиков, серией постов, в
которых он разоблачает мифы о systemd. `Пока доступен лишь первый
пост <http://people.debian.org/~stapelberg//2013/06/09/systemd-bloat.html>`__,
но, судя по всему `русскоязычных экспертов он разубедить не
сумел <http://www.linux.org.ru/forum/talks/9246549>`__. К счастью
русскоязычные противники systemd практически не пишут код и не участвуют
в жизни своих коммьюнити (порой доходит до совершенно удивительного -
новости о своих дистрибутивах они узнают от нас), поэтому к их мнению не
прислушиваются.

Вслед за `примером того, как приложение на Node.js может работать с
systemd </content/nodejs-и-systemd>`__ появился пример того, как
`приложение на Go может использовать socket activation, фирменную фичу
systemd <https://plus.google.com/107956312959748542910/posts/FssTwA3Vqz2>`__.

Напомним, что `Golang с недавних пор доступен в
Fedora </content/Референсная-реализация-языка-go-доступна-в-fedora>`__,
и, например, у `Fedora Erlang
SIG <http://fedoraproject.org/wiki/Erlang>`__ есть планы на Fedora 20,
включающие systemd и Go.

`Год назад мы говорили </content/systemd-и-wayland>`__, что `Keith
Packard <http://en.wikipedia.org/wiki/Keith_Packard>`__ сообщил, что
планируется использовать systemd в Wayland. Эти планы начали
материализовываться - инженер Intel, `Ander Conselvan de
Oliveira <http://www.ohloh.net/accounts/anderco>`__, включил
`первоначальную поддержку механизма уведомлений systemd в
Weston <http://www.phoronix.com/scan.php?page=news_item&px=MTM4Mzc>`__.

Интересно, будет-ли в Mir привязка к Upstart?
Вовсю идет работа над `kdbus <https://github.com/gregkh/kdbus>`__,
реализацией D-Bus, но в ядре (`вы уже могли о ней
слышать </content/Перенос-d-bus-в-ядро-linux>`__). На прошедшем
`Automotive Linux Summit
Spring <http://events.linuxfoundation.org/events/automotive-linux-summit-spring>`__
`Greg Kroah-Hartman <https://www.ohloh.net/accounts/gregkh>`__ рассказал
`о текущем состоянии дел <https://lwn.net/Articles/551969/>`__. Вполне
вероятно, что наличие kdbus будет одним из требований будущего GNOME
(GNOME sandboxes).

|image0|
И наконец последняя и самая ошеломляющая новость. Lennart Poettering и
`Tejun Heo <https://plus.google.com/109921140855127484054/about>`__,
инженер Red Hat и `мэйнтейнер
сgroups <http://lists.linuxfoundation.org/pipermail/containers/2011-November/028409.html>`__,
после нескольких месяцев обсуждений вместе с другими заинтересованными
участниками договорились, что управление cgroups будет производиться с
помощью API, предоставляемого systemd
(`раз <http://thread.gmane.org/gmane.comp.sysutils.systemd.devel/11381>`__
и
`два <http://thread.gmane.org/gmane.comp.sysutils.systemd.devel/11248>`__).

Это означает большие изменения для облачных систем и систем
виртуализации, которые придется переписать на использование systemd. У
маргинальных дистрибутивов есть два варианта - еще немного форкнуть
базовые системы (хотя c udev получилось как-то не очень убедительно),
либо не мучаться, а перейти на systemd. Определенно потребуется
скопипастить еще немного systemd в альтернативные init-системы. К нашему
сожалению, эту инициативу оценили отрицательно наши товарищи по Fedora
Project, такие авторитетные специалисты, как `Jon
Masters <https://plus.google.com/106265217227408958782/posts/QzNYc7PHQ3A>`__
и `Jon
Disnard <https://plus.google.com/104641385617978618363/posts/iYocHWkkiGw>`__.

Мы надеемся, что переубедим их.


.. |image0| image:: https://lwn.net/images/2013/als-gregkh.jpg

