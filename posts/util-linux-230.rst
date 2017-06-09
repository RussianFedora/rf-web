.. title: util-linux 2.30
.. slug: util-linux-230
.. date: 2017-06-09 17:08:56 UTC+03:00
.. tags: util-linux
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

`Вышел util-linux 2.30
<https://www.spinics.net/lists/util-linux-ng/msg14048.html>`_, и его мэйнтейнер
и основной разработчик, инженер Red Hat и участник Fedora, `Karel Zak
<https://www.openhub.net/accounts/kzak>`_, поделился `в своем блоге
<https://karelzak.blogspot.com/2017/06/util-linux-v230-whats-new.html>`_ новыми
фичами релиза.

* Утилиту tailf выкинули на мороз.

* Добавили утилиту blkzone, появившуюся в результате взаимодействия
  разработчиков WD, Seagate и SanDisk, и которая предназначается для работы с
  т.н. `зонированными блочными устройствами
  <http://www.storagereview.com/methods_of_smr_data_management>`_.

* Добавили команду fincore, предназначенную для отображения использования
  страниц памяти, содержащих контент указанного файла.

* Постепенно переписывается код утилиты hwclock.

* Утилита column теперь использует библиотеку libsmartcols, о которой `вы уже
  слышали </content/Унификация-вывода-консольных-команд/>`_.

* Добавлены две новые команды - lsmem и chmem. Ранее они поставлялись в составе
  пакета s390-tools, и были написаны на Perl. Их предназначение - вывод
  диапазонов памяти и их статус, и переключение статуса диапазонов памяти
  online/offline (соответственно).

`Коллеги-аналитики уже обсуждают новость на OpenNET.ru
<https://www.opennet.ru/opennews/art.shtml?num=46649>`_.
