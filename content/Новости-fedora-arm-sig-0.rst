.. title: Новости Fedora ARM SIG
.. slug: Новости-fedora-arm-sig-0
.. date: 2013-06-20 11:09:57
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


В последнее время участники этой группы были очень заняты. Результат их
трудов `был
представлен <http://blogs.arm.com/software-enablement/1012-applied-micro-x-gene-armv8-64-bit-server-showcased-at-red-hat-summit/>`__
на прошедшем `Red Hat Summit <http://www.redhat.com/summit/>`__. Это
Fedora 19, работающая на вскоре выходящем `64-битном ARM-сервере от
Applied Micro <http://www.apm.com/products/x-gene>`__ - первый в мире
64-битный ARM-дистрибутив работающий на первом в мире 64-битном
ARM-оборудовании. В проектировании системы принял участие уже известный
вам `велосипедист </content/arm-сервер-и-велосипедостроительство>`__ и
участник Fedora ARM SIG `Jon
Masters <https://plus.google.com/106265217227408958782/about>`__. Машина
получилась прорывной - это и использование стандартных компонентов,
таких, как UEFI, IPMI, ACPI, вместо, как ранее было принято в
ARM-железе, кучки самодельных хаков, и использование `Unified
Kernel </content/Прогресс-в-разработке-fedora-для-arm>`__. Подробности
Jon рассказал во время своей презентации на Red Hat Summit (доступны
`слайды <http://people.redhat.com/jcm/arm/masters_t_0120_hyperscale_redhat_powered_arm_server.pdf>`__
и `короткий
видеоролик <http://www.youtube.com/watch?v=ZEEZKg4ix_E&feature=share>`__).

Вся работа была проведена совместно с другими заинтересованными
компаниями в рамках проекта Linaro, в котором Red Hat принимает
непосредственное участие.

Red Hat не только представляет новое железо, но и занимается
`dogfooding-ом <http://en.wikipedia.org/wiki/Eating_your_own_dog_food>`__.

Новое (пока 32-битное) ARM железо от
`Calxeda <http://www.calxeda.com/>`__
`заменило <http://semiaccurate.com/2013/05/15/redhat-put-calxeda-based-arm-servers-in-to-production/>`__
старый кластер из машинок уровня PandaBoard (`фото
1 <http://paulfedora.wordpress.com/2010/10/04/hardware-has-arrived/>`__,
`фото
2 <http://blog.chris.tylers.info/index.php?/archives/249-Fedora-ARM-PandaStack.html>`__,
`фото
3 <http://paulfedora.wordpress.com/2010/07/09/fedora-arm-buildsystem-status-update/>`__).

Теперь все пакеты для Fedora ARM собираются `на этих новых
серверах <http://slashdot.org/topic/datacenter/fedora-calxeda-roll-out-new-arm-powered-servers/>`__.

Вообще, отвлекшись немного от Fedora, надо заметить, что ARM для
серверного сегмента становится очень горячей темой. Мы уже говорили вам,
что `AMD анонсировала планы переключиться на
ARM-архитектуру </content/amd-переходит-на-arm>`__, и наконец-то эти
планы начали обретать видимые очертания - `анонсировано о начале выпуска
ARM-систем начиная с 2014
года <http://www.theregister.co.uk/2013/06/18/amd_opteron_arm_server_chips/>`__.

Участники Fedora ARM SIG не только помогают создавать новые платформы
для дата-центров, но и работают над проектами, ориентированными на
обычного пользователя. Уже `известный
вам </content/rob-clark-присоединяется-к-команде-разработчиков-red-hat>`__
участник Fedora ARM SIG `Rob Clark <https://github.com/robclark>`__
упорно продолжает работать над
`freedreno <http://freedreno.github.io/>`__ (об этом проекте вы
`слышали </content/Начальная-поддержка-google-nexus-4-в-видеодрайверах-xorg>`__).

В последний месяц он окончательно добавил поддержку Qualcomm A3XX
(используется, например, в Google Nexus 4) в свой видеодрайвер. Это
пришлось сделать в несколько этапов. Сначала надо было `переписать
ускорение 2D с помощью
3D-операций <http://www.phoronix.com/scan.php?page=news_item&px=MTM3OTk>`__,
т.к. этот чип больше не содержит 2D-ускорителя. Как только он закрыл эту
задачу, то сразу стало возможным `запустить gnome-shell на Nexus
4 <http://bloggingthemonkey.blogspot.com.es/2013/06/freedreno-gnome-shell-on-nexus4a320.html>`__.

После этого, раз стало возможным запускать GNOME, он `быстро набросал
инсталлятор для Fedora
19 <http://bloggingthemonkey.blogspot.ru/2013/06/fedora-19-installer-for-nexus4.html>`__.

Обратите внимание, это **не Anaconda**! Еще необходимо заметить, что
Fedora для Nexus 4 не будет работать на базе CyanogenMod, как это
сделано в мобильной версии известного дистрибутива Linux для начинающих
- у нас все по-честному. И наконец, добившись работы Fedora на Google
Nexus 4, он подчистил то, что уже имелось, и включил `окончательную
версию патчсета в основное дерево
Mesa <http://cgit.freedesktop.org/mesa/mesa/commit/?id=2855f3f>`__.

Опять отвлекаясь от Fedora, но раз уж заговорили о видеодрайверах для
ARM-железа, то нельзя не упомянуть титаническую работу по созданию
полностью открытого драйвера для Mali, проведенную в одиночку бывшим
инженером Novell и участником проектов X.org, Debian и Coreboot, `Luc
Verhaegen <https://www.openhub.net/accounts/libv>`__. В последние месяцы
он `добился впечатляющих
результатов <http://libv.livejournal.com/24735.html?nojs=1>`__, и
быстродействие его варианта видеодрайвера сравнялось с проприетарным
блобом для Android. Молодец, Luc!
