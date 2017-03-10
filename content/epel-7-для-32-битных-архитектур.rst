.. title: EPEL 7 для 32-битных архитектур
.. slug: epel-7-для-32-битных-архитектур
.. date: 2014-03-22 17:05:04
.. tags: epel, arm, centos
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Как только команда CentOS `уже начала пересборку RHEL 7 для 32-битных
архитектур </content/centos-начинает-набирать-скорость>`__, выброшенных
из RHEL 7, так сразу возникла проблема - EPEL для RHEL 7 существует лишь
для официально поддерживаемых архитектур, и ни x86, ни armv7 нет.

Хорошо, что пересборка EPEL 7 только началась, и участники CentOS не
сильно опоздали со своим
`предложением <https://thread.gmane.org/gmane.linux.redhat.fedora.epel.devel/9134>`__
о запуске пересборок для 'secondary arch' для EPEL. В целом коммьюнити
положительно приняло предложение, которое покрывает два потенциально
интересных "use case" - миграция с устаревающих 32-битных машин и рост
популярности ARM-платформ.

Параллельно с EPEL для secondary arch, группа заинтересованных лиц пока
обсуждает идею создания репозитория для RHEL, но с другими правилами
обновления пакетов - `EPIC (Extra Packages for Infrastructure and
Clouds) <https://thread.gmane.org/gmane.linux.redhat.fedora.epel.devel/9143/focus=9153>`__.

Посмотрим, что из этого выйдет.
