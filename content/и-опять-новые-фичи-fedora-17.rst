.. title: И опять новые "фичи" Fedora 17
.. slug: и-опять-новые-фичи-fedora-17
.. date: 2012-02-01 00:42:25
.. tags: cups, cloudstack, eucaliptus, jboss, networkmanager, xen, openvswitch, openstack, qemu, firewalld
.. category: Fedora Changes
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

На собрании FESCo, прошедшем 30 января 2012 года, `были
одобрены <https://thread.gmane.org/gmane.linux.redhat.fedora.devel/158842/focus=158866>`__
новые "фичи" Fedora 17:

-  `Переработанные средства создания
   LiveCD <https://fedoraproject.org/wiki/Anaconda/Features/ReworkLiveCD>`__.

   Идея в том, чтоб унифицировать дальше различные способы установки
   системы, которые должны использовать Anaconda вместо кривеньких
   самодельных скриптов.

-  `Интеграция CUPS и
   colord <https://fedoraproject.org/wiki/Features/CUPS_colord_Support>`__,
   что позволит использовать ICC-таблицы принтеров на этапе растеризации
   изображения.

-  `Включение в дистрибутив
   Cloudstack <https://fedoraproject.org/wiki/Features/Cloudstack>`__,
   платформы IaaS.

-  `Обновление набора программ для облачных
   вычислений <https://fedoraproject.org/wiki/Features/Cluster>`__.

-  `Включение в дистрибутив
   Eucaliptus <https://fedoraproject.org/wiki/Features/Eucalyptus>`__,
   еще одной платформы для облачных вычислений

-  `Включение в дистрибутив JBoss Application Server
   7 <https://fedoraproject.org/wiki/Features/JBossAS7>`__, широко
   известного в узких кругах Java EE сервера приложений
-  `Улучшение
   NetworkManager <https://fedoraproject.org/wiki/Features/RealHotspot>`__,
   упрощающее создание на базе Fedora 17 хотспот-точек
-  `Улучшение
   NetworkManager <https://fedoraproject.org/wiki/Features/NMEnterpriseNetworking>`__,
   упрощающее предоставление на базе Fedora 17 сервисов масштаба
   предприятия - bonding, IP-over-Infiniband, VLAN и т.п.
-  `Включение библиотек и программ для Xen
   API <https://fedoraproject.org/wiki/Features/XAPI>`__, что позволит
   управлять системой виртуализации Xen в инсталляциях больших масштабов
-  `Включение Open
   vSwitch <https://fedoraproject.org/wiki/Features/Open_vSwitch>`__,
   сетевого свитча для виртуализированных окружений
-  `Улучшение управления
   электропитанием <https://fedoraproject.org/wiki/Features/PowerManagementF17>`__
-  `Обновление платформы для облачных вычислений OpenStack до версии
   "Essex" <https://fedoraproject.org/wiki/Features/OpenStack_Essex>`__
-  `Предоставление виртуализированного средства профилирования
   системы <https://fedoraproject.org/wiki/Features/KVM_Guest_PMU>`__.

   Благодаря нему в гостевых системах можно будет пользоваться
   стандартными средствами профилирования
-  `Предоставление возможности "живой" миграции блочных устройств
   KVM <https://fedoraproject.org/wiki/Features/KVM_Live_Block_Migration>`__.

   Это позволит на лету переключаться между форматами виртуальных
   дисков, мигрировать их между LUN не выключая систему и т.п.
-  `Улучшение экономного распределения в
   KVM <https://fedoraproject.org/wiki/Features/KVMThinProv>`__.

   Предлагается предоставить пользователю возможность на лету
   переключаться между "thin provisioning" и "thick provisioning" (в
   котором случае все ресурсы будут выделяться полностью) при работе с
   виртуальными образами систем.

-  `Провести статический анализ всего Python кода в
   Fedora <https://fedoraproject.org/wiki/Features/StaticAnalysisOfPythonRefcounts>`__.

   Пока предполагается автоматизировать нахождение ошибок счетчиков
   ссылок для модулей Python, написанных на C.
-  `Предоставление возможности разделения сетевых соединений по "зонам
   доверия" <https://fedoraproject.org/wiki/Features/network-zones>`__.

   Например, сетевой интерфейс, подключенный к неизвестной публичной
   сети попадает в недоверенную зону, а он-же, но подключенный через
   домашнюю WPA2-сеть - попадает в доверенные.

-  `Переход на firewalld, как на firewall по
   умолчанию. <https://fedoraproject.org/wiki/Features/firewalld-default>`__
-  `Включение в дистрибутив
   Darkserver <https://fedoraproject.org/wiki/Features/Darkserver>`__,
   сервиса для идентификации build-id по стэктрейсу.


Как всегда, участники Fedora демонстрируют, что им вполне по плечу
замахнуться на действительно непростые задачи, в рамках которых
происходит адаптация, включение в дистрибутив и предварительная
настройка крайне сложных приложений, в том числе и уровня предприятия.

Это в корне отличается от подхода многих других дистрибутивов, где
мэйнтейнеры максимум осиливают написание "рецепта" сборки приложения,
или тратят время на перекраску обоев и перенос кнопок из одного угла в
другой.
