.. title: Новые "фичи" Fedora 19
.. slug: Новые-фичи-fedora-19
.. date: 2013-01-24 14:40:42
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Список уже принятых FESCo фич, `о которых вы уже
  знаете </content/Начали-принимать-фичи-в-fedora-19>`__, вчера
  пополнился еще несколькими:

-  `Обновление BIND до версии
   10 <https://fedoraproject.org/wiki/Features/BIND10>`__
-  Включение
   `Enlightenment <https://fedoraproject.org/wiki/Features/Enlightenment>`__,
   еще одного DE. Хорошо или плохо, но внедрение GNOME 3 в Fedora резко
   повысило интерес к не очень популярным до того альтернативным DE.

-  Включение
   `Erlyvideo <https://fedoraproject.org/wiki/Features/Erlyvideo>`__,
   многофункционального сервера для видеотрансляций, написанного на
   Erlang.

-  Традиционное `обновление
   Boost <https://fedoraproject.org/wiki/Features/F19Boost153>`__. В
   этот раз до версии 1.53.0.
-  Переименовали фичу DualStackNetworking. Теперь в рамках этой фичи
   будет произведена радикальная переработка `системы разрешения сетевых
   имен (getaddrinfo) в
   glibc <https://fedoraproject.org/wiki/Features/FixNetworkNameResolution>`__.

   К сожалению, с появлением IPv6, IPv4+IPv6, в ней нашлись проблемы.

   Обратите внимание на страницу - там перечисляется их часть. Также
   интересная `дискуссия происходит в списке
   рассылки <https://thread.gmane.org/gmane.linux.redhat.fedora.devel.announce/947/focus=964>`__.

-  Запланированы улучшения в `консольном интерфейсе к
   NetworkManager <https://fedoraproject.org/wiki/Features/NetworkManagerCLIAddConnection>`__.

   Планируется его полная доработка по функциональности до уровня его
   GUI-интерфейса.

-  `Как и предполагалось </content/nodejs-и-systemd>`__, в Fedora 19
   будет `полная поддержка разработки и запуска ПО на основе
   Node.js <https://fedoraproject.org/wiki/Features/NodeJS>`__. Конечно,
   пользоваться ею можно прямо сейчас, но кое-чего еще не хватает.

-  Будет реализована `проверка подписей пакетов на этапе первичной
   установки <https://fedoraproject.org/wiki/Features/PackageSignatureCheckingDuringOSInstall>`__.

   Это давняя проблема - ключи не проверяются во время первичной
   установки, и, учитывая, что она может производиться по сети, это
   может привести к очевидным проблемам (даже не хочется их называть,
   чтоб не накликать беду). Проблема в том, что раньше не было
   возможности сформировать "chain of trust" во время первичной
   установки, а теперь благодаря предустановленным ключам в
   RestrictedBoot (т.н. "SecureBoot") такая возможность есть.

-  `Обновление PHP до версии
   5.5 <https://fedoraproject.org/wiki/Features/Php55>`__
-  `Удаление
   PyXML <https://fedoraproject.org/wiki/Features/RemovePyXML>`__ и
   переход на стандартную, поддерживаемую библиотеку из python

| 
| Согласно новому порядку каждую фичу теперь анонсируют в рассылке
  разработчиков, где ее могут обсудить рядовые участники, а уж только
  потом она идет на обсуждение в FESCo. Уже анонсировано с десяток новых
  фич, которые поставлены сейчас обсуждаются, и вы можете принять в
  обсуждении участие - подписывайтесь на
  **devel\*lists.fedoraproject.org**!
