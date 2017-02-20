.. title: Дисковый массив с Ceph от Western Digital 
.. slug: Дисковый-массив-с-ceph-от-western-digital
.. date: 2016-04-29 14:23:05
.. tags: western digital, ceph, redhat, posix, xfs, 
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`WD Labs анонсировали дисковый
массив <http://ceph.com/community/500-osd-ceph-cluster/>`__ из
специальных дисков своего производства, у которых обычный
микроконтроллер заменен на ARM-микрокомпьютер с Linux (к сожалению, был
выбран Debian). Вместо стандартных SATA-интерфейсов там два гигабитных
ethernet-адаптера, объединенные физически в коннектор, аналогичный SATA,
который будут использовать и другие производители.

|WaspV3\_PCBA-1|
|Wasp-8TB-Top-Bot|

Такие вот "умные" 8-терабайтные диски собираются по 500 в стандартную
стойку от SuperMicro, и образуют 4-петабайтный массив с возможностью
отдачи данных до 10-гигабит/c.

|Front view - 25 new enclosures-small|

Внутри используется Ceph, и весь массив проектировался с помощью
инженеров Red Hat, чьим подразделением и является компания Inktank,
`купленная Red Hat пару лет
назад </content/red-hat-покупает-компанию-inktank>`__. В новости очень
важно отметить, что наверное впервые в продакшене используется Ceph с
новым бэкендом для прямого доступа к диску,
`BlueStore <http://www.sebastien-han.fr/blog/2016/03/21/ceph-a-new-store-is-coming/>`__.

Бэкенд
`презентовали <https://vault2016.sched.org/event/68kb/bluestore-a-new-faster-storage-backend-for-ceph-sage-weil-red-hat>`__
наши коллеги на недавно прошедшей `Vault
2016 <https://vault2016.sched.org/>`__. До этого использовался бэкенд
FIleStore, который использовал файловые системы (XFS или `для
смелых </content/scylladb-доросла-до-версии-10>`__ btrfs), но
`распределенная файловая система быстро упирается в юниксвэйные
ограничения стандарта
POSIX </content/Вышел-openstack-kilo-и-другие-новости>`__.

Конечно, все это не значит, что XFS стала вдруг плохой. Те, кому
требуется POSIX-система, например в `LMAX <https://www.lmax.com/>`__,
`выбирают именно
XFS <http://epickrram.blogspot.com/2015/12/journalling-revisited.html>`__,
а не, например, ext4. Последняя годится для rootfs, ну еще для
чего-нибудь. А если нужно высоконагруженное и надежное решение, то выбор
однозначен - продукт 22 лет разработки, XFS.


.. |WaspV3\_PCBA-1| image:: http://ceph.com/wp-content/uploads/2016/04/WaspV3_PCBA-1-293x220.jpg
   :width: 293px
   :height: 220px
   :target: http://ceph.com/wp-content/uploads/2016/04/WaspV3_PCBA-1.jpg
.. |Wasp-8TB-Top-Bot| image:: http://ceph.com/wp-content/uploads/2016/04/Wasp-8TB-Top-Bot-460x173.jpg
   :width: 520px
   :height: 195px
   :target: http://ceph.com/wp-content/uploads/2016/04/Wasp-8TB-Top-Bot.jpg
.. |Front view - 25 new enclosures-small| image:: http://ceph.com/wp-content/uploads/2016/04/Front-view-25-new-enclosures-small-e1461351200861-225x300.jpg
   :width: 225px
   :height: 300px
   :target: http://ceph.com/wp-content/uploads/2016/04/Front-view-25-new-enclosures-small.jpg
