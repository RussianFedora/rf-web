.. title: Итоговая пачка фич Fedora 21
.. slug: Итоговая-пачка-фич-fedora-21
.. date: 2014-06-22 21:17:14
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Уже готов итоговый список того нового, что будет ждать нас в Fedora
  21. Мы уже `несколько </content/Будущие-фичи-fedora-21>`__
  `раз </content/Еще-немного-будущих-фич-fedora-21>`__
  `рассказывали </content/Новые-фичи-fedora-на-подходе>`__
  `про </content/Новые-фичи-fedora-21>`__
  `принятые </content/Новые-фичи-fedora-21-0>`__
  `фичи </content/Новые-фичи-fedora-21-1>`__ по мере их поступления, а
  теперь можно подвести промежуточный итог (курсивом выделены фичи, про
  которые мы уже говорили, а зачеркнуты фичи, которые пришлось перенести
  или от которых пришлось отказаться):

-  `(А)периодически обновляемые базовые установочные образы для облачных
   систем <https://fedoraproject.org/wiki/Changes/(A)Periodic_Updates_to_Cloud_Images>`__.

   Планируется их периодически пересобирать, скажем для включения
   исправлений безопасности.

-  *`Доработка autofs - добавление парсера
   amd-формата <https://fedoraproject.org/wiki/Changes/Add_amd_map_parser_to_autofs>`__
   (`automount daemon <http://www.am-utils.org/>`__). Проект am-utils
   заброшен, и autofs выглядит более перспективно, но, к сожалению, в
   autofs до сих пор не хватает некоторого функционала из am-utils,
   среди которого поддержка amd-формата. Вот его добавление и
   запланировано.*
-  *`Полная поддержка чипов Allwinner sunxi (A10 / A13 /
   A20) <https://fedoraproject.org/wiki/Changes/AllwinnerSunxiSupport>`__
   (используются, например, в
   `CubieTruck <http://www.cubietruck.com/>`__). Работа будет проведена
   в рамках `Fedora ARM
   SIG <https://fedoraproject.org/wiki/Architectures/ARM>`__. До сих пор
   Fedora на этой платформе работала благодаря ремиксу, а теперь
   планируется включить все нужное прямо в Fedora для ARM. К сожалению,
   поддержка графического режима работы пока не планируется.*
-  *Включение в репозиторий `Amplab
   Tachyon <https://fedoraproject.org/wiki/Changes/AmplabTachyon>`__,
   распределенной файловой системы. Эта работа проводится в рамках
   `Fedora BigData
   SIG <https://fedoraproject.org/wiki/SIGs/bigdata>`__.*
-  `Anaconda Server
   Roles <https://fedoraproject.org/wiki/Changes/AnacondaServerRoleSupport>`__
   - плугин для анаконды, реализующий некоторые часто используемые
   операции для серверов, слишком сложные для скриптов в секции %post.

-  Включение в репозиторий `Apache
   Accumulo <https://fedoraproject.org/wiki/Changes/ApacheAccumulo>`__,
   распределенного KV-хранилища.

-  Включение в репозиторий `Apache
   Ambari <https://fedoraproject.org/wiki/Changes/ApacheAmbari>`__,
   фреймворка для управления кластерами и GUI для Hadoop.

-  *Включение в репозиторий `Apache
   HBase <https://fedoraproject.org/wiki/Changes/ApacheHBase>`__,
   распределенной базы данных, построенной на базе Hadoop.*
-  *Включение в репозиторий `Apache
   Hive <https://fedoraproject.org/wiki/Changes/ApacheHive>`__,
   хранилище данных, построенное на базе Hadoop.*
-  *Включение в репозиторий `Apache
   Mesos <https://fedoraproject.org/wiki/Changes/ApacheMesos>`__,
   система управления кластерами. Можно сказать, что это микроядро для
   кластерных систем. Также для `Fedora BigData
   SIG <https://fedoraproject.org/wiki/SIGs/bigdata>`__.*
