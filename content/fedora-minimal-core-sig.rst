.. title: Fedora Minimal Core SIG
.. slug: fedora-minimal-core-sig
.. date: 2012-11-11 13:15:50
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


В Fedora есть возможность установить систему в минимальной конфигурации
(без tar, less, ifconfig, графических программ и библиотек и т.п.).
Внезапно, `Adam Williamson <http://www.happyassassin.net/about/>`__
заметил, что `минимальная конфигурация тянет за собой
пол-иксов <https://bugzilla.redhat.com/show_bug.cgi?id=874378>`__, о чем
сразу же `сообщил в
рассылке <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/170599>`__.

Завязалось обсуждение, по результатам которого было
`объявлено <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/170682>`__
о создании новой группы по интересам - `Fedora Minimal Core
SIG <https://fedoraproject.org/wiki/SIGs/Minimal_Core>`__. Целью группы
будет работа над поддержкой минимального варианта системы в
действительно минимальном виде. В качестве побочной деятельности
участники будут присматривать и за цепочками зависимостей пакетов,
которые `ранее порой пугали
размерами <http://peter.fedorapeople.org/RHEL5.3-ImageMagick-dependencies.txt>`__.

Присоединяйтесь к группе - сделаем Fedora стройнее.

Первым действием участников новосозданной группы стало `предложение по
удалению polkit (бывший PolicyKit) из минимального
набора <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/170759>`__
(что выглядит довольно разумно, особенно учитывая, что polkit теперь
тянет виртуальную машину JS).

