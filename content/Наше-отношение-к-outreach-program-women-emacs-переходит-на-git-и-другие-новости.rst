.. title: Наше отношение к Outreach Program for Women, Emacs переходит на Git и другие новости
.. slug: Наше-отношение-к-outreach-program-women-emacs-переходит-на-git-и-другие-новости
.. date: 2014-10-27 17:50:36
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Aleksandra Fedorova изложила позицию по отношению к "Outreach Program
for Women", разделяемую нашим маленьким локальным
коммьюнити <https://plus.google.com/106519095760339600726/posts/YdY8ZjWgtff>`__.

Owen Taylor
`анонсировал <http://blog.fishsoup.net/2014/10/23/perf-gnome-org-introduction/>`__
ввод в строй средства мониторинга производительности
`perf.gnome.org <https://perf.gnome.org/>`__. Это CI-система для раннего
выявления регрессий производительности. `Новость уже обсуждается
коллегами-аналитиками на
OpenNET.ru <http://www.opennet.ru/opennews/art.shtml?num=40926>`__.

На LWN.net, за paywall выложили
`статью <https://lwn.net/Articles/616859/>`__ про любителей `Cute
Embedded Nonsense Hacks </content/cute-embedded-nonsense-hacks>`__,
которые вместо следования заветами Jon Masters (`ACPI и
UEFI </content/arm64-те-aarch64-и-непростой-путь-перехода-arm-на-новые-стандарты>`__)
продолжают упорствовать в расколе. Вместо ACPI и UEFI, они разрабатывают
DeviceTree оверлеи - возможность ядром изменять DT-описания. Логику нам,
если честно, сразу постичь не удается, ведь DeviceTree разрабатывалось
для оборудования, которое ядро определить не может, и поэтому ему нужно
явно о нем сказать (описать в DeviceTree). А теперь, получается, они
встраивают механизм в ядро для изменения описаний DT при изменении в
оборудовани. А как оно будет работать, если по начальному условию, у
ядра нет возможности определить оборудование? Nonsense, как и было
сказано. Но посмотрим, конечно, как пойдет.

На Red Hat Developers Blog появилась статья про новый функционал GCC
(`по очень непроверенным слухам немного позаимствованный из
LLVM <http://clang.llvm.org/docs/UsersManual.html#controlling-code-generation>`__)
- `GCC Undefined Behavior Sanitizer –
ubsan <http://developerblog.redhat.com/2014/10/16/gcc-undefined-behavior-sanitizer-ubsan/>`__.

И напоследок, долгожданная новость. `Emacs переходит с bzr на
git <https://plus.google.com/+EricRaymond/posts/agdbxccbxGu>`__!
Понадобилось всего `10 месяцев </content/Короткие-новости-20>`__.

Удивительно, что еще остались проекты, `использующие
bazaar <https://en.wikipedia.org/wiki/GNU_Bazaar#Projects_using_Bazaar>`__!

