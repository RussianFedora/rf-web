.. title: Fedora пересобирает все пакеты с GCC 6
.. slug: fedora-пересобирает-все-пакеты-с-gcc-6
.. date: 2016-02-25 15:41:01
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Снова настало это время. Наши коллеги начали пересборку всех пакетов в
Fedora с помощью нового GCC 6 (`будет
фичей <https://fedoraproject.org/wiki/Changes/GCC6>`__ будущей Fedora
24). Пока результаты обескураживают - вместо ожидавшегося одного
процента поломок, `сломалось почти три процента
пакетов <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/DH7M2ADHM6XCRFTRRSKZD6MWFUJKHBZK/>`__.

В нашем списке рассылки необычно большое количество зашедших в тупик
мэйнтейнеров, которые попытались самостоятельно справиться с ошибками -
навскидку,
`один <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/216934>`__,
`два <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/216905>`__,
`три <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/216862>`__,
`четыре <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/216855>`__,
`пять <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/216842>`__,
`шесть <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/216794>`__.

Прорвемся, конечно.

Как обычно, результаты наших усилий пойдут на пользу и другим
дистрибутивам, которые когда-нибудь тоже перейдут на GCC 6. Кстати, в
этой пересборке всего сломалось чуть меньше 10% пакетов (как и обычно),
но значительная часть поломок не имеет отношения к переходу на GCC 6, а
связана с застарелыми проблемами в ПО, которым никто не пользуется. Эти
пакеты, которые поломались не из-за GCC 6, видимо будут скоро выброшены.

Мы, в отличие от других дистрибутивов, не гонимся за огромными числами
предоставляемых пакетов, среди которых много мусора, которым не только
никто не пользуется, но и который давным давно уже поломан.

