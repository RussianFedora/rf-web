.. title: Новые "фичи" Fedora 19
.. slug: Новые-фичи-fedora-19-0
.. date: 2013-02-11 16:21:15
.. tags: erlang, voip, gnome, systemd, networkmanager, clouds, gcc, virtualization
.. category: Fedora Changes
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Вновь анонсированы новшества будущей Fedora 19 (предыдущие анонсы - `раз
</content/И-опять-новые-фичи-fedora-19>`__, `два
</content/Новые-фичи-fedora-19>`__, `три
</content/Начали-принимать-фичи-в-fedora-19>`__). На последнем собрании FESCo
одобрили следующее:

- Дальнейшие улучшения в `новом интерфейсе Anaconda
  <https://fedoraproject.org/wiki/Features/AnacondaNewUI_Followup>`__ (мы тоже
  можем менять местами кнопки и изменять размеры элементов UI).

- `Интеграция Anaconda и realmd
  <https://fedoraproject.org/wiki/Features/AnacondaRealmIntegration>`__, что
  позволит при установке подключаться к AD и FreeIPA доменам.

- Вызвавшая споры фича - `возвращение Apache OpenOffice в репозитории Fedora
  <https://fedoraproject.org/wiki/Features/ApacheOpenOffice>`__. Работу взялся
  провести участник OpenOffice.org с 10-летним стажем, `Andrea Pescetti
  <http://www.pescetti.it/andrea/>`__.

- `Улучшенная поддержка IPSec в NetworkManager
  <https://fedoraproject.org/wiki/Features/BetterNetworkManagerIPSecIntegration>`__.

- `Обновление CUPS до версии 1.6
  <https://fedoraproject.org/wiki/Features/CUPS1.6>`__. Мы уже `рассказывали об
  этой версии </content/cups-160>`__.

- Довольно странная фича - `помощник разработчика
  <https://fedoraproject.org/wiki/Features/DevelopersAssistant>`__.

  Несмотря на название, это всего-лишь некоторое количество мета-пакетов,
  которые будут содержать в своих зависимостях полезные для разработчиков
  приложения (и, порой, простенькие скрипты для первичной настройки). Наверное
  это будет интересно начинающим.

- Интересная фича - `создание минимальной initramfs для загрузки на конкретной
  машине <https://fedoraproject.org/wiki/Features/DracutHostOnly>`__.

  Сейчас initramfs содержит набор модулей и компонент, позволяющий загрузиться
  на произвольной конфигурации, что не всегда нужно.

  Пользователи, вместо самосборных "писюков" (где от загрузки к загрузке может
  измениться, например, материнская плата), предпочитают "монолитные" машины
  (ноутбуки различных производителей, компьютеры Apple, и т.п., где максимум,
  что можно сделать, это нарастить память и заменить USB-клавиатуру), и им уже
  не так интересно иметь возможность вырвать винчестер, переставить на
  совершенно другой компьютер и успешно загрузиться. Теперь время загрузки и
  пересборки initramfs при обновлении ядра важнее.

- `Обновление Erlang до версии R16
  <https://fedoraproject.org/wiki/Features/Erlang_R16>`__. В этой версии
  отказались от параметризованных модулей, что потребует внесения изменений в
  ряд библиотек и приложений, среди которых mochiweb (уже исправлено), Wings и
  возможно другие.

- Очень интересная фича от `Daniel Pocock <https://github.com/dpocock>`__,
  участника Debian и разработчика reSIProcate, `Federated VoIP
  <https://fedoraproject.org/wiki/Features/FederatedVoIP>`__, целью которой
  является упрощение развертывания на базе Fedora узла интегрированной
  распределенной VoIP-сети, использующей открытые SIP- и XMPP-компоненты.

- `Язык правил для firewalld
  <https://fedoraproject.org/wiki/Features/FirewalldRichLanguage>`__.

- `Официальные образы Fedora для развертывания в облачных сервисах
  <https://fedoraproject.org/wiki/Features/FirstClassCloudImages>`__. Сейчас
  Fedora поставляется лишь в виде ISO-образов для установки, а планируется с
  каждым релизом (альфа, бета, TC и финальным релизом) поставлять также
  официальные образы, пригодные для моментального развертывания узла в облаках.
  Это потребует внесение ряда изменения в инфраструктуру проекта, но дело
  стоящее.

