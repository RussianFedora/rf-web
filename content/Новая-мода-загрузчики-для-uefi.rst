.. title: Новая мода - загрузчики для UEFI
.. slug: Новая-мода-загрузчики-для-uefi
.. date: 2012-06-25 12:48:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


После того, как Canonical решил последовать почти по тому же правильному
пути, выбранному Fedora, в вопросе работы с UEFI и функцией SecureBoot,
и его пиар-отдел заявил об этом, они обнаружили, что это нарушает GPL,
под которой распространяется GRUB 2, основной загрузчик системы. Как
обычно, в будущем времени, они объявили, что `напишут специальный
загрузчик для
UEFI <https://lists.ubuntu.com/archives/ubuntu-devel/2012-June/035445.html>`__
взяв за основу `efilinux <https://github.com/mfleming/efilinux>`__ от
Intel.

А вот `наши читатели уже в
курсе </content/Требования-canonical-для-производителей-оборудования-c-uefi>`__,
что участники Fedora `Kay
Sievers <https://www.openhub.net/accounts/kaysievers>`__ и `Harald
Hoyer <https://www.openhub.net/accounts/backslash>`__ уже написали такой
загрузчик, который только собирается дописывать неизвестно кто в
Canonical. Kay и Harald назвали загрузчик
`gummyboot <https://cgit.freedesktop.org/~kay/gummiboot>`__, и он уже
быстро потолстел с первоначальных 600 строк кода до тысячи. Из последних
новостей Kay сообщает в своей ленте Google+, что `загрузчик научился
запоминать опцию загрузки по
умолчанию <https://plus.google.com/108087225644395745666/posts/ZqnNzgn4wdN>`__,
задаваемую пользователем в меню загрузчика. GRUB2 так не умеет, значит
gummyboot "готов к десктопу"!
