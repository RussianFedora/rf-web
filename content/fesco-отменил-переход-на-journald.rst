.. title: FESCo отменил переход на Journald
.. slug: fesco-отменил-переход-на-journald
.. date: 2012-03-20 00:25:44
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


На прошедшем сегодня собрании FESCo `начали
принимать <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/161156>`__
"фичи" для Fedora 18. Среди принятых:

-  Одно из больших планирующихся изменений, это `ARM будет основной
   архитектурой <https://fedoraproject.org/wiki/Features/FedoraARM>`__.

   Ошибка сборки пакета на ней теперь будет блокировать включение его в
   Fedora (как это обстояло с PPC и PPC64 архитектурами раньше).

-  `Обновление pcre до версии
   8.30 <https://fedoraproject.org/wiki/Features/pcre8.30>`__. С этой
   версии в pcre доступна поддержка UTF-16.

-  `Поддержка режима HotSpot в
   Networkmanager <https://fedoraproject.org/wiki/Features/RealHotspot>`__.

-  `Реорганизация метаданных для
   yum <https://fedoraproject.org/wiki/Features/ReworkPackageGroups>`__.

   Сейчас они хранятся в виде одного большого comps-файла, что невыгодно
   в ряде случаев.

-  `Обновление RPM до версии
   4.10 <https://fedoraproject.org/wiki/Features/RPM4.10>`__. Это, в
   основном, исправления ошибок и оптимизации, так-что обычные
   пользователи скорее всего ничего и не заметят.

-  `Перемещение мандата
   kerberos <https://fedoraproject.org/wiki/Features/KRB5CacheMove>`__
   из /tmp в /run/user/$USERNAME

И наконец, наверное наиболее важная новость, это то, что единогласно (8
голосов против, 0 за) было принято решение `**отказаться от
перехода** <https://fedoraproject.org/wiki/Features/systemd-journal>`__
на Journald. В свете `последних
улучшений <http://russianfedora.ru/content/lumberjack-%D0%B8%D0%BB%D0%B8-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5-%D0%B6%D1%83%D1%80%D0%BD%D0%B0%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5>`__
в системе журналирования событий, те нововведения, которые привносит
этот компонент, уже не так актуальны. Отказ касается только включения
этой "фичи" в Fedora 18, и возможно ее предложат в измененном виде, учтя
критику, в Fedora 19 или позже.

