.. title: Загрузка с initrd теперь быстрее, чем без initrd
.. slug: Загрузка-с-initrd-теперь-быстрее-чем-без-initrd
.. date: 2013-04-06 20:12:12
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Не так давно `Lennart
Poettering <https://www.openhub.net/accounts/mezcalero>`__ написал
`руководство по сокращению времени загрузки
системы <http://freedesktop.org/wiki/Software/systemd/Optimizations>`__
(его активно обсуждали, например, `на
OpenNET <https://www.opennet.ru/opennews/art.shtml?num=33840>`__). С
радостью сообщаем вам, что участник Fedora и инженер Red Hat `Harald
Hoyer <https://www.openhub.net/accounts/backslash>`__ и разработчик udev и
systemd `Kay Sievers <https://www.openhub.net/accounts/kaysievers>`__
оптимизировали dracut так, что он теперь создает initrd-образ, с которым
`загрузка происходит быстрее, чем без
него <https://plus.google.com/108087225644395745666/posts/H9CFBQLG8S8>`__.

Теперь совет об отключении initrd можно считать устаревшим.

