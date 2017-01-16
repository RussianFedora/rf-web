.. title: В X.org включают поддержку systemd!
.. slug: В-xorg-включают-поддержку-systemd
.. date: 2014-01-27 20:31:33
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Наш коллега, инженер Red Hat, `Hans de
Goede <https://github.com/jwrdegoede>`__, продолжил работу по
`интеграции systemd и
X.org </content/xorg-без-привилегий-суперпользователя>`__. Он приступил
к более решительным шагам и предложил `патчи для включения в X.org
socket activation и дальнейшей интеграции с
systemd-logind <http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/39533>`__.

Конечно пока это будет compile-time switch, и никто не требует срочно
отказываться от поддержки устаревших Unix-систем в X.org.

