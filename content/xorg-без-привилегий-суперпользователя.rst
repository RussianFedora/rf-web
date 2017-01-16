.. title: X.org без привилегий суперпользователя
.. slug: xorg-без-привилегий-суперпользователя
.. date: 2014-01-16 19:01:54
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Прошли годы, и благодаря systemd, наш коллега, инженер Red Hat, `Hans de
Goede <https://github.com/jwrdegoede>`__, добился работы X без
дополнительных привилегий, и без одновременного доступа к /dev/ttyXX.

Первая серия патчей `уже отправлена им в список
рассылки <http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/39393>`__.

Идея запускать такой сложный кусок системы, как X, не под
суперпользователем (и без suid-бита) `не
нова <https://lwn.net/Articles/341033/>`__. С ней `экспериментировал
Intel в рамках уже давно забытого проекта
moblin <http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/1158>`__,
потом `Canonical попыталась
реализовать <https://wiki.ubuntu.com/X/Rootless>`__, но столкнулась с
рядом проблем, `и отложила
планы <https://blueprints.launchpad.net/ubuntu/+spec/desktop-maverick-rootless-x>`__.

Участники Fedora немного чувствуют вину за неудачу Canonical, т.к. мы
дали им неверные подсказки, например `использовать
ConsoleKit <http://lists.x.org/archives/xorg-devel/2010-June/010513.html>`__,
в то время, как вкладывались в systemd, переводя ConsoleKit в разряд
неподдерживаемого ПО. Тем не менее, даже без ConsoleKit, оставались бы
нерешенными проблемы, связанные с отсутствием системного вызова revoke,
доступного, например, `в
OpenBSD <http://nixdoc.net/man-pages/OpenBSD/revoke.2.html>`__.

Разумеется, в частных случаях отдельные энтузиасты добивались работы X
на самосборных системах, когда не требовалось обеспечивать безопасность
единственного пользователя (см. `"админ
локалхоста" <https://lurkmore.to/127.0.0.1>`__).

И вот, наконец-то, благодаря systemd, и высокой интеграции его
компонентов, мы можем в общем случае запускать X не от
суперпользователя. Одна из внезапно возникших проблем, это логи X.org,
которые он ведет самостоятельно, не используя даже syslog. `Недавно
пришедший к нам </content/Короткие-новости-19>`__ Tom Gundersen
предлагает использовать syslog или Journald для ведения логов. В
`обсуждении <https://plus.google.com/+DavidHerrmann/posts/ggK1tStCvJH>`__
в ленте Google+ участника ArchLinux, `David
Herrmann <http://dvdhrm.wordpress.com/about-me/>`__, инженер Linaro,
Koen Kooi, предлагает использовать Journal, т.к. это сильно упростит
жизнь embedded-разработчиков, которые переходят на systemd, а `Aaron
Seigo <https://www.ohloh.net/accounts/aseigo>`__ высказывается за
общесистемное решение, т.е. за syslog или Journald.

