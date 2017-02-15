.. title: Планируется полная пересборка всех Ocaml-пакетов для Fedora 18
.. slug: Планируется-полная-пересборка-всех-ocaml-пакетов-для-fedora-18
.. date: 2012-12-14 13:02:44
.. tags: ocaml, oops, erlang
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Richard W.M. Jones <http://people.redhat.com/~rjones/>`__ сообщил, что
в Ocaml 4.00.0 для архитектуры x86\_64 `вернулась старая
ошибка <https://bugzilla.redhat.com/877128>`__, которую исправили в
версии 4.00.1. `Придется пересобирать все пакеты для Fedora
18 <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/172175>`__ с
новой версией Ocaml.

Заодно сообщаем планы на недавно анонсированную версию Erlang - R15B03. Сборка
для Fedora немного задержалась, но оказалось, что и к лучшему, т.к. `почти
сразу после выхода обнаружилась досадная ошибка в модуле ssl
<http://thread.gmane.org/gmane.comp.lang.erlang.general/65549/focus=65695>`__,
которая уже исправлена.

