.. title: ABRT в Fedora 26
.. slug: abrt-v-fedora-26
.. date: 2017-03-13 15:13:27 UTC+03:00
.. tags: abrt, systemd
.. category: Fedora Changes
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

В Fedora 26 будет `включен сервис systemd-coredump по умолчанию
<https://fedoraproject.org/wiki/Changes/coredumpctl>`_. Теперь обработка дампов
памяти будет осуществляться systemd-coredump.

Все вроде хорошо, но у нас уже есть сервис, который тоже обрабатывает
неизбежные фатальные ошибки в приложениях - `ABRT
<https://github.com/abrt/abrt>`_. Не будет ли пересечения зон ответственности?
`Нет
<https://abrt.github.io/abrt/systemd/core_pattern/2017/03/07/fedora-26-change/>`_,
отвечает нам `Matej Habrnal <https://github.com/mhabrnal>`_, один из
разработчиков. В Fedora 26 ABRT будет извлекать coredump-ы из логов journald, и
для пользователя все будет прозрачно.  Пока будет и возможность вернуться к
прежнему поведению, когда все ошибки будут полностью обрабатываться ABRT, так
что волноваться нечего.
