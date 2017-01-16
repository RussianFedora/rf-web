.. title: Docker научился вести логи прямо в Journal
.. slug: docker-научился-вести-логи-прямо-в-journal
.. date: 2015-05-13 12:16:38
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Dan Walsh
`объявил <http://www.projectatomic.io/blog/2015/04/logging-docker-container-output-to-journald/>`__
об успешном включении еще одной опции для журналирования в Docker -
`ведение журнала напрямую в
Journal <https://github.com/docker/docker/pull/12557>`__. Ранее были
доступны опции *syslog*, *json* (по умолчанию), или *"без журнала"*.
