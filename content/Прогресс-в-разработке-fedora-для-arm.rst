.. title: Прогресс в разработке Fedora для ARM
.. slug: Прогресс-в-разработке-fedora-для-arm
.. date: 2012-10-27 20:34:52
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Продолжается работа над Fedora для ARM. Участник Fedora, `Andrew
Haley <https://fedoraproject.org/wiki/AndrewHaley>`__, сообщил `что им и
его коллегами по Red Hat ведется работа по портированию OpenJDK на
ARM64 <http://www.advogato.org/article/1067.html>`__. Пока на рынке нет
доступного оборудования, так что попробовать не получится. Но поскольку
Red Hat, Applied Micro и ARM `объявили о начале совместных работ по
созданию серверной платформы на базе
ARM64 <http://www.hpcwire.com/hpcwire/2012-10-25/arm_red_hat_appliedmicro_to_develop_disruptive_64-bit_server_platform.html>`__,
то мы скоро что-нибудь увидим.

А вот `Peter
Robinson <https://plus.google.com/117898952501074015902/posts>`__
сообщил более практически ценную новость - `в основной сборке ядра Linux
для Fedora включена поддержка т.н. Unified Kernel для
ARM <http://thread.gmane.org/gmane.linux.redhat.fedora.arm/4257>`__. Мы
`уже сообщали </content/Новости-secondary-arch-fedora>`__ о том, что
ведется работа в этом направлении, и вот - `первые
результаты <http://pkgs.fedoraproject.org/cgit/kernel.git/commit/?id=faa8d0c>`__
уже в Git-репозитории (а вскоре и в Koji). Не за горами тот час, когда
для новых ARM-устройств не понадобится собирать специфичное ядро для
каждой конкретной системы, и в ряде случаев даже можно будет
устанавливать с помощью графического инсталлятора.

Кстати, об инсталляторе Anaconda. Наша коллега `Tyler
Siprova <https://plus.google.com/u/0/100383574349411246751/about>`__
предлагает желающим очередную пачку вакансий в Red Hat, среди которых
есть `вакансия Python-разработчика для очередных масштабных переработок
Anaconda <https://plus.google.com/u/0/100383574349411246751/posts/5B6w9Lb5Vwv>`__.

Если кому по душе - обращайтесь к Tyler.