-  *Включение в репозиторий `Apache
   Oozie <https://fedoraproject.org/wiki/Changes/ApacheOozie>`__,
   планировщика заданий Hadoop.*
-  Включение в репозиторий `Apache
   Pig <https://fedoraproject.org/wiki/Changes/ApachePig>`__, платформы
   для анализа больших объемов данных.

-  Включение в репозиторий *`Apache
   Spark <https://fedoraproject.org/wiki/Changes/ApacheSpark>`__, еще
   одного кластерного компонента, предназначенного для обработки больших
   объемов данных.*
-  `AppInstaller <https://fedoraproject.org/wiki/Changes/AppInstallerContinued>`__
   - полная интеграция `нового инсталлятора ПО в
   GNOME </content/Дополнения-к-приложениям-в-gnome-software>`__.

-  *`Обновление Erlang до версии
   17 <https://fedoraproject.org/wiki/Changes/BetterErlangSupport>`__, и
   начало работы по интеграции Erlang и systemd.*
-  `Выпуск нескольких дополнительных установочных образов для приложений
   Big Data в облачных
   системах <https://fedoraproject.org/wiki/Changes/Big_Data_Cloud_Image>`__.

-  Внедрение технологии `LVM Cache Logical
   Volumes <https://fedoraproject.org/wiki/Changes/Cache_Logical_Volumes>`__,
   когда в LVM быстрые SSD-диски используются для кэширования более
   медленных.

-  Включение `Cockpit
   Project <https://fedoraproject.org/wiki/Changes/CockpitManagementConsole>`__
   по умолчанию в образы для Fedora Server.

-  `Более удобный способ использования образа для облачных систем для
   обычных
   серверов <https://fedoraproject.org/wiki/Changes/Convert_Fedora_Cloud_Image_to_Fedora_Server>`__.

   Т.е. быстрый способ попасть `со скотного двора в
   дом <https://www.theregister.co.uk/2013/03/18/servers_pets_or_cattle_cern/>`__.

-  [STRIKEOUT:*`Перевод приложений с cron jobs на timer-юниты
   systemd <https://fedoraproject.org/wiki/Changes/cron-to-systemd-time-units>`__*].
   Участник `покинул Fedora Project из-за несогласия по ряду
   вопросов <https://lists.fedoraproject.org/pipermail/test/2014-May/121356.html>`__.

-  *`Унификация системных
   крипто-политик <https://fedoraproject.org/wiki/Changes/CryptoPolicy>`__.

   Это еще один шажок в сторону унифицированного общесистемного
   криптографического фреймворка, с централизованным управлением. Сейчас
   планируется ввести общесистемную установку уровня безопасности. В
   идеале, изменяя некий текстовый файл, системный администратор
   установит минимальный размер ключей, список допустимых
   криптоалгоритмов и т.п. для всей системы. Все крипто-библиотеки и
   крипто-приложения должны учитывать установленные параметры. Работы
   довольно много - это не 11 новых обоев, но мы надеемся, что наши
   коллеги успеют.*
