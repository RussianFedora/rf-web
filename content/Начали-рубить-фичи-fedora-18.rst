.. title: Начали "рубить" фичи Fedora 18
.. slug: Начали-рубить-фичи-fedora-18
.. date: 2012-09-12 11:56:05
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Стартовала серия печальных собраний FESCo - после оптимистичных и
  радостных предыдущих собраний, пришло время трезвой оценки готовности
  принятых ранее фич. `Не уложились в
  график <https://fedorahosted.org/fesco/ticket/932>`__ следующие фичи:

-  `Кэширование
   Kerberos-мандатов <https://fedoraproject.org/wiki/Features/KRB5DirCache>`__
   (мэйнтейнер пытается уложиться в график).

-  `Обновление языка
   D <https://fedoraproject.org/wiki/Features/F18_D_programming>`__
   (застрял на package review).

-  `Новые правила SELinux для
   systemd <https://fedoraproject.org/wiki/Features/SELinuxSystemdAccessControl>`__
   (Dan Walsh отослал патчи в systemd, и там их рассматривают - скорее
   всего успеют, т.к. все участники очень продуктивны).

-  `QXL/Spice KMS
   Driver <https://fedoraproject.org/wiki/Features/QXLKMSSupport>`__ (не
   успевают оттестировать и, видимо, не успеют - а в вашем дистрибутиве
   проводят тестирование?)
-  `Agent-Free Systems
   Management <https://fedoraproject.org/wiki/Features/AgentFreeManagement>`__
   (мэйнтейнер не отвечает).

-  `Начальная настройка
   системы <https://fedoraproject.org/wiki/Features/InitialExperience>`__
   (вылетели из графика, скорее всего нагонят).

-  `Реорганизация групп пакетов в
   yum <https://fedoraproject.org/wiki/Features/ReworkPackageGroups>`__
   (написаны патчи, рассматриваются в yum / rpm / anaconda).

-  `Отказ от скриптов usermode в пользу
   PolKit <https://fedoraproject.org/wiki/Features/UsermodeMigration>`__
   (большая задача - идет тяжело и, вероятно, будет перенесена на Fedora
   19).

-  `LLVM для PowerPC
   64 <https://fedoraproject.org/wiki/Features/LLVMonPPC64>`__ (что-то
   застряло в IBM, но может быть еще успеют нагнать).

-  `ownCloud <https://fedoraproject.org/wiki/Features/OwnCloud>`__
   (застрял на package review).

-  `Поддержка LLVMpipe в VNCServer на PowerPC
   64 <https://fedoraproject.org/wiki/Features/VNCServerWithLLVMpipe>`__
   (заблокировано LLVM для PowerPC 64).

-  `Sugar 0.98 <https://fedoraproject.org/wiki/Features/Sugar_0.98>`__
   (мэйнтейнер обещает ускориться).


| 
| Отдельно выражены сомнения в успехе MATE (и особенно - в степени
  готовности, декларируемой теперь уже единственным мэйнтейнером), но
  нас это `не
  удивило </content/На-неделю-откладывается-релиз-fedora-18>`__.

| Неясна ситуация с фичей `tmp-on-tmpfs (монтирование /tmp как
  tmpfs) <https://fedoraproject.org/wiki/Features/tmp-on-tmpfs>`__,
  предложенной Lennart Poettering. `Споры вокруг нее идут уже четвертую
  неделю <https://fedorahosted.org/fesco/ticket/940>`__, и у Lennart
  Poettering неожиданно оказались сильные оппоненты (не привычная шумная
  толпа анонимных аналитиков, с маргинальными дистрибутивами наперевес,
  а опытные разработчики с десятками лет стажа, знакомые с предметной
  областью и использующие *техническую* аргументацию). Теперь ее будущее
  очень неопределенно. Вероятно, ее сделают включающейся по желанию
  пользователя в момент первоначальной установки.

