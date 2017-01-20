.. title: Поддержка произвольных команд в /sbin/service
.. slug: Поддержка-произвольных-команд-в-sbinservice
.. date: 2012-06-27 11:20:07
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


При переходе на systemd оказались потерянными произвольные,
неопределенные в LSB, команды. По стандарту LSB `их определено не так уж
и
много <http://refspecs.linuxbase.org/LSB_3.2.0/LSB-Core-generic/LSB-Core-generic/iniscrptact.html>`__,
поэтому порой приложения добавляют свои, благо это просто, в
init-скрипт. Это, разумеется, нестандартное поведение, но многие
администраторы к нему привыкли, и потеря этого будет довольно
болезненной в ряде случаев.

После непродолжительного обсуждения инженеры Red Hat `Bill
Nottingham <https://www.openhub.net/accounts/notting>`__ и `Michal
Schmidt <https://fedoraproject.org/wiki/User:Michich>`__ реализовали
поддержку `произвольных пользовательских команд из
init-скриптов <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/166326>`__.

Вкратце, приложение должно создать файл по адресу
*/usr/libexec/initscripts/legacy-actions/frobozz/xyzzy*, чтоб было
возможно выполнять команду */sbin/service frobozz xyzzy*. Переопределить
стандартные LSB команды таким образом не получится - авторы планируют
включить проверку на это в */sbin/service*.