-  *`Поддержка ведения журнала CUPS в
   journald <https://fedoraproject.org/wiki/Changes/CupsJournalLogging>`__,
   который традиционно пишет в файлики в */var/log/* Это часть более
   значительного проекта по унификации ведения журнала во всех
   приложениях и демонах. Мы уверены, что все OpenSource-приложения
   должны перестать писать в файлики, в syslog и т.п, и переходить на
   унифицированный фреймворк, предоставляемый systemd, т.е. journald. И
   мы надеемся, что вы в ближайшее время услышите еще о фичах из этой
   серии.*
-  Среди ролей проекта Fedora Server будет `роль сервера базы
   данных <https://fedoraproject.org/wiki/Changes/DatabaseServerRole>`__.

-  `Официальный образ Fedora для
   Docker <https://fedoraproject.org/wiki/Changes/Docker_Container_Image>`__,
   собранный Fedora Release Engineering, а не кем-то еще.

-  Среди ролей проекта Fedora Server будет `контроллер домена (на основе
   FreeIPA) <https://fedoraproject.org/wiki/Changes/DomainControllerServerRole>`__.

-  `Обновление Boost до версии
   1.56 <https://fedoraproject.org/wiki/Changes/F21Boost156>`__.

-  `Обновление Make до версии
   4.0 <https://fedoraproject.org/wiki/Changes/F21Make40>`__.

-  `Обновление TCL/TK до версии
   8.6 <https://fedoraproject.org/wiki/Changes/f21tcl86>`__.

-  *Очередное изменение во флагах GCC по умолчанию - `включение
   *-Werror=format-security* <https://fedoraproject.org/wiki/Changes/FormatSecurity>`__.

   Как обычно, будет запланирована полная пересборка всего дерева. В
   качестве теста мы уже попробовали пересобрать дерево, и нашли `почти
   две сотни
   проблем <https://bugzilla.redhat.com/showdependencytree.cgi?id=1038083&hide_resolved=0>`__,
   часть из которых уже исправлена (и патчи, как обычно, уже отправлены
   или отправляются в апстрим). Типичное исправление `выглядит довольно
   просто <https://src.fedoraproject.org/cgit/rtpproxy.git/tree/rtpproxy-0008-Fix-FTBFS-if-Werror-format-security-flag-is-used.patch>`__,
   но его нужно сделать, чем мы традиционно и занимаемся.*
-  `Фреймворк для управлений ролями Fedora
   Server <https://fedoraproject.org/wiki/Changes/FrameworkForServerRoleDeployment>`__.

-  *`Обновление GCC до версии
   4.9.x <https://fedoraproject.org/wiki/Changes/GCC49>`__. Как всегда,
   запланирована полная пересборка всех пакетов.*
-  *`Обновление GHC до версии
   7.8 <https://fedoraproject.org/wiki/Changes/GHC_7.8>`__. Работа будет
   проведена участниками `Fedora Haskell
   SIG <https://fedoraproject.org/wiki/Haskell_SIG>`__.*
-  `GNOME 3.12 <https://fedoraproject.org/wiki/Changes/GNOME3.12>`__,
   вышедший `несколько месяцев назад </content/Короткие-новости-23>`__,
   и `уже доступный в специальном тестовом выпуске RFFemix
   20 </content/rfremix-20-gnome-312-edition>`__.

-  *`"Headless"
   Java <https://fedoraproject.org/wiki/Changes/HeadlessJava>`__. Одной
   из популярных претензий к большим языковым платформам, поставляемым в
   Fedora /RHEL, было "мне нужно запустить демон на %название\_языка%, а
   он тянет за собой пол-иксов" (например, так жалуются на
   `Erlang <https://bugzilla.redhat.com/784693>`__). Теперь появится
   возможность поставить Java без "десктопных" компонентов, таких, как
   X11 и PulseAudio.*
-  *`Улучшенная интеграция менеджера пакетов Apache Ivy с
   Fedora <https://fedoraproject.org/wiki/Changes/ImprovedIvyPackaging>`__.*
-  *`Улучшения в экосистеме
   Scala <https://fedoraproject.org/wiki/Changes/ImprovedScalaEcosystem>`__.

   Несмотря на то, что в Fedora формально Scala уже есть, пользоваться
   ей, без сторонних репозитариев, пока было сложно. В рамках этого
   изменения будет добавлен ряд отсутствующих компонентов.*
-  *`Перенесенная с Fedora 20 </content/И-опять-новые-фичи-fedora-20>`__
   фича - `поддержка DNSSEC в
   FreeIPA <https://fedoraproject.org/wiki/Changes/IPAv3DNSSEC>`__.*
-  *`Java 8 по
   умолчанию <https://fedoraproject.org/wiki/Changes/Java8>`__ - очень
   серьезное изменение.*
-  Долгожданное включение
   `Jenkins <https://fedoraproject.org/wiki/Changes/Jenkins>`__. ДО сих
   пор его у нас не было, как это ни прискорбно.

-  *`System-wide
   jQuery <https://fedoraproject.org/wiki/Changes/jQuery>`__. Сейчас у
   нас нет пакета с jQuery в дистрибутиве, поэтому каждое приложение,
   которое его использует, тянет его как `bundled
   lib </content/bundled-libraries-немного-статистики-и-комментариев-к-ней>`__,
   и эта практика в общем случае `приводит к куче
   проблем </content/Досмеялись-Серьезная-ошибка-в-gnutls>`__. Теперь,
   после включения пакета в дистрибутив, от мэйнтейнеров приложений,
   использующих jQuery, будет требоваться перейти на system-wide копию,
   либо получить от FESCo разрешение.*
-  *Обновление KDE до `KDE Frameworks
   5 <https://fedoraproject.org/wiki/Changes/KDE_Frameworks_5>`__.*
-  [STRIKEOUT:*`Переход с bzip2 на
   lbzip2 <https://fedoraproject.org/wiki/Changes/lbzip2>`__,
   независимую реализацию, поддерживающую многопоточность. Сейчас идет
   обсуждение этой фичи, и некоторые наши коллеги сомневаются в
   целесообразности полного перехода, т.к. в рамках lbzip2 не было
   предусмотрено библиотечного API. Автор утверждает, что может "легко
   запилить", но это мы слышим постоянно, и народ был неособо этим
   впечатлен.*]. Отказались (отложили до Fedora 22 или позднее).

-  `libzhuyin <https://fedoraproject.org/wiki/Changes/libzhuyin>`__,
   незатейливо названный компонент (очередной!) для ввода китайских
   символов.

-  *`Переименование фонтов Lohit Oriya и Lohit Punjabi в Lohit Odia и
   Lohit
   Gurmukhi <https://fedoraproject.org/wiki/Changes/Lohit_Odia_Gurmukhi>`__,
   как того требует правительство индийского штата Орисса.*
-  `Обновление MariaDB до версии
   10.0 <https://fedoraproject.org/wiki/Changes/MariaDB10>`__.

-  *`Обновление MATE до версии
   1.8 <https://fedoraproject.org/wiki/Changes/MATE_1.8>`__.*
-  *`Сделать ядро Linux более
   модульным <https://fedoraproject.org/wiki/Changes/Modular_Kernel_Packaging_for_Cloud>`__,
   чтоб не устанавливать (или легко удалять) ненужные модули при
   установке в виртуальные машины.*
-  `Обновление Mono в Fedora с версии 2.10 до
   3.4 <https://fedoraproject.org/wiki/Changes/Mono_3.4>`__. Мы уж
   думали, что Mono забросили.

-  `Создавать официальные облачные образы с помощью Anaconda и
   Koji <https://fedoraproject.org/wiki/Changes/Move_to_ImageFactory_For_Cloud_Image_Creation>`__.

   Это и повысит прозрачность и создания, и упростит повторяемость
   процесса, и просто улучшит качество Anaconda и нашей инфраструктуры.

   Чем меньше нестандартных утилит и шагов используется в работе нашей
   rel-eng группы, тем лучше.

-  *Включение в репозиторий `NFS
   Ganesha <https://fedoraproject.org/wiki/Changes/NFSGanesha>`__,
   независимой реализации NFS-сервера, работающей в user-space. Работа
   будет проведена одним из upstream-разработчиков.*
-  *`Базовая поддержка OpenCL в Fedora
   21 <https://fedoraproject.org/wiki/Changes/OpenCL>`__.*
-  *`Объявить \*-javadoc пакеты
   необязательными <https://fedoraproject.org/wiki/Changes/OptionalJavadocs>`__.

   С начала массовых пересборок для ARM и переходом на Java 8,
   выяснилось, что 80% ошибок сборки возникли во время создания
   javadoc-пакетов. Было решено сделать их необязательными, чтоб не
   блокировать сборку основных пакетов. Исправление ошибок в javadoc,
   это невысокоприоритетная задача, так как полно более важных дел, но
   когда-нибудь мы может быть возьмемся и за нее.*
-  *`Общесистемная политика доступа к
   смарт-картам <https://fedoraproject.org/wiki/Changes/PcscAccessControl>`__.

   Ну тут все понятно. Планируется запретить неавторизованным
   пользователям и/или процессам доступ к смарт-картам.*
-  `Обновление PHP до версии
   5.6. <https://fedoraproject.org/wiki/Changes/Php56>`__
-  `Репозиторий-песочница <https://fedoraproject.org/wiki/Changes/Playground_repository>`__.

   Мы продолжаем экспериментировать с формами взаимодействия
   мэйнтейнеров и пользователей. В рамках этой фичи будет создан
   "тестовый" репозиторий, в котором будут находиться пакеты в процессе
   их рецензирования или просто экспериментальные. Особенно отмечается,
   что в репозиторий запрещено включать ПО нарушающее т.н. `"софтверные
   патенты" <http://peter.fedorapeople.org/presentations/Pirate_Party_Russia_2012_full.pdf>`__.

-  *`PrivateDevices=yes и PrivateNetwork=yes для всех сервисов, которые
   предназначены для долговременной
   работы <https://fedoraproject.org/wiki/Changes/PrivateDevicesAndPrivateNetwork>`__.

   Это очередная фича systemd, которую мы начнем активно использовать.

   Идея в том, чтобы отобрать у сервисов, которым это не нужно, доступ к
   физическим устройствам (PrivateDevices=yes), или вообще доступ к сети
   (PrivateNetwork=yes). Такие ограничения резко снизят возможности
   злоумышленников.*
-  *`Обновление Python3 до версии
   3.4 <https://fedoraproject.org/wiki/Changes/Python_3.4>`__*
-  [STRIKEOUT:*`Python3 по
   умолчанию <https://fedoraproject.org/wiki/Changes/Python_3_as_Default>`__*].
   Решили перенести на Fedora 22.

-  `Пересылка системного журнала Journald на удаленную
   машину <https://fedoraproject.org/wiki/Changes/Remote_Journal_Logging>`__,
   как это было давно реализовано в syslog.

-  *`Удаление виртуальной "Provides: python-setuptools-devel" и
   соответствующих BuildRequires/Requires из
   rpm-пакетов <https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel>`__.*
-  `Обновление Review Board до версии
   2.0 <https://fedoraproject.org/wiki/Changes/ReviewBoard2>`__.

-  *`RPM 4.12 <https://fedoraproject.org/wiki/Changes/RPM-4.12>`__. Это
   очень серьезный апдейт - в нем, например, будут включены `"мягкие"
   зависимости </content/rpm-и-мягкие-зависимости>`__.*
-  `Ruby 1.9.3 и RoR 3.2.8 будут доступны в
   SCL <https://fedoraproject.org/wiki/Changes/Ruby193_in_SCL>`__ (см.

   ниже).

-  *`Обновление Ruby до версии
   2.1 <https://fedoraproject.org/wiki/Changes/Ruby_2.1>`__.*
-  *`Обновление Ruby on Rails до версии
   4.1 <https://fedoraproject.org/wiki/Changes/Ruby_on_Rails_4.1>`__*
-  Включение `Software
   Collections <https://fedoraproject.org/wiki/Changes/SCL>`__
-  `Перенесенная с Fedora 20 </content/Короткие-новости-18>`__ фича -
   `Переход KDE с KDM на
   SDDM <https://fedoraproject.org/wiki/Changes/SDDMinsteadOfKDM>`__.

-  Включение `Serf
   0.4.5 <https://fedoraproject.org/wiki/Changes/Serf_0.4.5>`__,
   написанного на Golang `децентрализованного оркестратора
   сервисов <http://www.serfdom.io/intro/vs-zookeeper.html>`__.

-  Включение `Shogun Machine Learning
   Toolbox <https://fedoraproject.org/wiki/Changes/shogun>`__.

-  `Облачные образы системы будут уменьшенного
   размера <https://fedoraproject.org/wiki/Changes/Smaller_Cloud_Image_Footprint>`__.

-  `В SSSD будет доступен GPO-Based Access
   Control <https://fedoraproject.org/wiki/Changes/SssdGpoBasedAccessControl>`__.

-  *`Поддержка конфигурационных файлов syslinux в
   U-boot <https://fedoraproject.org/wiki/Changes/u-boot_syslinux>`__.

   Традиционно, в ARM-системах, то, как надо загружать систему,
   `"хардкодилось" прямо в
   U-boot </content/Текущие-недостатки-архитектуры-arm>`__, что, само
   собой, неудобно для дистрибутивов общего пользования. Поэтому было
   принято решение вынести платформо-специфичные настройки в отдельный
   файл конфигурации, который будет создаваться Anaconda или самим
   пользователем, и который будет использоваться U-boot во время
   загрузки. Возможно в будущем перейдут на `спецификации для
   загрузчиков от
   FreeDesktop.org <http://www.freedesktop.org/wiki/Specifications/BootLoaderSpec/>`__,
   но пока будет вот так.*
-  `Использование RPM-макроса %license в пакетах, из которых собираются
   облачные
   образы <https://fedoraproject.org/wiki/Changes/Use_license_macro_in_RPMs_for_packages_in_Cloud_Image>`__.

   Это позволит удалять документацию на этапе сборки, но оставлять
   лицензионную информацию. Мы очень тщательно подходим к вопросам
   лицензирования. Однако стоит предупредить, что `старые версии RPM
   трактуют неизвестные им мкросы как
   ошибки </content/rpm-и-мягкие-зависимости>`__ (таковы были
   архитектурные решения того времени), так что не получится
   использовать один и тот-же SPEC-файл на Fedora и старых версиях RHEL,
   например.

-  `Запуск 64-битных ARM-машин на
   x86\_64-хостах <https://fedoraproject.org/wiki/Changes/Virt_64bit_ARM_on_x86>`__.

   Эти ARM-системы `собираются выпускать в
   РФ <http://www.kommersant.ru/doc/2493881>`__, так что интерес уже
   есть - нужно удовлетворять! К тому же практика такова, что ARM на
   эмуляции в x86\_64-хосте `работает быстрее, чем на нативном
   железе </content/Короткие-новости-про-основные-компоненты-системы-base-os>`__.

-  `Полная поддержка Wayland в
   GNOME <https://fedoraproject.org/wiki/Changes/Wayland>`__.

-  `Поддержка аутентификации Web-приложений на системном
   уровне <https://fedoraproject.org/wiki/Changes/Web_App_Authentication>`__,
   например с помощью плугинов Apache для SSSD.

-  Выделение специальной директории для `Web
   Assets <https://fedoraproject.org/wiki/Changes/Web_Assets>`__
   (CSS-файлы, JS-скрипты и т.п.). Также теперь мы будем стараться
   применять практику `"no bundled
   libs" </content/bundled-libraries-немного-статистики-и-комментариев-к-ней>`__
   ко всем JS-скриптам в системе.

-  *Долгожданный `X.org без прав
   суперпользователя <https://fedoraproject.org/wiki/Changes/XorgWithoutRootRights>`__.

   Эта фича стала возможно благодаря работе нашего коллеги, инженера Red
   Hat, `Hans de Goede <https://github.com/jwrdegoede>`__, о чем `вы уже
   могли слышать </content/xorg-без-привилегий-суперпользователя>`__.*
   Недавно Ханс похвалился, что `все уже
   готово <https://hansdegoede.livejournal.com/14446.html?nojs=1>`__.


| 

| |image0|
| **В этот раз релиз будет просто ошеломляющим!**

.. |image0| image:: https://lh3.googleusercontent.com/-UW6WlRj1dwI/U4xMKMBO3jI/AAAAAAAAInw/Vwjq_xPiqbs/Boypu1ICcAAISEF.jpg%253Alarge.jpg

