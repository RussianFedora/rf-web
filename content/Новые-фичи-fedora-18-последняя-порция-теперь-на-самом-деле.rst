.. title: Новые "фичи" Fedora 18 (последняя порция - теперь на самом деле)
.. slug: Новые-фичи-fedora-18-последняя-порция-теперь-на-самом-деле
.. date: 2012-07-31 09:29:17
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Несмотря на то, что в `прошлое собрание
  FESCo </content/Новые-фичи-fedora-18-последняя-порция>`__ было
  объявлено, что больше новых фич принимать не будут, в самый последний
  день, практически после собрания, было поставлено на рассмотрение
  FESCo с дюжину новых заявок. Пришлось провести еще один раунд
  обсуждений, `благодаря
  которому <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/167315/focus=167335>`__
  успели запрыгнуть в вагон следующие фичи:

-  `Samba 4.0 <https://fedoraproject.org/wiki/Features/Samba4>`__,
   поддерживающая новую версию протокола SMB и работающая с FreeIPA.

   Подробнее может рассказать участник Samba и инженер Red Hat,
   `Александр Боковой <http://abbra.dreamwidth.org/>`__, который со
   своими коллегами и занимался соединением Samba и FreeIPA.

-  Планируется включить
   `MATE <https://fedoraproject.org/wiki/Features/MATE-Desktop>`__ -
   форк Gnome 2. Несмотря на значительный объем работы, успех
   `Cinnamon </content/cinnamon-доступен-в-fedora>`__ окрылил
   добровольцев. Ситуацию с поддержкой MATE облегчает то, что в RHEL 6
   включен Gnome 2, а это значит, что редхатовцы будут предоставлять
   исправления к нему еще несколько лет - коммьюнити вокруг MATE просто
   будет должно аккуратно подбирать патчи.

-  `Обновление oVirt до версии
   3.1 <https://fedoraproject.org/wiki/Features/oVirtEngine_3.1>`__.

-  `Обновление обучающей среды Sugar до версии
   0.98 <https://fedoraproject.org/wiki/Features/Sugar_0.98>`__.

-  Включение нового трассировщика для Linux - `LTTng
   2.0 <https://fedoraproject.org/wiki/Features/LTTng>`__.

-  Включение
   `ownCloud <https://fedoraproject.org/wiki/Features/OwnCloud>`__,
   персонального облачного решения. Теперь будет можно делать свое
   маленькое облачко.

-  Продолжится работа над изменением системы печати - встречайте `Print
   Service <https://fedoraproject.org/wiki/Features/PrintService>`__,
   апплет Gnome, объединяющий доступ к принтерам IPP, к Google Cloud
   Print, HP ePrint и упрощающий их настройку.

-  Продолжается интеграция systemd и SELinux. Теперь `systemd будет
   проверять, есть ли у приложения возможность запускать и останавливать
   другие
   приложения <https://fedoraproject.org/wiki/Features/SELinuxSystemdAccessControl>`__,
   как это было реализовано в SysVinit-скриптах с помощью специальных
   меток SELinux.

-  `Александр Боковой <http://abbra.dreamwidth.org/>`__ с коллегами еще
   планируют представить `новую версию
   IPA <https://fedoraproject.org/wiki/Features/IPAv3Trusts>`__, с более
   тесной интеграцией с Active Domains.

-  `Обновление Python до версии
   3.3 <https://fedoraproject.org/wiki/Features/Python_3.3>`__.

-  `Federated File System
   (FedFS) <https://fedoraproject.org/wiki/Features/FedFS>`__,
   реализация `RFC 5716 <http://tools.ietf.org/html/rfc5716>`__ для
   NFSv4 (пока - планируют расширить и на Samba). Грубо говоря, это
   современный automount для сетевых файловых систем.

-  `Включение видеодрайверов с
   KMS <https://fedoraproject.org/wiki/Features/ServerKMSDrivers>`__ для
   серверных систем, `о которых мы уже
   писали </content/Новые-видеодрайверы-c-поддержкой-kms-для-старых-видеокарт>`__.

-  `LLVM для платформы
   PPC64 <https://fedoraproject.org/wiki/Features/LLVMonPPC64>`__, что
   нужно для другой фичи - `поддержка LLVMpipe в VNCServer на платформе
   PPC64 <https://fedoraproject.org/wiki/Features/VNCServerWithLLVMpipe>`__.

-  `Обновление Systemtap до версии
   2.0 <https://fedoraproject.org/wiki/Features/Systemtap2>`__
-  `NFSometer <https://fedoraproject.org/wiki/Features/NFSometer>`__ -
   фреймворк для тестирования производительности и пропускной
   способности NFS-сервисов.

-  `QXL/Spice видеодрайвер с поддержкой
   KMS <https://fedoraproject.org/wiki/Features/QXLKMSSupport>`__.


| 
| Отложили принятие решения по предложенной инженером Dell фиче -
  `Agent-Free
  Management <https://fedoraproject.org/wiki/Features/AgentFreeManagement>`__
  (управление и мониторинг ресурсами системы без установки
  дополнительных сервисов). Понятно, что это означает, лишь то, что
  сервисы будут предустановлены заранее, и наличие очередной пачки
  демонов, запущенных по умолчанию, может вызвать неконтролируемые
  вспышки ярости у пользователей ноутбуков (например).

| Вот теперь все.

