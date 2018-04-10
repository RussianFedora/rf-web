.. title: Когда в Fedora будет Firefox с поддержкой gstreamer
.. slug: Когда-в-fedora-будет-firefox-с-поддержкой-gstreamer
.. date: 2013-04-05 16:35:59
.. tags: firefox, gstreamer, html5, патенты
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Несмотря на то, что Firefox начиная с 14й версии умеет использовать
gstreamer для проигрывания кодеков, находящихся в патентном рабстве у
`MPEG LA <http://www.mpegla.com/>`__, пользователи Fedora для просмотра
котиков на ютубе вынуждены ставить вечно глючный и кривой flash-плейер
от Adobe (который показывает котиков и рекламу), или ставить один из
двух вечно глючных и кривых flash-плейеров от opensource-разработчиков
(которые не показывают ни котиков, ни рекламу, зато они открытые и
свободные). К сожалению, эта ситуация сложилась не по прихоти
мэйнтейнеров, а `исходя из вполне рациональных
соображений <https://bugzilla.redhat.com/843583>`__ - сначала реализация
была с ошибками, затем неполная, затем оказалось, что надо портировать
на новый gstreamer1.

Бэкграунд этой печальной истории можно попытаться проследить по
`5-летнему багу в
багзилле MoFo в 300+ комментариев - "GStreamer backend for HTML5 video
element" <https://bugzilla.mozilla.org/422540>`_, и в тикете `#794282 - "Enable
GStreamer in official
builds" <https://bugzilla.mozilla.org/794282>`_. Сейчас в Fedora
ситуация такова - мы ждем окончания портирования на gstreamer1
(`#806917 - "support GStreamer
1.0" <https://bugzilla.mozilla.org/806917>`_), т.к. gstreamer-0.10
признан устаревшим.
