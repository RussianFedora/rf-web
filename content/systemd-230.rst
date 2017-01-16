.. title: systemd 230!
.. slug: systemd-230
.. date: 2016-05-22 21:40:51
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Вышел systemd
230 <http://thread.gmane.org/gmane.comp.sysutils.systemd.devel/36521>`__.

Фич довольно много, например systemctl revert, которая удаляет
пользовательские изменения к указанному systemd-юниту (напомним, трогать
юниты в /usr/lib/systemd не надо, а надо добавлять изменения в
/etc/systemd/), но среди них есть особенно интересная - `поддержка
Ambient
Capabilities <https://www.freedesktop.org/software/systemd/man/systemd.exec.html#AmbientCapabilities>`__,
про которые `мы вам уже
рассказывали </content/linux-capabilities-и-tame-из-openbsd>`__. Теперь
можно будет легко передавать необходимые привилегии процессу,
запускаемому не от суперпользователя.

`Новость уже обсуждается коллегами-аналитиками на
OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=44474>`__.

