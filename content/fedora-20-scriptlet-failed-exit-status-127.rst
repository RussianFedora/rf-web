.. title: Fedora 20: scriptlet failed, exit status 127
.. slug: fedora-20-scriptlet-failed-exit-status-127
.. date: 2014-01-19 14:35:02
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: bookwar

**Это архивная статья**


Объявление для пользователей Fedora 20 и RFRemix 20:

| в пакете **selinux-policy-3.12.1-116.fc20** содержится баг, который
  проявляется при последующих обновлениях в виде примерно такого лога
  yum:

::

    warning: %post(libudisks2-2.1.2-1.fc20.x86_64) scriptlet failed, exit status 127
    Non-fatal POSTIN scriptlet failure in rpm package libudisks2-2.1.2-1.fc20.x86_64
      Обновление  : yum-3.4.3-130.fc20.noarch                                                       
    warning: %post(yum-3.4.3-130.fc20.noarch) scriptlet failed, exit status 127
    Non-fatal POSTIN scriptlet failure in rpm package yum-3.4.3-130.fc20.noarch
      Обновление  : system-config-language-1.4.0-7.fc20.noarch                                      

| Для решения проблемы нужно временно перевести selinux в разрешающий
  режим, обновить его политики, и включить enforced-режим обратно:

::

    # setenforce 0
    # yum clean expire-cache
    # yum update selinux-policy
    # setenforce 1

В пакете **selinux-policy-3.12.1-117.fc20** баг уже исправлен. Поэтому
если вы обновились сразу на него, пропустив обновление на версию
3.12.1-116, ничего делать не нужно.


Подробности на вики-странице `Common F20
Bugs <https://fedoraproject.org/wiki/Common_F20_bugs#RPM_scriplets_fail_during_updates>`__
