.. title: В util-linux переписали sfdisk
.. slug: В-util-linux-переписали-sfdisk
.. date: 2014-10-17 12:43:35
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Наш коллега, `Karel Zak <https://www.openhub.net/accounts/kzak>`__,
`полностью переписал
sfdisk <http://karelzak.blogspot.ru/2014/10/new-sfdisk.html>`__, утилиту
из состава пакета
`util-linux <https://github.com/karelzak/util-linux>`__. Около года
назад, осенью 2013, он `закончил рефакторинг утилиты
fdisk <http://karelzak.blogspot.com/2013/10/util-linux-v224-fdisk8.html>`__,
выделив из нее общую часть в библиотеку libfdisk. Затем он `переписал
утилиту
cfdisk <http://karelzak.blogspot.ru/2014/06/new-cfdisk-util-linux-v225.html>`__
с использованием этой библиотеки, и теперь пришла очередь переписать
sfdisk с использованием libfdisk.

Вообще, в последнее время Karel активно занимается рефакторингом пакета
- вы уже слышали, что он `выделил часть для форматирования текста в
консоли в общую библиотеку
libsmartcols </content/Унификация-вывода-консольных-команд>`__. Жаль,
что coreutils разрабатывается отдельно. Кстати, вы в курсе, что
существует `проект по переписыванию GNU
Coreutils <https://github.com/uutils/coreutils>`__ на Rust?
