.. title: Текущее состояние работ по удалению виртуальных терминалов из ядра (CONFIG_VT=n)
.. slug: Текущее-состояние-работ-по-удалению-виртуальных-терминалов-из-ядра-configvtn
.. date: 2013-02-09 17:08:02
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Как вы уже могли слышать `уже почти полтора года идет работа по удалению
из ядра
Linux </content/Идет-работа-по-удалению-виртуальных-терминалов-из-ядра-configvtn>`__
виртуальных терминалов в пользу аналогичного решения, работающего в
userspace и использующего KMS, udev, systemd, Mesa и gtk2/pango.

Недавно, на прошедшем FOSDEM 2013, участник Arch Linux, `David
Herrmann <https://plus.google.com/112212087950959620804/about>`__,
подвел итоги проделанной работы и озвучил дальнейшие планы. Вы можете
посмотреть `видео от
PHORONIX <https://www.phoronix.com/scan.php?page=news_item&px=MTI5Njc>`__
и `ознакомиться со
слайдами <https://fosdem.org/2013/schedule/event/kmscon/attachments/slides/248/export/events/attachments/kmscon/slides/248/FOSDEM2013_linux_console.pdf>`__.

Стыдно признаться, но в Arch kmscon уже доступен в репозитории, а вот в
Fedora его пока приходится собирать из исходников.

Кстати, о прошедшем FOSDEM - видеозаписи выступлений потихоньку начали
`выкладывать <http://video.fosdem.org/2013/>`__. Например, доступна
запись с выступлением Lennart Poettering, `systemd, 2 года
спустя <http://video.fosdem.org/2013/maintracks/Janson/systemd,_Two_Years_Later.webm>`__,
и Vincent Untz, `не сошли-ли с ума разработчики
GNOME? <http://video.fosdem.org/2013/maintracks/Janson/Has_the_GNOME_community_gone_crazy_.webm>`__
