.. title: Новости systemd
.. slug: Новости-systemd
.. date: 2014-11-21 14:09:36
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Lennart Poettering выложил слайды со своего выступления на NLUUG
Najaarsconferentie 2014, где он рассказывал о `фичах безопасности в
systemd <http://0pointer.net/public/systemd-nluug-2014.pdf>`__.

Видеозапись выступления никто не сделал.

К сожалению, в RHEL 7 и пересборки включен относительно старый systemd
версии 208. В нем нет ни пользовательских сессий, ни управления сетью, и
много чего еще. Для тех, кто хочет воспользоваться всем этим, наш
коллега `Lukáš Nykrýn <https://www.openhub.net/accounts/lnykryn>`__
подготовил `экспериментальную сборку самого свежего
systemd <https://copr.fedoraproject.org/coprs/lnykryn/systemd/>`__,
прямо из Fedora Rawhide. Конечно, никаких гарантий не предоставляется,
но мы уже пробуем.

Продолжается `процесс включения kdbus в
ядро </content/Наконец-то-начался-процесс-включения-kdbus-в-ядро>`__.

Greg KH представил `второй вариант
патчсета <https://lkml.org/lkml/2014/11/21/3>`__. Из заметного, помимо
попытки исправить `недостатки, замеченные
ранее </content/Процесс-включения-kdbus-в-ядро>`__, отметим появление
специализированной файловой системы kdbusfs, которая будет монтироваться
в /sys/fs/kdbus.

Наш коллега, `Miroslav
Lichvar <https://www.openhub.net/accounts/lichvarm>`__, работает над
интересным проектом -
`timedatex <https://github.com/mlichvar/timedatex>`__. Это сервис
управления системными часами, управляемый через D-Bus, и, что самое
интересное, являющийся аналогом
`systemd-timedated <http://www.freedesktop.org/wiki/Software/systemd/timedated/>`__,
но не требующий никаких библиотек systemd.

Flannel (ранее Rudder), `еще один вариант управления
сетью </content/Короткие-новости-30>`__, использующий etcd и systemd
(systemd-notify для надежного управления сервисом), наконец-то `включают
в Fedora <https://bugzilla.redhat.com/1165688>`__. Похоже, что SDN, это
уже не будущая, а нынешняя горячая тема.

