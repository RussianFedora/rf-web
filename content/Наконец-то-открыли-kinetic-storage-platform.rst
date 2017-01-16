.. title: Наконец-то открыли Kinetic Storage Platform
.. slug: Наконец-то-открыли-kinetic-storage-platform
.. date: 2015-08-29 14:30:40
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Seagate, традиционный участник RICON,
`сдержал <http://www.linuxfoundation.org/news-media/announcements/2015/08/linux-foundation-brings-together-industry-leaders-advance-cloud>`__
свое обещание открыть исходный код Kinetic Storage Platform (они
пообещали сделать это на прошедшем OpenStack Summit, `о чем вы уже могли
слышать </content/Вышел-openstack-kilo-и-другие-новости>`__). В рамках
проекта будет развиваться платформа распределенного хранилища данных
(Software-defined Storage. К проекту уже присоединились Cisco,
Cleversafe, Dell, Digital Sense, Huawei, NetApp, Open vStorage, Red Hat,
Scality, Seagate, SwiftStack, Toshiba, Western Digital.

Хранилище сразу спроектировали не на базе устаревшего и неподходящего
для распределенных систем стандарта POSIX (о его недостатках `мы
регулярно
рассказываем </content/Вышел-openstack-kilo-и-другие-новости>`__), а как
KV-хранилище с `незамысловатым
протоколом <https://github.com/Seagate/kinetic-protocol>`__,
использующим `protocol
buffers <https://developers.google.com/protocol-buffers/>`__. Добавление
поддержки в WIreshark будет сравнительно несложным делом.

Ну пока еще этот Kinetic взлетит, а до тех пор народ будет использовать
традиционные хранилища, и их разработчикам еще работы будет много. Если
вы из `"Ceph vs.

Gluster" </content/Вышел-openstack-kilo-и-другие-новости>`__ выбрали
последний, то наверное уже слышали, чтоб в конце весны `вышла версия
GlusterFS
3.7.0 <https://blog.gluster.org/2015/05/glusterfs-3-7-0-has-been-released-introducing-many-new-features-and-improvements/>`__
(новость уже `обсуждалась на
OpenNET.ru <http://www.opennet.ru/opennews/art.shtml?num=42257>`__). Из
особо понравившихся фич можно выделить "bitrot detection", поддержка
NFSv4 и pNFS, и шардинг, но новинок там гораздо больше.

