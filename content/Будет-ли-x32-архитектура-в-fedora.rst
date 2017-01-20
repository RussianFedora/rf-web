.. title: Будет ли x32 архитектура в Fedora?
.. slug: Будет-ли-x32-архитектура-в-fedora
.. date: 2012-05-16 17:48:08
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Недавно Canonical анонсировала, что `в версии 12.10 будет поддержка
архитектуры
x32 <http://www.phoronix.com/scan.php?page=news_item&px=MTEwMTk>`__, о
которой `можно почитать
здесь <https://sites.google.com/site/x32abi/>`__. Закономерно у
участников Fedora возник вопрос - `обсуждалась ли возможность включения
этой новой архитектуры в
Fedora? <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/164019>`__
Незамедлительно были получены неутешительные ответы. Оказывается, что
Canonical, `как обычно в последнее
время <http://www.rfremix.ru/content/В-ubuntu-1210-ожидается-полноценная-поддержка-wayland-но-есть-нюанс>`__,
не уведомила разработчиков о своих планах - `Josh
Boyer <https://www.openhub.net/accounts/jwboyer>`__ сообщил, что `полной
поддержки x32 еще нет в Glibc, и вероятно не будет до версии
2.16 <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/164019/focus=164020>`__
(а уж только потом можно вести разговор о пересборке ПО). Также `Matthew
Garrett <https://plus.google.com/109386511629819124958/about>`__ выразил
сомнение, что `"обычные пользователи" увидят хоть какие-то
улучшения <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/164019/focus=164021>`__
(а ухудшения они точно увидят, как всегда бывает с новой архитектурой).

Однако, если найдутся желающие, у которых будет достаточно квалификации,
чтоб потянуть поддержку целой архитектуры, то это можно будет
реализовать, как очередную "secondary arch".
