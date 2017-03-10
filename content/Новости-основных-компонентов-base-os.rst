.. title: Новости основных компонентов Base OS
.. slug: Новости-основных-компонентов-base-os
.. date: 2013-10-31 17:19:37
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| `Счастливые пользователи продолжают благодарить команду разработчиков
  systemd <https://thread.gmane.org/gmane.comp.sysutils.systemd.devel/13768>`__.

  В этот раз свое спасибо сказал еще один embedded-разработчик, инженер
  компании `Axis Communications <http://www.axis.com/ru/>`__. Они сильно
  упростили себе разработку и поддержку решений, используя systemd. Чтоб
  он лучше подходил под их нужды, они общаются с разработчиками,
  обсуждая и сравнивая различные подходы и отправляя багрепорты. Вот так
  вот! Это и называется конструктивный подход.

| Еще один embedded-разработчик, Pengutronix, перешел на предложенный
  нашими участниками `стандарт для
  загрузчиков <http://www.freedesktop.org/wiki/Specifications/BootLoaderSpec/>`__,
  одобренный FreeDesktop. Об этом они рассказали на недавно прошедшей
  `Embedded Linux Conference Europe
  2013 <http://events.linuxfoundation.org/events/embedded-linux-conference-europe>`__
  (`слайды их
  выступления <http://elinux.org/images/9/90/Barebox-elce2013-bootloaderspec.pdf>`__).

  До сих пор этот стандарт поддерживали лишь gummiboot и systemd (и
  `существует патч для
  grub2 <http://pkgs.fedoraproject.org/cgit/grub2.git/tree/0460-blscfg-add-blscfg-module-to-parse-Boot-Loader-Specif.patch>`__).

| Не очень хорошая новость. `Мы уже рассказывали
  вам </content/Опубликованы-рекомендации-для-разработчиков-оборудования-на-базе-aarch64-64-битный-arm>`__,
  что наш коллега,
  `велосипедист </content/arm-сервер-и-велосипедостроительство>`__ и
  участник Fedora ARM SIG `Jon
  Masters <https://plus.google.com/106265217227408958782/about>`__,
  участвовал в разработке спецификаций для производителей решений на
  базе архитектуры AArch64 - в них он потребовал наличия UEFI и ACPI. И
  вот, несколько неожиданное развитие событий - `UEFI Forum теперь будет
  управлять спецификациями
  ACPI <http://www.businesswire.com/news/home/20131029005610/en/UEFI-Forum-Includes-ACPI-Specification-Portfolio-Unites>`__.

  Надвигающуюся потенциальную проблему хорошо озвучил в `своей ленте
  Google+ <https://plus.google.com/113713059726404063654/posts/cLVf33eTBKv>`__
  разработчик Coreboot, `Patrick
  Georgi <https://www.openhub.net/accounts/patrick_georgi>`__ - UEFI Forum
  может запросто спрятать спецификации за некими юридическими
  соглашениями, что будет препятствием для разработчиков, особенно
  разработчиков открытого оборудования.

| `Вышел DNF версии
  0.4.6 <https://thread.gmane.org/gmane.linux.redhat.fedora.devel/187855>`__.

  Среди фич - долгожданная отмена транзакций (yum history undo) и
  ограничение по количеству устанавливаемых в параллель пакетов (kernel,
  например).

| Наш коллега, участник Fedora и сисадмин kernel.org, `Konstantin
  Ryabitsev <https://plus.google.com/114752601290767897172/about>`__ на
  Kernel Summit 2013 в Эдинбурге рассказал о апгрейде инфраструктуры
  kernel.org. На LWN за paywall уже лежит `рекап его
  выступления <https://lwn.net/Articles/572127/>`__. Из важного - теперь
  на серверах kernel.org SELinux включен в enforcing. А вы еще
  выключаете SELinux?
| Lennart Poettering `официально объявил о переходе с D-Bus на
  libsystemd-bus <https://plus.google.com/115547683951727699051/posts/2F6hmF9hw7K>`__
  (вы уже слышали, что `такая работа
  ведется </content/Короткие-новости-15>`__). Это позволило внедрить
  совершенно новую функциональность в systemd - встречайте утилиту
  systemd-run, с чьей помощью можно
| \*) Запускать произвольное приложение, как сервис systemd:

::

    # systemd-run /usr/bin/cpuburn

| 
| \*) Запускать произвольное приложение через ssh на удаленной машине,
  как сервис systemd:

::

    # systemd-run -H login.example.com /usr/bin/cpuburn

| 
| \*) Запускать произвольное приложение в контейнере, как сервис
  systemd:

::

    #  systemd-run -M mycontainer /usr/bin/cpuburn

| 
| Запущенные приложения будут работать под управлением systemd, и их
  логи будут собираться в Journald. Но особенно интересно, что поддержка
  libsystemd-bus сейчас расползается по другим утилитам, т.е. вероятно у
  нас будет возможность управлять systemd на удаленных машинах
  (systemctl, machinectl, loginctl, и т.п.). Это, скорее всего, оценят
  те, у кого `в systemd уже десятки и сотни тысяч контейнеров на
  множестве физических машин </content/Короткие-новости-про-облака>`__.

| А вот прошедший Automotive Linux Summit особых новостей не принес -
  `все те-же Tizen, Wayland,
  systemd <https://lwn.net/Articles/572228/>`__, так полюбившиеся
  embedded-разработчикам. Ну хотя, может мы чего-то упустили, так что
  посмотрите сами на
  `расписание <http://events.linuxfoundation.org/events/automotive-linux-summit-fall/program/schedule>`__
  и
  `слайды <http://events.linuxfoundation.org/events/automotive-linux-summit-fall/program/slides>`__.

