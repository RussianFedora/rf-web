.. title: Короткие новости про основные компоненты системы (Base OS)
.. slug: Короткие-новости-про-основные-компоненты-системы-base-os-0
.. date: 2013-12-22 22:22:37
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Pulseaudio наконец-то `получил поддержку
Journald <http://cgit.freedesktop.org/pulseaudio/pulseaudio/commit/?id=d20ee7e>`__.

Заодно, один из немногих разработчиков Canonical, `Ryan
Lortie <https://launchpad.net/~desrt>`__, `улучшил совместимость
Pulseaudio с
FreeBSD <http://cgit.freedesktop.org/pulseaudio/pulseaudio/commit/?id=1da34e9>`__.

К сожалению, из-за зоопарка "нестандартных стандартов" в мире BSD, мы не
уверены, что это поможет работе на множестве других несовместимых друг с
другом вариантов BSD, но возможно подтолкнет их разработчиков к
конструктивной деятельности, как появление новых проектов по созданию
систем инициализации `подтолкнуло разработчика продолжить работу по
портированию launchd на
FreeBSD <http://www.linux.org.ru/news/bsd/9951942>`__.

`Вышла новая версия
Enlightenment <https://phab.enlightenment.org/phame/live/3/post/enlightenment_dr_0_18_0_release/>`__.

Из новинок - еще большая интеграция с systemd и постепенный переход на
Wayland. Мы уже неоднократно говорили, что `все ведущие DE переходят на
systemd </content/Часть-функциональности-gnome-kde-и-xfce-переносят-в-systemd>`__,
так что постепенный переход Enlightenment нас неособо удивляет.

Kay Sievers в своей ленте Google+ объявил, что достиг еще одного рубежа
- `systemd с kdbus загружается на физическом
железе <https://plus.google.com/+KaySievers/posts/AXJxacCzoz2>`__. Ждем
в Fedora 21!
И в продолжение `недавней новости о
gummiboot </content/Короткие-новости-18>`__, получившем поистине
Enterprise-grade фичу, возможность демонстрации splash-screen во время
секундной загрузки - Kay выложил `видео загрузки Fedora с gummiboot на
Macbook Air <https://plus.google.com/+KaySievers/posts/jh4Bn7iD7Bb>`__.

Если вы не в курсе, то самые популярные среди разработчиков Base OS
Linux платформы, это различные модели Macbook, Lenovo, и Google
Chromebook. Все остальные ноутбуки поддерживаются по остаточному
принципу. Учтите это, когда будете совершать следующую покупку.

И под конец, новость не совсем про Base OS. `Из бизнеса вылетела
Calxeda <http://gigaom.com/2013/12/19/arm-server-pioneer-calxeda-plans-restructuring-after-running-out-of-cash/>`__.

Отношение к новости двойственное. С одной стороны, оказалось, что `их
серверная система на базе 32-битного ARM дико
тормозная </content/Короткие-новости-про-основные-компоненты-системы-base-os>`__.

С другой - первым всегда тяжело, а вторым легче, т.к. они могут не
повторять ошибки ведущих. Конечно, если бы знать задним умом, то надо
было бы сразу прыгать на 64-битный ARM, а не пытаться использовать для
серьезных задач телефонный микропроцессор, но если бы, да кабы.

