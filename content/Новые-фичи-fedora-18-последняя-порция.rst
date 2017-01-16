.. title: Новые "фичи" Fedora 18 (последняя порция)
.. slug: Новые-фичи-fedora-18-последняя-порция
.. date: 2012-07-24 10:17:57
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| На собрании FESCo
  `одобрили <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/167037>`__
  еще несколько фич будущей Fedora 18:

-  Одобрена отложенная в прошлый раз `интеграция GNOME и
   IBus <https://fedoraproject.org/wiki/Features/GNOMEIBusIntegration>`__.

-  `Преднастроенные профили
   сервисов <https://fedoraproject.org/wiki/Features/PackagePresets>`__
   и `система управления display
   manager'ми <https://fedoraproject.org/wiki/Features/DisplayManagerRework>`__,
   о которых `вы могли уже
   слышать </content/И-опять-новые-фичи-fedora-18>`__, также получили
   одобрение.

-  `Heat <https://fedoraproject.org/wiki/Features/Heat>`__, система для
   управлениями облачными приложениями в OpenStack. `Повышается степень
   участия Red Hat в
   OpenStack </content/Статистика-по-вкладу-компаний-в-разработку-openstack>`__.

-  `TeamDriver <https://fedoraproject.org/wiki/Features/TeamDriver>`__,
   способ соединять несколько физических сетевых карт в одно логическое
   устройство. Разработчики пишут, что функциональность аналогична
   `bonding <http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding>`__,
   но подход к реализации иной. В общем посмотрим, что это такое.

-  Обновление IPython `до версии
   0.13 <https://fedoraproject.org/wiki/Features/IPython_0.13>`__.

-  В третий раз одобряют
   `Riak <https://fedoraproject.org/wiki/Features/Riak>`__ (в этот раз
   `уже совсем мало осталось
   сделать <https://bugzilla.redhat.com/showdependencytree.cgi?id=652682&hide_resolved=0>`__).

-  Одобрили широкое внедрение `фильтрования системных
   вызовов <https://fedoraproject.org/wiki/Features/Syscall_Filters>`__
   (одним из `его первых пользователей будет
   systemd </content/systemd-и-seccomp>`__).

-  Загрузка при включенном
   `SecureBoot <https://fedoraproject.org/wiki/Features/SecureBoot>`__
   одобрена, как фича. Теперь это официально. Мы сделали все, что могли,
   и лучше варианта нет.

-  `Avahi по умолчанию будет
   включен <https://fedoraproject.org/wiki/Features/AvahiDefaultOnDesktop>`__.

   Уже довольно много ПО может работать лучше, если есть Avahi, а с
   недавних пор он `требуется и CUPS для автоопределения сетевых
   принтеров </cups-160>`__, так что удивительно лишь то, что его не
   включили раньше.

-  Две фичи, улучшающие ситуацию с виртуализацией - `поддержка
   Suspend/Hibernate в
   virtio <https://fedoraproject.org/wiki/Features/Virt_Guest_Suspend_Hibernate>`__
   и `снапшоты запущенной гостевой системы без
   остановки <https://fedoraproject.org/wiki/Features/Virt_Live_Snapshots>`__.

-  Включение `autohinting в fontconfig и
   FreeType <https://fedoraproject.org/wiki/Features/FontconfigEnableAutohinting>`__.

   Это теоретически улучшит ситуацию с отображением шрифтов.

-  `Обновление шрифтов Liberation до версии
   2 <https://fedoraproject.org/wiki/Features/Liberation_Fonts_2>`__.

-  `System Storage
   Manager <https://fedoraproject.org/wiki/Features/SystemStorageManager>`__
   - утилита или набор утилит для упрощения процесса управления сложными
   системами хранения (LVM, DM, MD).

-  Переход на
   `firewalld <https://fedoraproject.org/wiki/Features/firewalld-default>`__
   - динамически конфигурируемый файервол для Linux, управляемый через
   D-BUS. Это позволит полностью отказаться от iptables, ip6tables,
   ebtables.


| 
| Это последний раз, когда одобряются новые фичи для этой версии - окно
  закрыто, больше заявки на Fedora 18 не принимаются.

