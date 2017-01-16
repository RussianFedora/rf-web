.. title: Новые фичи Fedora на подходе
.. slug: Новые-фичи-fedora-на-подходе
.. date: 2014-03-27 10:52:01
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Анонсирован ряд новых фич Fedora:

-  Включение в репозиторий `Amplab
   Tachyon <https://fedoraproject.org/wiki/Changes/AmplabTachyon>`__,
   распределенной файловой системы. Эта работа проводится в рамках
   `Fedora BigData SIG <https://fedoraproject.org/wiki/SIGs/bigdata>`__.

-  Включение в репозиторий `Apache
   Mesos <https://fedoraproject.org/wiki/Changes/ApacheMesos>`__,
   система управления кластерами. Можно сказать, что это микроядро для
   кластерных систем. Также для `Fedora BigData
   SIG <https://fedoraproject.org/wiki/SIGs/bigdata>`__.

-  `Apache
   Spark <https://fedoraproject.org/wiki/Changes/ApacheSpark>`__, еще
   один кластерный компонент, предназначенный для обработки больших
   объемов данных.

-  `Улучшения в экосистеме
   Scala <https://fedoraproject.org/wiki/Changes/ImprovedScalaEcosystem>`__.

   Несмотря на то, что в Fedora формально Scala уже есть, пользоваться
   ей, без сторонних репозитариев, пока было сложно. В рамках этого
   изменения будет добавлен ряд отсутствующих компонентов.

-  `Перенесенная с Fedora 20 </content/И-опять-новые-фичи-fedora-20>`__
   фича - `поддержка DNSSEC в
   FreeIPA <https://fedoraproject.org/wiki/Changes/IPAv3DNSSEC>`__.

-  Очень серьезное изменение - `Java 8 по
   умолчанию <https://fedoraproject.org/wiki/Changes/Java8>`__.

-  Включение в репозиторий `NFS
   Ganesha <https://fedoraproject.org/wiki/Changes/NFSGanesha>`__,
   независимой реализации NFS-сервера, работающей в user-space. Работа
   будет проведена одним из upstream-разработчиков.

-  `PrivateDevices=yes и PrivateNetwork=yes для всех сервисов, которые
   предназначены для долговременной
   работы <https://fedoraproject.org/wiki/Changes/PrivateDevicesAndPrivateNetwork>`__.

   Это очередная фича systemd, которую мы начнем активно использовать.

   Идея в том, чтобы отобрать у сервисов, которым это не нужно, доступ к
   физическим устройствам (PrivateDevices=yes), или вообще доступ к сети
   (PrivateNetwork=yes). Такие ограничения резко снизят возможности
   злоумышленников.


| 
| Официально включение их в список состоится довольно скоро.

