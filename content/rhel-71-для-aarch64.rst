.. title: RHEL 7.1 для AArch64
.. slug: rhel-71-для-aarch64
.. date: 2015-06-22 23:33:53
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Недавно `анонсировали CentOS 7 для
AArch64 <https://thread.gmane.org/gmane.linux.centos.announce/9137>`__, и
вот - `официально
объявлено <https://www.redhat.com/en/about/blog/long-arm-linux-red-hat-enterprise-linux-server-arm-development-preview>`__
о сборке RHEL 7.1 для платформы AArch64.

Работа велась в рамках Fedora ARM SIG, и наш коллега, Jon Masters в
своей ленте Google+ делится своими воспоминаниями о том, `как все
развивалось <https://plus.google.com/+JonMasters/posts/AYMw5SVXioH>`__.

Для тех, кому интересно, как Red Hat становится технологическим лидером
отрасли, будет очень полезно ознакомиться, как компания постепенно
становилась одним из лидеров, ответственных за выработку стандартов
(удобных пржде всего для предлагающего их) в данной области. Подсказка -
действовать нужно не "реактивно", а "проактивно", загодя подготавливая
для себя выгодные условия, а не реагируя на сложившиеся обстоятельства,
становясь догоняющим.

Brendan Conoboy опубликовал `третью
статью <https://developerblog.redhat.com/the-arm-arc-part-3/>`__ из
цикла "The ARM Arc"
(`1-я <https://developerblog.redhat.com/arm-arc-part1/>`__ и
`2-я <https://developerblog.redhat.com/the-arm-arc-part-2-2/>`__ части),
в которой рассказал об отношениях Red Hat Enterprise Linux Server for
ARM Development Preview 7.1 (официальное название продукта) и Fedora.

Интересно, что если бы RHEL 7 базировался на Fedora 18, а не на Fedora
19 (плюс несколько пакетов из Fedora 20), то, как считает Brendan,
собрать RHEL 7 для AArch64 было бы малореально. Дело, конечно, не только
и не столько в количестве собирающихся без ошибок пакетов, а в том, что
на базе Fedora 19 разрабатывались стандарты на AArch64, которые позволят
запускать собранный дистрибутив на оборудовании, виртуальном или
"физическом", без `Cute Embedded Nonsense
Hacks </content/cute-embedded-nonsense-hacks>`__.

