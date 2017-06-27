.. title: Erlang и systemd
.. slug: erlang-и-systemd
.. date: 2014-07-13 17:50:18
.. tags: erlang, systemd, redhat, rabbitmq, openstack, couchdb
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Мы продолжаем работу по systemd-изации Erlang в рамках `проекта по
улучшению состояния с этим языком в Fedora
21 <https://fedoraproject.org/wiki/Changes/BetterErlangSupport>`__. На
текущий момент мы уже `включили поддержку socket activation в
epmd <https://src.fedoraproject.org/cgit/erlang.git/commit/?id=f7eb6dd>`__,
которую `добавил Matwey V.
Kornilov </content/erlang-продолжает-получать-поддержку-systemd>`__, а
также `добавили поддержку system
notification <https://src.fedoraproject.org/cgit/erlang.git/commit/?id=0585732>`__,
что повышает надежность старта приложений, требующих запущенного epmd.

Благодаря новой библиотеке `erlang-sd\_notify
<https://github.com/lemenkov/erlang-sd_notify>`__, для поддержки system
notification, инженеру Red Hat, `John Eckersberg
<https://github.com/jeckersb>`__, удалось `изменить типа systemd-сервиса для
RabbitMQ на Notify
<https://src.fedoraproject.org/cgit/rabbitmq-server.git/commit/?id=eea61e0>`__
(пользователи Red Hat OpenStack 5.0 `смогут воспользоваться результатами нашей
работы <https://rhn.redhat.com/errata/RHEA-2014-0845.html>`__), что резко
повысит надежность запуска RabbitMQ в облаках. До сих пор `SysV init-скрипт
RabbitMQ содержал большое количество хаков
<https://bugzilla.redhat.com/show_bug.cgi?id=1112770#c0>`__, и все равно `часто
ничего не работало <https://bugzilla.redhat.com/show_bug.cgi?id=1104193#c2>`__.
Такова ненадежность и хрупкость портянок на Bash, из которых состоят
SysV-скрипты. И это, между прочим, ПО уровня Enterprise, на котором работают
миллионные и миллиардные сервисы, так что понятно, что творится в других
случаях.

Помимо этого, разработчик Litecoin и Bitcoin, основатель Fedora
Community, `Warren Togami <https://github.com/wtogami>`__, взялся за
CouchDB. Он использует его в своем бизнесе, и также был заинтересован,
чтоб он работал с большей степенью использования API systemd. `CouchDB
теперь тоже использует
systemd <https://src.fedoraproject.org/cgit/couchdb.git/commit/?id=e63180e>`__,
и мы, как обычно, `предложили наши изменения в upstream, на
включение <https://github.com/apache/couchdb/pull/258>`__. Так,
потихоньку, поддержка systemd будет реализована везде.

К сожалению, в Fedora пока еще недоступна поддержка Journald в Erlang,
которую `более полугода назад разработали в
Travelping </content/erlang-получает-поддержку-systemd>`__, но мы
работаем над этим. Также неисправленными остались `политики SELinux для
Erlang-приложений <http://wtogami.blogspot.com/2014/07/selinux-problems-with-erlang-on.html>`__
- Warren Togami вместе с Dan Walsh `работает над этой
задачей <https://bugzilla.redhat.com/show_bug.cgi?id=1116014>`__.

И напоследок забавная и одновременно печальная новость. К сожалению мы с
нашими systemd-изменениями попали в не очень удачное время для CouchDB.

И дело не только в двух огромных изменениях, падающих в git-репозиторий
CouchDB прямо сейчас - `переход с тестового фреймворка etap на тестовый
фреймворк eunit <https://github.com/apache/couchdb/pull/253>`__ и
`слияние с проектом
BigCouch <https://thread.gmane.org/gmane.comp.db.couchdb.devel/34218>`__,
а в двух огромных бомбах политкорректности.

Во-1 по коммьюнити ударило `[STRIKEOUT:DDoS-ом] обсуждением замены
master/slave терминологии на
нерасистскую <https://issues.apache.org/jira/browse/COUCHDB-2248>`__.

Это популярная сейчас тема - если заменить устоявшиеся выражения на
политкорректные, то получишь +10 к твоей харизме в геймифицированном
реаллайфе. Больше никаких плюсов не будет, лишь бессмысленное отвлечение
сил разработчиков на обсуждение политкорректного
`новояза <https://ru.wikipedia.org/wiki/Новояз>`__. И во-2, выяснилось,
что `в примерах используются образы из рекламной кампании Барака Обамы
или его
противника <https://thread.gmane.org/gmane.comp.db.couchdb.devel/34252>`__.

Нам трудно сказать чьим
`маскотом <https://ru.wikipedia.org/wiki/Персонаж-талисман>`__ был Joe
The Plumber, т.к. политики в США со стороны выглядят очень похожими -
войны ведут, как республиканцы, так и демократы, так что мы не очень
разбираемся, кто там и за кого в этом
`луна-парке <https://lurkmore.to/Блэкджек_и_шлюхи>`__.

К чести коммьюнити, оба обсуждения истратили не столько уж и много
энергии участников, и [STRIKEOUT:`заняв место в пятницу, чтоб в субботу
пораньше освободиться <http://www.ostrie.net/id/11078>`__] исправив и
закончив оба обсуждения быстрее, чем в аналогичных случаях делали в
других коммьюнити, разработчики продолжили программирование.
