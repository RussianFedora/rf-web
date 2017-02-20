.. title: Одобрено еще несколько новых "фич" Fedora 17
.. slug: одобрено-еще-несколько-новых-фич-fedora-17
.. date: 2012-01-24 12:54:49
.. tags:
.. category: Fedora Changes
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


На прошедшем 23 января 2012 года собрании FESCo
`одобрили <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/158410/focus=158434>`__
ряд новых фич Fedora 17, и в этот раз их список очень внушителен:

-  `Включение
   DIET <https://fedoraproject.org/wiki/Features/F17_DIET>`__, открытого
   решения для высокопроизводительных вычислений
-  `Переработка способа создания
   LiveCD <https://fedoraproject.org/wiki/Anaconda/Features/ReworkLiveCD>`__,
   с целью унификации установщиков и методов установки/сборки, которых
   уже несколько штук
-  `Сервис дедупликации backtrace'ов в
   ABRT <https://fedoraproject.org/wiki/Features/ABRTBacktraceDeduplication>`__.

   Сейчас почти на каждый бэктрейс от ABRT открывается новая заявка в
   Bugzilla, которые затем приходится объединять вручную. В рамках этой
   "фичи" будет предпринята попытка автоматизации этого довольно нудного
   процесса.

-  `Утилита конфигурации
   шрифтов <https://fedoraproject.org/wiki/Features/FontConfigurationTool>`__,
   в зависимости от языка. Сейчас для этого требуется знать, как
   настраивается fontconfig.

-  `Сервис автодополнения английских
   слов <https://fedoraproject.org/wiki/Features/english-typing-booster>`__.

   Это, скорее всего, нужно для того, чтоб в сети появлялись `смешные
   гифки с ошибками autocomplete не только с
   iPhone <http://damnyouautocorrect.com/>`__, но и с Fedora, что
   поможет популяризировать дистрибутив.

-  `Обновление Eclipce до версии
   Juno <https://fedoraproject.org/wiki/Features/EclipseJuno>`__
-  `Включение в дистрибутив языка
   Opa <https://fedoraproject.org/wiki/Features/Opa09>`__. Это язык,
   `предназначенный для облачных вычислений <http://opalang.org/>`__.

-  `Очередные новые индийские
   языки <http://fedoraproject.org/wiki/Features/Additional_Indic_Langs>`__.

-  `DNSSEC на
   десктопах <https://fedoraproject.org/wiki/Features/DNSSEC_on_workstations>`__.

   Это следующий этап перехода дистрибутива на DNSSEC.

-  `Поддержка файловых систем EXT4 более 16
   терабайт <https://fedoraproject.org/wiki/Features/F17Ext4Above16T>`__,
   что уже совсем нефантастично звучит в наши дни
-  `Обновление Haskell Platform до версии
   2011.4 <https://fedoraproject.org/wiki/Features/HaskellPlatform2011.4>`__.

   Чуть ранее уже была одобрена фича, в рамках которой будет произведено
   `обновление Glasgow Haskell Compiler до
   7.4.1 <https://fedoraproject.org/wiki/Features/GHC74>`__
-  `Обновление IPA до версии
   3 <https://fedoraproject.org/wiki/Features/IPAv3NewFeatures>`__
-  `Обновление OpenJDK до версии
   7 <https://fedoraproject.org/wiki/Features/Java7>`__
-  `Обновление mkdumprd для
   kexec-tools <https://fedoraproject.org/wiki/Features/NewMkdumprd>`__.

   Теперь оно будет использовать dracut.

-  `Включение
   virt-sandbox <https://fedoraproject.org/wiki/Features/VirtSandbox>`__,
   `позволяющего организовать выполнение произвольных пользовательских
   приложений в изолированном окружении, построенном с использованием
   libvirt <http://www.opennet.ru/opennews/art.shtml?num=32847>`__.

-  `Включение Non-Uniform Memory Alignment Daemon в
   дистрибутив <https://fedoraproject.org/wiki/Features/numad>`__
-  `Включение
   Quantum <https://fedoraproject.org/wiki/Features/OpenStack_Quantum>`__,
   виртуального сервиса сети, предназначенного, в основном, для системы
   облачных вычислений OpenStack.

-  `RabbitMQ как middleware bus для проекта
   OpenStack <https://fedoraproject.org/wiki/Features/OpenStack_using_Qpid>`__.

-  `Обновление Ruby до версии
   1.9.3 <https://fedoraproject.org/wiki/Features/Ruby_1.9.3>`__
-  `Включение новой возможности
   SELinux <https://fedoraproject.org/wiki/Features/SELinuxDenyPtrace>`__
   - запрет на трассировку приложением другого процесса
-  `Запуск некоторых приложений с их собственной временной
   директорией <https://fedoraproject.org/wiki/Features/ServicesPrivateTmp>`__
   вместо общего пространства в /tmp .
-  `Включение
   Wallaby <https://fedoraproject.org/wiki/Features/Wallaby>`__,
   программируемого семантического сервиса конфигураций для HPC системы
   Condor.


Помимо этих фич, на рассмотрение уже поданы `новые
заявки <https://fedoraproject.org/wiki/Category:FeatureReadyForWrangler>`__.

