.. title: Сеть в systemd
.. slug: Сеть-в-systemd
.. date: 2014-01-23 10:34:12
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Как вы знаете, `в systemd включают управление
сетью </content/В-systemd-приходит-управление-сетью>`__. Работу ведет
`недавно присоединившийся к Red Hat </content/Короткие-новости-19>`__
участник Arch Linux, `Tom
Gundersen <https://plus.google.com/+TomGundersen/about>`__. Недавно,
`systemd научился создавать
bridge </content/Новости-systemd-за-прошедший-месяц-полтора>`__, а
теперь `Tom научил systemd
bonding <https://cgit.freedesktop.org/systemd/systemd/commit/?id=52433f6>`__.

Если кто пропустил, то Tom написал цикл статей про свою мотивацию,
текущее состояние (на момент написания) и планы по включению сетевых
возможностей в systemd - `постановка
задачи <https://plus.google.com/+TomGundersen/posts/bDQCP5ZyQ3h>`__,
`роль udev <https://plus.google.com/+TomGundersen/posts/anS8GseSAfw>`__,
`libsystemd-rtnl <https://plus.google.com/+TomGundersen/posts/JhaBNn8Ytwu>`__,
`текущее состояние networkd (на момент
написания) <https://plus.google.com/+TomGundersen/posts/8d1tzMJWppJ>`__,
`будущее <https://plus.google.com/+TomGundersen/posts/U6Es8bpmMbP>`__.

