.. title: Улучшения в gettext и другие новости
.. slug: Улучшения-в-gettext-и-другие-новости
.. date: 2016-07-28 18:34:02
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Последние несколько лет мэйнтейнером gettext является наш коллега,
инженер Red Hat и участник Fedora Project, `Daiki
Ueno <https://www.openhub.net/accounts/ueno>`__. За это время в gettext
были внесены важные улучшения, благодаря которым нет никакой нужды
использовать конкурирующее решение - `intltool, разрабатывающееся в
Launchpad с помощью bzr <https://launchpad.net/intltool>`__. Наш
коллега, Matthias Clasen, в своем блоге `постарался рассказать о
преимуществах
gettext <https://blogs.gnome.org/mclasen/2016/07/21/using-modern-gettext/>`__.

Вкратце, это большое количество понимаемых форматов (\*.desktop, файлы
Gtkbuilder, \*.appdata.xml, \*.metainfo.xml), включение и использование
переведенных строк, и удобство подключения новых XML-форматов к gettext.

`Peter Hutterer <https://fedoraproject.org/wiki/User:Whot>`__ объявил,
что `libinput окончательно
завершен <https://who-t.blogspot.com/2016/07/libinput-is-done.html>`__.

У него закончился TODO-список. Эта библиотека будет основным источником
ввода для Wayland, поэтому это очень важно. `Fedora перешла на libinput,
как основной драйвер для X11 начиная с Fedora
22 </content/Первая-пачка-фич-fedora-22>`__ - таким образом будет
достигнут бесшовный переход на Wayland. Недавно, кстати, `выпустили
Wayland Protocols
1.5 <https://lists.freedesktop.org/archives/wayland-devel/2016-July/030211.html>`__
- набор дополнительных протоколов для Wayland, и среди изменений есть
относящиеся к touchpad. Немного опасаемся за будущее Wayland. В XMPP
идея о базовом функционале и дополнительных функциях, реализуемых в виде
необязательных к следованию им XEP, привела к тому, что гарантированно
работали только базовые функции, и от протокола массово начали
отказываться большие вендоры в пользу самописных, более функциональных
решений.

Постепенно `набирает скорость Vulkan </content/Вышел-vulkan-10>`__. Наш
коллега, инженер Red Hat и участник Fedora и Debian, `David
Airlie <https://www.openhub.net/accounts/airlied>`__, предложил `первый
вариант Vulkan-драйвера для некоторых видеокарт
AMD <http://airlied.livejournal.com/81460.html>`__.

Новости о systemd больше не пугают революционностью. Недавно `systemd
дорос до версии
231 <https://lists.freedesktop.org/archives/systemd-devel/2016-July/037220.html>`__.

Основная работа, судя по ChangeLog, идет в направлении контейнеров и
systemd-networkd. Интересно, что и systemd, и wayland стали настолько
хороши, что `GNOME в Fedora 24 теперь использует их практически
незаметно для
пользователя <https://paste.fedoraproject.org/396888/69716934/>`__
(обратите внимание на строку 259, где располагается процесс с PID 2147).

А ведь `нам уже говорили, что systemd --user планировали
переработать </content/Что-там-у-systemd>`__.

