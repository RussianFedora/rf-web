.. title: Последние новости короткой строкой.
.. slug: node-364
.. date: 2012-11-21 11:09:01
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Вышел systemd
196 <https://thread.gmane.org/gmane.comp.sysutils.systemd.devel/7400>`__.

Среди улучшений - udev теперь может загружать данные об устройствах из
базы данных (вместо текстовых файлов), многочисленные улучшения в
journald, удаление кода для поддержки устаревших дистрибутивоспецифичных
функций, поддержка систем без PolicyKit, поддержка работы в режиме
установки оффлайн-обновлений (требующих перезагрузки).

`Ralph Bean <https://www.openhub.net/accounts/ralphbean>`__
продемонстрировал, как `подключаться к шине Fedora Infrascructure
используя лишь Python и
ZeroMQ <http://threebean.org/blog/zeromq-and-fedmsg-diy/>`__. Так что,
если вам не хватает какой-то функциональности, то теперь вы можете ее
легко написать. Например, производить какие-нибудь статистические
исследования активности участников Fedora. Конечно можно сделать гораздо
проще - `есть целая библиотека для работы с Fedora Message Bus,
написанная на Python <http://fedmsg.readthedocs.org/en/latest/>`__.

Опубликован `предварительный план DevConf
2013 <https://eischmann.wordpress.com/2012/11/19/devconf-is-getting-content-and-it-looks-great/>`__
и объявлены `первые докладчики <http://devconf.cz/node/32>`__.

`Сообщают <http://log.amitshah.net/2012/11/avi-kivity-stepping-down/>`__,
что `Avi Kivity <http://www.linkedin.com/in/avikivity>`__, инженер
Qumranet и Red Hat, и активный участник Debian, объявил о своем уходе с
поста ко-мэйнтейнера KVM. Он с товарищами организовал стартап, который
представит что-то очень грандиозное, по словам Ави. Ну что, пожелаем
удачи!
`Radek Vokál <http://www.linkedin.com/in/radekvokal>`__ собрался с духом
и сообщил шокировавшую нас всех новость - он утверждает, что некоторые
разработчики, которые ранее использовали Fedora, по странному совпадению
после выхода GNOME 3 перешли на другие дистрибутивы или даже на Mac OS
X. В попытке придать правдоподобности этому своему измышлению, он
`приводит список причин, по которым эти заблудшие еретики сделали
это <http://rvokal.livejournal.com/23984.html>`__. Перед тем, как
сложить большой костер, надо признаться, что с некоторыми вещами дела
обстоят действительно не так и просто.

Кстати, о GNOME 3. `Allan
Day <https://plus.google.com/100040579167442382687/about>`__ рассказал
`о дальнейших [STRIKEOUT:удалениях функциональности] улучшениях в
интерфейсе GNOME
3 <https://afaikblog.wordpress.com/2012/11/20/the-next-step/>`__. Надо
признать, что интерфейс выглядит очень неплохо, как минимум на
картинках. Между тем, `Kalev
Lember <https://www.openhub.net/accounts/klember>`__ сообщает, что
`обновил GNOME 3 в Fedora 18 до версии
3.6.2 <https://thread.gmane.org/gmane.linux.redhat.fedora.devel/171054>`__.

`Rich W.M. Jones <http://people.redhat.com/~rjones/>`__ продолжает
создавать биндинги для libguestfs. Теперь он `написал биндинг для
Lua <https://rwmj.wordpress.com/2012/11/17/new-in-libguestfs-lua-bindings/>`__.

Если кто не в курсе, то Lua, это JavaScript по-португальски.

`Daniel P. Berrangé <https://www.openhub.net/accounts/berrange>`__
разразился серией заметок об OpenStack - `как произвести файловую
инъекцию перед запуском виртуальной машины на файл с образом диска
используя libguestfs вместо
FUSE <http://berrange.com/posts/2012/11/15/692/>`__, `что нового в
поддержке OpenStack Nova
libvirt? <http://berrange.com/posts/2012/11/16/what-was-new-in-libvirt-for-the-openstack-nova-folsom-release/>`__
и `как быстро развернуть OpenStack разработчику на Fedora используя
DevStack <http://berrange.com/posts/2012/11/19/walk-through-of-running-openstack-on-fedora-17-using-devstack/>`__.

Другой участник Fedora и его коллега, `Russel
Bryant <https://www.openhub.net/accounts/russellb>`__, рассказывает о
`новом сервисе OpenStack Nova -
nova-conductor <https://russellbryantnet.wordpress.com/2012/11/19/a-new-nova-service-nova-conductor/>`__.

И в завершении заметок об OpenStack - `Mark
McLoughlin <https://www.openhub.net/accounts/markmc>`__ рассказывает об
`обсуждении разделения проекта OpenStack на базовую часть и на
"incubation" <https://blogs.gnome.org/markmc/2012/11/17/the-future-of-incubation-and-core/>`__.

