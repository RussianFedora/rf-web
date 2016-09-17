.. title: Syslog ужасен
.. slug: syslog-uzhasen
.. date: 2016-09-16 16:42:51 UTC+03:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

`Justin Azoff`_, безопасник из `National Center for Supercomputing
Applications`_, также решил рассказать `киборгам-любителям читать логи
глазами <http://russianfedora.pro/content/И-опять-про-бинарные-логи>`_ про `объективные
недостатки syslog
<https://www.bouncybouncy.net/blog/syslog-is-terrible/>`_.

.. _Justin Azoff: https://github.com/JustinAzoff
.. _National Center for Supercomputing Applications: http://www.ncsa.illinois.edu/

****

   Я ненавижу syslog.

   Протокол ужасен.

   Формат сообщений ужасен.

   API ужасен.


Протокол
========

`Документ с RFC по syslog <https://tools.ietf.org/html/rfc5424>`_ был обновлен в 2009 году.
Несмотря на то, что этот документ - недавний, это лишь формализация текущих реализаций syslog и содержит много лишнего из 1980х. Есть `альтернативы <http://docs.graylog.org/en/2.0/pages/gelf.html>`_, но ничего стандартизированного. Большинство встраиваемых устройств или готовых систем поддерживают лишь минимум функционала.

"Facilities"
------------

Заголовок сообщения syslog содержит несколько байтов зарезервированных
для обозначения источника сообщения. До сих пор `ююкаете
<https://ru.wikipedia.org/wiki/Uucp>`_? В протоколе syslog оно
поддерживается! Используете что-нибудь посовременнее 1985 года?
Отказать!

Жестко определены следующие "facilities"::

  Код    "Facility"
   0    kernel messages
   1    user-level messages
   2    mail system
   3    system daemons
   4    security/authorization messages
   5    messages generated internally by syslogd
   6    line printer subsystem
   7    network news subsystem
   8    UUCP subsystem
   9    clock daemon
  10    security/authorization messages
  11    FTP daemon
  12    NTP subsystem
  13    log audit
  14    log alert
  15    clock daemon (note 2)
  16    local use 0  (local0)
  17    local use 1  (local1)
  18    local use 2  (local2)
  19    local use 3  (local3)
  20    local use 4  (local4)
  21    local use 5  (local5)
  22    local use 6  (local6)
  23    local use 7  (local7)

..

  Значения "facility" ДОЛЖНЫ быть из диапазона от 0 до 23 включительно.


У большинства из 24 значений "facilitiy" также есть короткое слово,
ассоциированное со значением: kern, user, mail, auth, news, ftp, и так
далее. Вместо того, чтобы просто использовать 4 байта, чтобы
обозначить почту, как ‘mail’, его впихивают вместе со значением
приоритета сообщения ("priority") в 2 байта. А после того, как
сэкономили пару байтов, эти два байта записывают в кавычки - ``<>``.

Вместо кодирования сообщения от NTP с приоритетом 7 пятью байтами
("``7 ntp``"), его кодируют в 5 байт, как "``<103>``".

Почему это число заключено в скобки, а все остальное нет?

.. image:: https://www.bouncybouncy.net/images/brackets.png
   :alt: Brackets

Получается так, что поле "facility" полностью бесполезно в современных системах. Скорее всего, если вы получаете syslog-сообщения от приложения, то их всех пошлют, как ``local0``.

(не)Надежная доставка
---------------------

У большинства реализаций syslog есть пара опций доставки:

* Использовать TCP и `рисковать блокировкой всего приложения
  <https://blog.bitbucket.org/2012/01/12/follow-up-on-our-downtime-last-week/>`_
  если сервер недоступен.
* Использовать UDP и рисковать потерей сообщений под большой нагрузкой.

Ни один из этих вариантов не отвечает за потерянные сообщения:

  Протокол syslog не предоставляет подтверждения от доставке
  сообщений. Хотя некоторые транспортные протоколы могут предоставлять
  результат доставки, концептуально, syslog, это чисто симплексный
  протокол коммуникации.

Как то раз я мониторил около тысячи свитчей. Одна из наиболее
разъярявших меня проблем с syslog была такой - если порт аплинка
мигнул, вы не получите никакого сообщения об этом событии. В
большинстве случаев однокилобайтного буфера хватило бы для
гарантированной доставки всех сообщений.

Некоторые реализации syslog предоставляют надежную доставку, включая
буферизацию сообщений, когда сервер недоступен.

* `RFC 3195`_, которому стукнуло 15 лет, описывает вариант syslog с гарантированной доставкой.
* В rsyslog есть `RELP`_
* В syslog-ng есть `RLTP`_

.. _RFC 3195: https://tools.ietf.org/html/rfc3195
.. _RELP: http://www.rsyslog.com/doc/relp.html
.. _RLTP: https://www.balabit.com/documents/syslog-ng-pe-latest-guides/en/syslog-ng-pe-guide-admin/html/concepts-rltp.html

(не)Структурированные данные
============================

