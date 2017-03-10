.. title: В systemd приходит управление сетью
.. slug: В-systemd-приходит-управление-сетью
.. date: 2013-11-06 12:00:02
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Разработчик Arch Linux, `Tom
Gundersen <https://plus.google.com/+TomGundersen/about>`__, в рассылке
systemd-devel сегодня `предложил первый вариант системного сервиса,
networkd <https://thread.gmane.org/gmane.comp.sysutils.systemd.devel/13935>`__.

Конфигурация сервиса производится с помощью ini-файлов, и сделана
несовместимой ни с NetworkManager, ни с рекомендуемыми Red Hat способами
настройки в /etc/sysconfig/network-scripts/\*, ни с connman. Пока
новшество вызвало смешанную реакцию.

