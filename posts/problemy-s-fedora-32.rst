.. title: Проблемы с Fedora 32
.. slug: problemy-s-fedora-32
.. date: 2020-05-22 19:32:07 UTC+03:00
.. tags: gcc, node.js, java, security
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Не успела `выйти Fedora 32 <https://www.linux.org.ru/news/redhat/15670322>`_, как в ней начали находиться странные `даже по описанию <https://bugzilla.redhat.com/show_bug.cgi?id=1827357>`_ ошибки. Оказалось, что в GCC 10, начиная с `лета 2019 года <https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=b9ef6a2e04bfd013>`_, содержится `неприятная ошибка <https://gcc.gnu.org/bugzilla/show_bug.cgi?id=94734`_, из-за которой в ряде случаев генерируется неправильно работающий код. Недоумевающие пользователи `начали обсуждать сложившуюся ситуацию <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/I2UU47UPDAFH4N25F3AQR7DDMTKR7NK6/>`_, в которой мы по сути не можем доверять ни одному приложению или библиотеке, собранной в Fedora 32 с GCC 10 примерно до апреля 2020 года. По уму, надо бы экстренно пересобирать все дерево пакетов снова, но в уже выпущенной версии Fedora мы так не делаем. Ну постепенно все битые пакеты так или иначе пересоберем.

Вообще, в Fedora 32, надо признать, появились проблемы. От полуразрушенной Java (которую, правда, `хотят отремонтировать <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/NGE3RS4U2LZ2DTLSSAURVDSKDKZM2PV4/>`_), `заброшенных NodeJS-пакетов <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/6RCOEGWV7U65E2PJVJL3FUTBEPSTS5ZT/#R6KGX5RZTMKUO4CRW5BYUW7V5W2EZOXC>`_ и до `слишком стремительно обновляющегося Python3 <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EMMLOXU6ZYT6DFPBTTVOD5DSGYKSJ7SH/>`_. Народ начал привычно возмущаться, зачем мы упаковываем JS- и в целом языко-специфичные проекты, когда в них есть свои полурабочие, зато стремительные и удобные пакетные менеджеры? Наши коллеги привели обычный список аргументов - более высокая степень интеграции, безопасность, удобное управление, и так далее. Интересно, что вот прямо недавно, вопросом безопасности таких менеджеров пакетов озаботились `исследователи из Университета Бонна <https://arxiv.org/abs/2005.09535>`_.