RFC5424 добавляет поддержку структурированных данных используя формат
``key="value"`` обрамленный скобками. Выглядит примерно так::

  ... [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"]

Это довольно хорошая спецификация, хотя в ней не указано, как
журналировать типизованные данные (int, bool), и нет поддержки
иерархических структур, таких, как списки.

Возьмем гипотетическое сообщение от SMTP::

  {from:"a@example.com", bytes:12345, to:["b@example.com", "c@example.com"], spam: false, status:"queued"}

Довольно легко его представить, как JSON, а в RFC5424 эквивалента нет.

К сожалению, это неважно, что в syslog поддержка структурированных
данных ограничена, так как подавляющее большинство ПО все равно не
поддерживает журналирование в таком формате.

ПО продолжает использовать неструктурированное `printf`-подобное
журналирование. Это явление я называю `lossy serialization`.

Мой любимый пример `lossy serialization`, это sshd. `sshd делает так <https://github.com/openssh/openssh-portable/blob/6cb6dcffe1a2204ba9006de20f73255c268fcb6b/auth.c#L301>`_, когда записывает результат аутентификации::

  authlog("%s %s%s%s for %s%.100s from %.200s port %d ssh2%s%s",
    authmsg,
    method,
    submethod != NULL ? "/" : "", submethod == NULL ? "" : submethod,
    authctxt->valid ? "" : "invalid user ",
    authctxt->user,
    ssh_remote_ipaddr(ssh),
    ssh_remote_port(ssh),
    authctxt->info != NULL ? ": " : "",
    authctxt->info != NULL ? authctxt->info : "");

``authlog`` это обертка, которая вызывает ``syslog()``.

Этот кусок кода генерирует примерно такие сообщения::

  Failed password for root from 192.168.50.65 port 34780 ssh2

Много человеко-лет было `потрачено
<https://github.com/Prelude-SIEM/prelude-lml-rules/blob/master/ruleset/ssh.rules>`_
в попытках `распарсить
<https://github.com/fail2ban/fail2ban/blob/0.10/config/filter.d/sshd.conf>`_
такие `сообщения
<https://github.com/beave/sagan-rules/blob/master/openssh.rules>`_. Зачастую,
эти попытки оканчивались ошибками и `проблемами с безопасностью
<http://dcid.me/texts/attacking-log-analysis-tools.html>`_.

Обратите внимание, что вызов ``authlog`` ничего не экранирует или кодирует. Попробуйте авторизоваться с таким именем пользователя - ``root from 8.8.8.8``::

  $ ssh 'root from 8.8.8.8'@localhost

А теперь проверьте syslog::

  Sep  3 15:25:49 box sshd[23076]: Failed password for invalid user root from 8.8.8.8 from 127.0.0.1 port 54460 ssh2

Если вы распарсите это сообщение неверно, то окажется, что кто-то с адреса 8.8.8.8 попытался залогиниться рутом::

  Failed password for invalid user root from 8.8.8.8

Внутри sshd, переменная ``ssh_remote_ipaddr(ssh)``, содержит
изолированное значение адреса удаленного хоста, но как только его
запишут в текстовый журнал, оно теряется внутри сообщения. Если бы
sshd (и любой другой демон, которому нужно журналировать
структурированные данные) использовал бы API, аналогичный указанному
ниже, можно было бы однозначно десериализовать данные обратно, вместо
той одностронней сериализации, что у нас сейчас есть.

::
   
   authlog("msg", authmsg,
        "method", method,
        "submethod", submethod,
        "valid", authctxt->valid,
        "user", authctxt->user,
        "remote_ip", ssh_remote_ipaddr(ssh),
        "remote_port", ssh_remote_port(ssh),
        "protocol", "ssh2",
        "info", authctxt->info)

И это можно было бы записать в журнал следующим образом::

  [msg="failed" method="password" valid="t", user="root" remote_ip="192.168.50.65" remote_port="34780" protocol="ssh2" info=""]


А сообщение с адресом внутри имени пользователя выглядело бы так::

  [msg="failed" method="password" valid="f", user="root from 8.8.8.8" remote_ip="127.0.0.1" remote_port="54460" protocol="ssh2" info=""]

API ужасен
==========

API syslog очень прост::

  void syslog(int priority, const char *format, ...);

Как журналировать структурированные данные, и правильно их экранировать? Думайте сами, удачи!
Может быть этот функционал стоит включить в libc? `НИКОГДА! <https://sourceware.org/bugzilla/show_bug.cgi?id=13464>`_.

TL;DR
=====

* У вас скорее всего не получится надежно журналировать на удаленный сервер.
* Если вы не уверены, что произойдет, если ваш syslog-сервер упадет, СРОЧНО проверьте.
* А в полученных сообщениях у вас будут проблемы с их обработкой (получением данных, нужных для бизнес-процесса).

Насчет бинарных логов
=====================

Популярно мнение, что бинарные логи, это зло, и единственный способ
вести системный журнал, это текстовые файлы.

Мне лично все равно - текстовые или бинарные логи. Однако, если вы
пытаетесь убедить окружающих не использовать бинарные логи, потому что
они "не читаются глазами" и могут быть легко повреждены, то вам
следует обратить внимание на то, как устроена ротация логов на вашей
машине. Ну просто, если после ротации ваши логи сжимаются чем-то вроде
gzip, то у вас уже нет текстовичков.

****

Justin довольно хорошо указал на основные проблемы текстовичков, которые киборги-любители читать глазами считывают прямо с сектором жесткого диска, без дополнительных утилит, типа gzcat и less. Конечно, мы не ожидаем, что слова еще одного специалиста внезапно на этот раз убедят в своей неправоте наших коллег, анонимных аналитиков с Linux-ресурсов в интернете.
