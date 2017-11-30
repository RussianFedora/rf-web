.. title: Mir доступен в Fedora
.. slug: mir-dostupen-v-fedora
.. date: 2017-11-29 16:51:03 UTC+03:00
.. tags: mir, wayland, bosch, greenfield, gtk, html5
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

`В Fedora официально включили Mir <https://community.ubuntu.com/t/mir-available-on-fedora/2331>`_.

Напомним, в нашем коммьюнити нет диктата какой-либо коммерческой организации,
как, например, в известном коммьюнити вокруг дистрибутива U*****, в котором все
вопросы решает главарь компании C********. Если пользователь решит включить
открытое ПО в Fedora, и оно не нарушает законы США, то помешать ему не
получится. Более того, наше сообщество будет осуждать любые попытки помешать.
Если кому-то захочется добавить в Fedora форк GNOME 2, то это получится. Так и
тут - участник коммьюнити так решил, поэтому Mir будет доступен в репозиториях
Fedora.

Многие наши участники, конечно, сомневаются в практической ценности включения
Mir в Fedora, но это их личное мнение. Не нравится - не ставь.

Тем не менее, похоже, что это - лебединая песня Mir. Wayland же в это время
набегает, захватывает и заполоняет.

`Bosch разработал 3D window-менеджер на базе Wayland
<https://lists.freedesktop.org/archives/wayland-devel/2017-November/035849.html>`_.
Планируют применять в IVI-устройствах, куда, кстати, планировали нацелить и
Mir.

`Для Wayland разработали HTML5-композитор под названием Greenfield
<https://github.com/udevbe/greenfield>`_. Теперь можно запускать рабочий стол в
Firefox.

А вот Firefox можно будет запустить в другом Firefox. Как только окончательно
доработают Broadway, HTML5-бэкенд для GTK. Наш коллега, `Alexander Larrson
<https://www.openhub.net/accounts/alexl>`_, в последний месяц начал работу по
обновлению этого экспериментального бэкенда для планирующейся версии GTK 4. За
месяц им сделано `очень многое <https://git.gnome.org/browse/gtk+/log/?qt=grep&q=broadway>`_, например:

* `Новый рендерер для Broadway (пока используется Cairo) <https://git.gnome.org/browse/gtk+/commit/?id=23845a57a940fb7f7077b25059394dc9d4aa03c6>`_
* `Поддержка передачи файловых дескрипторов в протоколе <https://git.gnome.org/browse/gtk+/commit/?id=f31d7e1f9114d9d39229d827d564e54120598013>`_
* `Загрузка текстур <https://git.gnome.org/browse/gtk+/commit/?id=48d587d255439f9a2ed0697d5caad0f4d8710961>`_
* `Использование render nodes <https://git.gnome.org/browse/gtk+/commit/?id=f7d8ee041bdd77e94f7ea1f801b5f719f50588fc>`_

Скоро можно будет запустить Firefox под Wayland с помощью Mir в LibreOffice под X.org.
