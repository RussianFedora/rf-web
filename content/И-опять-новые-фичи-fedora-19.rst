.. title: И опять - новые "фичи" Fedora 19
.. slug: И-опять-новые-фичи-fedora-19
.. date: 2013-01-31 14:17:01
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Вновь пополнение списка одобренных фич грядущей Fedora 19, которых,
  кстати, `уже немало </content/Новые-фичи-fedora-19>`__:

-  `Включение
   CRIU <https://fedoraproject.org/wiki/Features/Checkpoint_Restore>`__,
   `разработки наших друзей из Parallels <http://criu.org/Main_Page>`__,
   которая позволяет сохранять состояние процессов и потом
   восстанавливать их. Мы надеемся, что технология найдет применение в
   таких важных частях системы, как systemd и RPM/Yum.

-  `Обновление GCC до версии
   4.8 <https://fedoraproject.org/wiki/Features/GCC48>`__. Тестовая
   пересборка уже была проведена, и по ее итогам, `как
   обычно </content/gcc-470>`__, не собралось чуть меньше 10% пакетов.

   Кстати, а дистрибутивы, которые хвалятся большими репозиториями,
   производят регулярные пересборки?
-  `Обновление Guile до версии
   2.0.7 <https://fedoraproject.org/wiki/Features/Guile2>`__.

-  `Включение во FreeIPA модели доверительных отношений Active
   Directory <https://fedoraproject.org/wiki/Features/IPAv3TrustImprovements>`__.

   Эту фичу предложил наш (бывший) соотечественник, инженер Red Hat,
   `Alexander
   Bokovoy <https://plus.google.com/117200318980623167325/about>`__.

-  `Техническое демо Java
   8 <https://fedoraproject.org/wiki/Features/Java8TechPreview>`__.

   Выход новой версии расчитан на сентябрь 2013 года, но вы уже сможете
   попробовать ее в Fedora (если, конечно, не задержатся с релизом на
   квартал-полгодика).

-  Замена нынешнего менеджера экранов KDE на
   `KScreen <https://fedoraproject.org/wiki/Features/KScreen>`__.

   Подключать и отключать дисплеи в KDE будет еще легче.

-  `MEMSTOMP <https://fedoraproject.org/wiki/Features/MEMSTOMP>`__ -
   инструмент (библиотека, которую можно загрузить с помощью
   LD\_PRELOAD), позволяющий найти перекрывающиеся участки памяти. Это
   позволит обнаружить ошибки, подобные `известной проблеме с
   memcpy/memmove в проприетарном
   flash-плугине <https://bugzilla.redhat.com/638477>`__, и обойдется
   дешевле (и будет проще), чем более мощное средство, такое, как
   valgrind.

-  `Включение
   NFSTest <https://fedoraproject.org/wiki/Features/NFStest>`__,
   средства тестирования NFS-серверов и клиентов, в т.ч. и
   `pNFS <http://www.pnfs.com/>`__.

-  Несколько раз откладывавшаяся фича - `включение
   Ns3 <https://fedoraproject.org/wiki/Features/Ns3>`__, симулятора
   сетей (интернет и интранет, мобильные сети, и т.п.), предназначенного
   для научных экспериментов.

-  `Обновление OpenStack до следующей
   версии <https://fedoraproject.org/wiki/Features/OpenStack_Grizzly>`__
   с кодовым именем "Grizzly".
-  `Замена MySQL на
   MariaDB <https://fedoraproject.org/wiki/Features/ReplaceMySQLwithMariaDB>`__.

   К сожалению, у Oracle плохие отношения с OpenSource сообществом, и
   практика показывает, что использование даже их якобы открытых и
   свободных технологий может вызвать серьезные проблемы, как `у крупных
   компаний <http://en.wikipedia.org/wiki/Oracle_v._Google>`__, так и `у
   простых
   разработчиков <http://www.h-online.com/open/news/item/VMware-stakes-IP-claim-on-Vert-x-1779548.html>`__.

   Конкретно в этом случае, к огромным организационно-юридическим
   выгодам от отказа от очередного продукта Oracle, еще и прилагаются
   некоторые технические бонусы.

-  `Обновление Ruby до версии
   2.0.0 <https://fedoraproject.org/wiki/Features/Ruby_2.0.0>`__.

-  `Включение Ruy <https://fedoraproject.org/wiki/Features/Ryu>`__,
   сетевой операционной системы, предназначенной для
   программно-конфигурируемых сетей (например, для OpenStack). Она
   использует OpenFlow, т.е. является контроллером OpenFlow.

-  `Scratch <https://fedoraproject.org/wiki/Features/Scratch>`__,
   графическая программная среда для создания игр и мультфильмов,
   предназначенная для школьников, будет включена в Fedora.

-  Очень интересная, и наверное сильно запоздавшая фича - `общее
   хранилище
   SSL/TLS-сертификатов <https://fedoraproject.org/wiki/Features/SharedSystemCertificates>`__.

   Сейчая Java, NSS, OpenSSL и все прочие приложения хранят и используют
   сертификаты независимо друг от друга. Проблемы с таким подходом
   довольно очевидны. Это - следующий (хотя, повторимся, сильно
   запоздавший) шаг по реализации более амбициозного плана - `Fedora
   Crypto
   Consolidation <http://fedoraproject.org/wiki/FedoraCryptoConsolidation>`__,
   полная реализация которого наконец-то позволит Linux-системам по
   удобству управления сертификатами безопасности догнать проприетарные
   операционные системы, такие как Windows и Mac OS X.
-  `SSSD будет более лучше интегрирован в Active
   Directory <https://fedoraproject.org/wiki/Features/SSSDImproveADIntegration>`__.

-  Будет доступен еще один вариант загрузки - `с помощью
   syslinux <https://fedoraproject.org/wiki/Features/SyslinuxOption>`__,
   вместо использующегося по умолчанию GRUB2 или нескольких
   UEFI-загрузчиков. Как считается некоторыми участниками Fedora,
   syslinux менее требователен к ресурсам и более прост в
   конфигурировании, что может сделать его предпочтительнее в ряде
   случаев, чем GRUB2.

-  `Очередной раунд переименований сетевых
   интерфейсов <https://fedoraproject.org/wiki/Features/SystemdPredictableNetworkInterfaceNames>`__.

   Прорвемся!

| 
| На подходе еще с пару десятков предложенных нововведений, так что
  ждите. А пока посмотрите на график количества анонсированных фич в
  зависимости от версии Fedora:

|image0|

| 
| Некоторые уже сделали беспочвенные ревизионистские заявления, что
  качество Fedora обратно пропорционально количеству анонсированных фич.

  Мы, разумеется, несогласны с ними - мы уверены, что Fedora не только
  постоянно хороша, но и становится лучше от релиза к релизу.

  Присоединяйтесь!

.. |image0| image:: http://peter.fedorapeople.org/stuff/fedora_features.png