- `Обновление GLIBC до версии 2.17
  <https://fedoraproject.org/wiki/Features/GLIBC217>`__.

- `Обновление GNOME до версии 3.8
  <https://fedoraproject.org/wiki/Features/Gnome3.8>`__. Добавить особо нечего
  - все увидите сами!

- Замена rpc.svcgssd на `gss-proxy
  <https://fedoraproject.org/wiki/Features/gss-proxy>`__, что позволит
  использовать общий сервис во всех приложениях, не только NFS-, но и
  CIFS-сервисах.

- `High Availability Container Resources
  <https://fedoraproject.org/wiki/Features/High_Availability_Container_Resources>`__-
  Pacemaker будет иметь возможность управлять не только ресурсами на физических
  машинах, но и ресурсами в виртуальных машинах, запущенных на физических
  серверах.

- `Обновление JRuby до версии 1.7
  <https://fedoraproject.org/wiki/Features/JRuby_1.7>`__.

- `Обновление KDE до версии 4.10
  <https://fedoraproject.org/wiki/Features/KDE410>`__.

- Замена ibus-anthy и ibus-mozc, подсистем для ввода японских алфавитов, на
  ibus-kkc, построенную на базе `libkkc
  <https://fedoraproject.org/wiki/Features/libkkc>`__.

- `Обновление MATE (форк GNOME 2) до версии 1.6
  <https://fedoraproject.org/wiki/Features/MATE-Desktop-1.6>`__. В этой версии
  планируется замена ряда компонентов на аналоги из GNOME 3, что упростит
  поддержку Desktop Environment.

- `Пересборка MinGW с GCC 4.8
  <https://fedoraproject.org/wiki/Features/MinGW_GCC_4.8>`__. В рамках этого
  изменения будет произведена полная пересборка новой версией компилятора всего
  списка приложений и библиотек для MinGW, в полном соответствии с правилами
  Fedora.

- `Обновление ModemManager до версии 0.7 или 0.8
  <https://fedoraproject.org/wiki/Features/MoreMobileBroadband>`__, в которых
  будет реализована более полная поддержка стандартов и протоколов 2G/3G/4G, в
  т.ч. и проприетарных.

- `Поддержка multiqueue в VirtIO
  <https://fedoraproject.org/wiki/Features/MQ_virtio_net>`__, как на стороне
  хоста, так и в драйверах гостевой машины. Чем это выгодно вы можете почитать
  на `странице разработчиков <http://www.linux-kvm.org/page/Multiqueue>`__,
  которые и займутся этой фичей в Fedora.

- `Лучшая поддержка bonding в NetworkManager
  <https://fedoraproject.org/wiki/Features/NetworkManagerBonding>`__, в т.ч.
  обнаружение уже существующих конфигураций, созданных, например, libvirt.

- `Лучшая поддержка bridging в NetworkManager
  <https://fedoraproject.org/wiki/Features/NetworkManagerBridging>`__, и
  аналогично предыдущей фиче - в т.ч. обнаружение уже существующих
  конфигураций, созданных, например, libvirt.

- После изменений дизайна Anaconda нам представят `измененный дизайн firstboot
  <https://fedoraproject.org/wiki/Features/NewFirstboot>`__, программы,
  производящей начальную настройку системы после установки.

- Включение `OpenAttestation
  <https://fedoraproject.org/wiki/Features/OpenAttestation>`__, что позволит
  реализовать поддержку `Trusted Computing Pools
  <http://wiki.openstack.org/TrustedComputingPools>`__ в OpenStack и в будущей
  версии oVirt.

- `Упрощения в настройке и использовании OpenLMI
  <https://fedoraproject.org/wiki/Features/OpenLMIEaseOfUse>`__, системы для
  управления Linux-машинами. О ней можно прочитать на `сайте разработчиков
  <https://fedorahosted.org/openlmi/>`__.

- Фича, перенесенная с Fedora 18 - `включение OpenShift Origin
  <https://fedoraproject.org/wiki/Features/OpenShift_Origin>`__, PaaS-платформы
  от Red Hat. Ее не успели включить в Fedora 18 из-за большого количества
  зависимых Ruby-пакетов.

