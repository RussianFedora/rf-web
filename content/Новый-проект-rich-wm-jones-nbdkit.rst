.. title: Новый проект Rich W.M. Jones - nbdkit
.. slug: Новый-проект-rich-wm-jones-nbdkit
.. date: 2013-06-24 14:57:38
.. tags: nbdkit, nbd
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

`Rich W.M. Jones <http://people.redhat.com/~rjones/>`__ анонсировал
`очередную свою
разработку <https://rwmj.wordpress.com/2013/06/21/new-project-nbdkit-liberally-licensed-nbd-server-with-a-plugin-api/>`__
- `nbdkit <https://github.com/libguestfs/nbdkit>`__, фреймворк для
создания NBD-серверов. Отличительными особенностями являются либеральная
лицензия, хорошая производительность благодаря многопоточности, хорошая
документация, и возможность расширения с помощью плагинов. Он уже
`написал три простейших
расширения <https://rwmj.wordpress.com/2013/06/21/three-plugins-for-nbdkit/>`__.

Основной идеей проекта было расширение возможностей libguestfs, но
перспективы у проекта гораздо больше. С его помощью, например, можно
создать дополнения для VMware с помощью
`VDDK <https://www.vmware.com/support/developer/vddk/>`__, т.к. лицензия
это позволяет.

