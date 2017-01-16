.. title: Тестовый день Fedora 23 - NetworkManager
.. slug: Тестовый-день-fedora-23-networkmanager
.. date: 2015-08-14 09:22:52
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Мы только-только `собираемся устроить Fedora 22 Release
Picnic </content/fedora-22-release-party-в-Москве>`__, а уже начались
тестовые дни для Fedora 23. Одним из первых будет `тестовый день
NetworkManager <https://fedoraproject.org/wiki/Test_Day:2015-08-20_NetworkManager>`__,
запланированный на 20 августа.

Вы уже знаете, что с Fedora 22 мы перешли на `NetworkManager
1.x.x <https://blogs.gnome.org/dcbw/2015/01/19/the-whole-damn-world-takes-effect-to-networkmanager-1-0/>`__.

В версии 1.0.0 он стал тоньше (меньше зависимостей), его DHCP-клиент
стал быстрее (код, взятый из systemd и connman), он стал лучше
сосуществовать с уже сконфигурированными устройствами, статическими
интерфейсами, и предустановленными маршрутами. К счастью, особо крупных
проблем не нашлось. Тем не менее, последовало уже два багфикс-релиза.

Сначала вышел `NetworkManager
1.0.2 <https://blogs.gnome.org/dcbw/2015/05/05/reach-the-top-with-networkmanager-1-0-2/>`__,
в котором среди прочих исправлена ошибка, с которой только что
столкнулись разработчики systemd-networkd - если на устройстве исчезает
питание (выдернули и воткнули кабель, или глюк ядра), то не стоит сразу
же сбрасывать настройки и запускать DHCPклиент по новой). Затем вышел
`NetworkManager
1.0.4 <https://blogs.gnome.org/dcbw/2015/07/16/networkmanager-1-0-4-released/>`__.

Сейчас на подходе уже версия 1.0.6, и вот ее-то и будем проверять.

