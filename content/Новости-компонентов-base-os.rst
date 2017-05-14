.. title: Новости компонентов Base OS
.. slug: Новости-компонентов-base-os
.. date: 2014-02-18 18:23:09
.. tags: grep, redhat, glibc, util-linux, systemd
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Участник Fedora и нынешний мэйнтейнер grep `Jim
Meyering <https://www.openhub.net/accounts/meyering>`__ анонсировал выход
`grep 2.17 <https://savannah.gnu.org/forum/forum.php?forum_id=7885>`__.
В версии значительно ускорена работа grep с multibyte кодировками в паре
случаев.

Инженер Red Hat, `Carlos
O'Donell <https://plus.google.com/116746191356411907058>`__,
объявил о выходе `GNU C Library версии
2.19 <https://savannah.gnu.org/forum/forum.php?forum_id=7882>`__.
Внимательные коллеги-аналитики сумели обсудить `новость на OpenNET.ru за
неделю до официального анонса на
GNU.org <https://www.opennet.ru/opennews/art.shtml?num=39043>`__, в
момент появления анонса в списке рассылки. Непонятно, почему Carlos
затянул еще на неделю с анонсом на GNU.org, но главное, что наконец-то
это было сделано.

После выхода очередного обновления `util-linux версии
2.24.1 <https://www.kernel.org/pub/linux/utils/util-linux/v2.24/v2.24.1-ReleaseNotes>`__
его мэйнтейнер и основной разработчик, инженер Red Hat и участник Fedora
`Karel Zak <https://www.openhub.net/accounts/kzak>`__, продолжает
знакомить нас с новыми возможностями утилит из пакета (предыдущие
новости - `раз </content/Короткие-новости-5>`__,
`два </content/Новости-пакета-util-linux-снова>`__,
`три </content/Новости-пакета-util-linux>`__). В этот раз он рассказал
об интересной функциональности утилиты fallocate, которая `получила
возможность преобразовывать обычный файл в
разреженный <https://plus.google.com/111319147897550904359/posts/XZDuSy1Smez>`__
(см. также
`Википедию <https://ru.wikipedia.org/wiki/Разрежённый_файл>`__).

Вообще, util-linux развиваются крайне шустро, и многие матерые
линуксоиды не в курсе о уже имеющейся функциональности. Так известный
гентушник и дистрохоппер Greg Kroah-Hartman в своей ленте Google+ `с
удивлением
узнал <https://plus.google.com/111049168280159033135/posts/RdqDPv6mu64>`__
о существовании ключа *dmesg --human*. В комментариях читатели его ленты
начали делиться другими интересными советами.

И напоследок новость `о грядущем выходе systemd
209 <http://cgit.freedesktop.org/systemd/systemd/tree/NEWS>`__, которую
`уже перевели на
Linux.org.ru <https://www.linux.org.ru/news/opensource/10195930>`__.

Ждем!
