.. title: systemd и Wayland
.. slug: systemd-и-wayland
.. date: 2012-04-05 10:15:53
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Keith Packard <https://en.wikipedia.org/wiki/Keith_Packard>`__,
известный разработчик X.org, фактически один из создателей X Window
System, выступая на **2012 Linux Foundation Collaboration** с докладом
по состоянию совместимости X11 и
`Wayland <http://wayland.freedesktop.org/>`__ среди прочего объявил, что
`планируется <https://www.phoronix.com/scan.php?page=news_item&px=MTA4MzA>`__
использовать systemd для запуска Weston, дополнения для протокола X11.

Прямо сейчас есть одно препятствие - systemd не может самостоятельно
запустить X.org (он запускает xdm.service или prefdm.service), и *пока*
они используют небольшой и грязный хак.

Также он сообщил, что X.org, запущенный под Wayland работает
**быстрее**, чем X.org, запущенный прямо на железе. А в ответ на вопрос,
будет-ли Wayland работать с аудио (старая идея о X Audio Server), он
официально рекомендовал PulseAudio.


