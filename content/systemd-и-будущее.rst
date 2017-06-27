.. title: systemd и будущее
.. slug: systemd-и-будущее
.. date: 2014-07-14 10:06:13
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Почти с самого появления было понятно, что systemd претендует не на
связку monit+sysv, но на гораздо большее. С `анонсом systemd
215 <https://thread.gmane.org/gmane.comp.sysutils.systemd.devel/20783>`__
(обсуждение `на
OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=40132>`__) это
было объявлено официально, в виде `доклада на FUDCON +
GNOME.Asia <http://0pointer.de/blog/projects/fudcon-gnomeasia.html>`__
(`слайды <http://0pointer.de/public/gnomeasia2014.pdf>`__ и `обсуждение
на OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=40148>`__).

Теперь это официальная Linux-платформа, конструктор для создания
Linux-системы. Логи, сеть, контейнеры, оборудование, пользователи - все
поглощается systemd.

Конечно, есть недовольные, особенно учитывая, что при реализации планов
не удалось обеспечить кое-что из запланированного. Например, `так и не
удалось сохранить полную работоспособность udev без
systemd <https://www.phoronix.com/scan.php?page=news_item&px=MTczNjI>`__,
но чего поделать?
|image0|
Интересно, что udev не получится использовать без systemd из-за перехода
на `kdbus </content/Перенос-d-bus-в-ядро-linux>`__. Отказываться от него
в апстриме systemd (или даже просто делать необязательным) не желают,
т.к. плюсы от него перевешивают минусы (трех недовольных гентушников).

Уже сейчас видно, что `производительность kdbus существенно выше
предыдущего решения </content/Первые-бенчмарки-kdbus>`__, да и другие
проекты тоже рассматривают использование kdbus. Например, не так давно,
D-Bus (и в частности kdbus)
`рассматривали <https://groups.google.com/forum/#!topic/flow-based-programming/-Zfqukz7jls>`__
в списке рассылки по `flow-based
programming <https://en.wikipedia.org/wiki/Flow-based_programming>`__,
но, конечно, гораздо более интересным был бы перевод
`Binder <http://git.kernel.org/?p=linux/kernel/git/torvalds/linux.git;a=blob;f=drivers/staging/android/binder.c;hb=HEAD>`__
на kdbus.

С самым первым анонсом kdbus, многие заинтересованные лица рассуждали на
тему перевода Binder на kdbus или объединения проектов, очень по разному
оценивая шансы на материализацию таких планов. Например, известный
гентушник и дистрохоппер Greg KH полагает, что это `маловероятное
событие </content/Различия-между-kdbus-и-binder>`__, а вот другие
разработчики ядра считают иначе. `John
Stultz <https://plus.google.com/111524780435806926688/about>`__, инженер
Linaro и бывший инженер IBM, который `уже
высказывался </content/Выложили-видеозаписи-с-linux-plumbers-conference-2013>`__
на Linux Plumbers Conference 2013 по поводу объединения kdbus и Binder,
в своей ленте Google+
`повторил <https://plus.google.com/111524780435806926688/posts/8fTvZG9kYWc>`__,
что с его точки зрения плюсы в слиянии обеих проектов перевешивают
минусы, и обратил наше внимание на работу своего коллеги, `Takahiro
Akashi <https://plus.google.com/113992592841977909554/about>`__ -
`**"Benchmarking
IPCs"** <https://docs.google.com/document/d/1Kxut7BCySxFYQ_bJUgV-ezijkLapENcWploaNnl8CVQ/pub>`__,
в которой измеряется скорость работы обеих систем. Выяснилось, что с
умолчальными параметрами kdbus в четыре раза медленнее, чем Binder (139
микросекунд против 35), но с помощью нескольких изменений в коде kdbus
удалось уменьшить задержку до 48, что, учитывая большую функциональность
kdbus, вполне терпимо.

Greg KH в комментариях в ленте Google+ у Takahiro Akashi `уже высказал
свой
скептицизм <https://plus.google.com/113992592841977909554/posts/g7Nbmwb2DVz>`__.

С его точки зрения, числа тут много не решают. Он полагает, что
архитектурное различие между двумя IPC устранить будет непросто (и
возможно не стоит того). А для нас особенно интересным оказалось то, что
мы увидели success story использования
`ftrace <https://www.kernel.org/doc/Documentation/trace/ftrace.txt>`__.

К сожалению, в ядрах, доступных в Fedora, kdbus отключен (мы не включаем
out-of-tree патчи), но `с недавних пор появился сторонний
полуофициальный репозиторий с ядрами, в которых включены тестовые
фичи <http://fedoramagazine.org/try-out-experimental-linux-kernel-features-with-the-kernel-playground/>`__,
и среди прочего там доступен kdbus (новость уже `обсуждается на
OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=40172>`__).


.. |image0| image:: http://samlib.ru/img/z/zelbai/treshiugar/shitopodelatx1.jpg
   :width: 30.0%