- `Обновление oVirt Engine до версии 3.2
  <https://fedoraproject.org/wiki/Features/oVirtEngine_3.2>`__.

- `Обновление Performance Co-Pilot до еще невыпущенной версии 4
  <https://fedoraproject.org/wiki/Features/Pcp4>`__.

- `Упрощенное развертывание Pacemaker/Corosync
  <https://fedoraproject.org/wiki/Features/Pcsd_Configuration_Wizards>`__. Эта
  фича позволит легко и просто настроить Pacemaker/Corosync для типичных
  сценариев.

- Дальнейшее развитие PreUpgrade - `PreUpgrade Assistant
  <https://fedoraproject.org/wiki/Features/PreUpgrade_Assistant>`__,
  инструмент, позволящий пользователям не только обновляться, но и не потерять
  внесенные пользователем изменения в конфигурацию, если их невозможно
  перенести средствами PreUpgrade/yum/rpm.

- `Поддержка FreeIPA в realmd
  <https://fedoraproject.org/wiki/Features/RealmdFreeIpaSupport>`__.

- Фича, интересная в основном мэйнтейнерам Java-пакетов - `упрощение сборки
  RPM-пакетов с Maven
  <https://fedoraproject.org/wiki/Features/Simplified_Maven_Packaging>`__.
  Обычные пользователи увидят это лишь опосредованно, в виде улучшения качества
  RPM-пакетов c Java-библиотеками и приложениями.

- `Включение полноценного аналога cron в systemd
  <https://fedoraproject.org/wiki/Features/SystemdCalendarTimers>`__.

- `Включение легковесных контейнеров в systemd
  <https://fedoraproject.org/wiki/Features/SystemdLightweightContainers>`__.
  Благодаря этой фиче будет очень просто запустить Fedora внутри уже запущенной
  Fedora. Т.е. это такая современная и более развитая версия chroot.

- Сделан еще один шаг к улучшению машиночитаемости системного журнала событий -
  теперь `сообщения будут иметь номера
  <https://fedoraproject.org/wiki/Features/SystemdMessageCatalog>`__.

  Например, вместо текстового сообщения "приложение совершило недопустимую
  операцию и будет закрыто", вам будет выдаваться простой и понятный
  идентификатор - скажем, "ORA-01033", с которым уже можно что-то делать. По
  нему можно создавать локализованные сообщения об ошибках, его можно будет
  погуглить невзирая на локаль пользователя, можно будет легко вести
  статистику.

- `Улучшено управление ресурсами сервисов в systemd
  <https://fedoraproject.org/wiki/Features/SystemdResourceControl>`__. Теперь
  можно будет наживую менять ограничения для запущенных сервисов.

- `Обновление systemtap до версии 2.2
  <https://fedoraproject.org/wiki/Features/Systemtap22>`__.

- `Обновление Thermostat, средства для мониторинга Java-приложений, до версии
  1.0 <https://fedoraproject.org/wiki/Features/Thermostat1.0>`__.

- `Включение системы Trusted Network Connect
  <https://fedoraproject.org/wiki/Features/Trusted_Network_Connect_(TNC)>`__.

- `Поддержка системы снапшотов в Yum на базе LVM2
  <https://fedoraproject.org/wiki/Features/YumFsSnapshotThinpSupport>`__. Это -
  первый шаг к полностью транзакционным обновлениям пакетов. Конечно,
  потребуется еще и интеграция с `CRIU
  <https://fedoraproject.org/wiki/Features/Checkpoint_Restore>`__, но начало
  положено.

- Планируется `изменение в yum, позволящее ему рассматривать группы, также, как
  и обычные пакеты
  <https://fedoraproject.org/wiki/Features/YumGroupsAsObjects>`__.  Т.е. вместо
  *sudo yum group install kde-desktop* можно будет просто скомандовать *sudo
  yum install kde-desktop*.

На подходе еще несколько фич, но возможно их уже перенесут в Fedora 20.

Отказались одобрить фичу `по замене десктопа по умолчанию в GNOME 3 на Cinnamon
<https://fedoraproject.org/wiki/Features/Cinnamon_as_Default_Desktop>`__.

