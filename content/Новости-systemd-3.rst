.. title: Новости systemd
.. slug: Новости-systemd-3
.. date: 2015-09-24 12:19:23
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Сформирована
программа <https://systemd.events/systemdconf-2015/schedule>`__ первого
systemd.conf 2015. Подтянулись и спонсоры, так что будет интересно.

Интересно, что еще продолжают биться об стену создатели альтернативных
init-систем. Совсем недавно появилась еще пара -
`beginning <https://github.com/Somasis/beginning>`__ и
`govisor <https://github.com/gdamore/govisor>`__ (про него даже
`написали на
OpenNET.ru <http://www.opennet.ru/opennews/art.shtml?num=43001>`__).

Одно время программисты писали десятки если не сотни window-менеджеров,
потом медиаплейеры, а вот теперь стали писать init-системы. Ну что
сказать, уровень растет!
С ростом интереса к базовым компонентам, появился спрос на исторические
материалы. Мы неоднократно говорили, что SysVinit был признан устаревшим
10-15 лет назад, вот, например, обратите внимание на `инициативу
GNOME-разработчика Seth Nickell <http://www.osnews.com/story/4711>`__
(опять эти гномеры!). В этой связи интересно посмотреть на `хронологию
событий <http://blog.darknedgy.net/technology/2015/09/05/0/>`__,
приведших к появлению нынешнего лидера.

Вышедший не так давно `systemd
226 <http://lists.freedesktop.org/archives/systemd-devel/2015-September/034177.html>`__
(`новость на
OpenNET.ru <http://www.opennet.ru/opennews/art.shtml?num=42936>`__)
интересен тем, что он не очень интересен. Кроме изменений в
systemd-networkd там унифицирована работа демона D-Bus и современного
kdbus. Требуется самый последний dbus 1.10, которого нет даже в Fedora
22, и мы видим четкий эволюционный путь - через работу с dbus 1.10 к
kdbus в следующем релизе (получается, что уже 24).

К самому D-Bus стали присматриваться пристальнее. Как раз, когда решили
менять - вот вовремя то! Ну, конечно, лучше поздно, чем никогда. Так или
иначе, народ уже увидел, что `в dbus содержится пересекающаяся
функциональность с
init-системой <http://homepage.ntlworld.com/jonathan.deboynepollard/Softwares/nosh/avoid-dbus-bus-activation.html>`__,
и это плохо. Где же вы раньше были?
К сожалению, `вновь появившиеся тесты производительности dbus vs. sd-bus
vs. kdbus +
sd-bus <http://blog.asleson.org/index.php/2015/09/01/d-bus-signaling-performance/>`__
противоречат `результатам синтетических тестов чистого kdbus
полуторагодичной давности </content/Первые-бенчмарки-kdbus>`__.

Впечатление такое, что Poettering и его команда что-то такое в sd-bus
наворотили, и там теперь серьезный затык. Пока переходить на kdbus
пожалуй не стоит. Будем надеяться, что это, все-таки, проблема в sd-bus,
и инженеры Google не столкнутся с такими проблемами, прежде чем `начнут
перевод Android на
kdbus <https://linuxplumbersconf.org/2015/ocw//system/presentations/3417/original/integrating-kdbus-in-android.pdf>`__.

И из других новостей - `вышел PulseAudio
7.0 <http://www.freedesktop.org/wiki/Software/PulseAudio/Notes/7.0/>`__.

Теперь с socket activation по TCP!
