.. title: Статус проекта Lumberjack
.. slug: Статус-проекта-lumberjack
.. date: 2012-11-26 14:38:04
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


После `анонса инициативы
Lumberjack </content/lumberjack-или-структурированное-журналирование>`__
прошло более полугода. За это время ситуация с системным журналом начала
улучшаться. Продолжается внедрение Journald, вышел rsyslog с поддержкой
CEE (и `уже включен в Fedora
18 <https://admin.fedoraproject.org/updates/FEDORA-2012-18876/librelp-1.0.1-1.fc18,rsyslog-7.2.2-1.fc18>`__),
созданы библиотеки - `ceelog <https://fedorahosted.org/ceelog/>`__,
`liblumberlog <https://github.com/deirf/libumberlog>`__, начат переход
"тяжелых" приложений на CEE-журналирование (например,
`libvirt <https://thread.gmane.org/gmane.comp.emulators.libvirt/64294>`__).

Другой популярный syslog-демон, syslog-ng, начиная с версии 3.3.1, также
обладает `поддержкой вывода сообщений в виде структурированного
JSON <https://www.balabit.com/files/syslog-ng/open-source-edition/3.3.1/changelog-en.txt>`__,
однако теперь автор `скептически настроен относительно
CEE <http://algernon.blogs.balabit.com/2012/08/another-month-rushed-away/>`__
и больше не собирается его поддерживать в своем продукте.

