.. title: Discoverable partitions в systemd
.. slug: discoverable-partitions-в-systemd
.. date: 2014-03-07 23:53:33
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Lennart Poettering и его команда `включили в systemd поддержку
разработанного ими же расширения спецификации
GPT <http://thread.gmane.org/gmane.comp.sysutils.systemd.devel/17524>`__,
`стандартизирующего уникальные GUID для характерных разделов
Linux <http://www.freedesktop.org/wiki/Specifications/DiscoverablePartitionsSpec/>`__.

Идея в том, чтоб systemd распознавал GUID для таких разделов, как /,
/home, /srv, swap и некоторых других, и монтировал их автоматически, без
использования /etc/fstab. Использование fstab уже давно не требуется в
системах с systemd, хотя порой прикладное ПО очень удивляется, если
этого файла не существует, или он нулевого размера (мы периодически
`отсылаем
патчи <https://git.fedorahosted.org/cgit/grubby.git/commit/?id=8ced05a>`__,
когда обнаруживаем такие случаи). У нас уже работают системы, в которых
/etc/fstab пуст (хотя еще и существует), так что это действительно
работает. Пока /etc/fstab все еще обрабатывается, но рекомендуется
постепенно переходить на `systemd-юниты для
разделов <http://www.freedesktop.org/software/systemd/man/systemd.mount.html>`__,
если случай сложен, или на GPT, если простой.

