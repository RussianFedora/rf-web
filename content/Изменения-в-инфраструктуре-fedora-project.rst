.. title: Изменения в инфраструктуре Fedora Project.
.. slug: Изменения-в-инфраструктуре-fedora-project
.. date: 2012-08-22 14:48:09
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Прямо сейчас происходят серьезные изменения в инфраструктуре Fedora
Project. Во-1 `Kevin
Frenzi <https://plus.google.com/116710523470818417285/about>`__ объявил,
что `fedorahosted.org <https://fedorahosted.org/web/>`__ `с одной машины
переехала на две, с общей файловой системой в
GlusterFS, <https://plus.google.com/u/0/116710523470818417285/posts/fe1sKecVgHP>`__
- больше не будет даунтаймов при апгрейдах (вернее их будет гораздо
меньше). Во-2 почти закончилась работа по переводу инфраструктуры Fedora
Project с `QPid <http://qpid.apache.org/>`__, реализации AMQP от Apache
Software Foundation, на `ØMQ (ZeroMQ) <http://www.zeromq.org/>`__.

Апгрейд
`предложил <https://github.com/ralphbean/fedmsg/blob/develop/doc/proposal.rst>`__
`Ralph Bean <https://www.ohloh.net/accounts/ralphbean>`__, который и
провел основную работу (см. "критикуя - предлагай"). Конечно, не очень
корректно сравнивать ZeroMQ и какую-то конкретно AMQP-реализацию, но
результатом перехода стало ускорение работы узла
`Moksha <https://fedorahosted.org/moksha/>`__, вокруг которого и
построена вся инфраструктура, до ста раз.

Теперь GNOME3, wayland, pulseaudio, NetworkManager, selinux и systemd
будут собираться и доставляться пользователям Fedora в сто раз быстрее!
