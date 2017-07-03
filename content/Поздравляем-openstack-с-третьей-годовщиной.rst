.. title: Поздравляем OpenStack с третьей годовщиной!
.. slug: Поздравляем-openstack-с-третьей-годовщиной
.. date: 2013-07-25 11:50:29
.. tags: openstack, clouds, nasa, rackspace, amazon, eucaliptus, apache software foundation, gluster, ceph, riak, ricon, seagate, posix, python, mirantis
.. category: статистика
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

19 июля 2010 года NASA и Rackspace `было объявлено о создании OpenStack
<http://www.serverwatch.com/news/article.php/3893726/Rackspace-NASA-Partner-on-OpenStack-Cloud-Computing-Install.htm>`__.
Запоздало, но поздравляем с годовщиной! День рождения, это повод подвести итоги
и рассказать о новостях за недавнее время.

Начнем с того, что если вы до сих пор не понимаете, как это все работает, то
Victoria Martínez de la Cruz опубликовала в своем блоге `схему взаимодействия
элементов OpenStack
<http://vmartinezdelacruz.com/in-a-nutshell-how-openstack-works/>`__.
Теперь-то все должно быть понятно.

Компания `RightScale <http://www.rightscale.com/>`__ опубликовала результаты
своего последнего `исследования состояния облачных технологий (PDF)
<http://www.rightscale.com/pdf/rightscale-state-of-the-cloud-report-2013.pdf>`__,
в котором утверждается, что единственный непобежденный конкурент у OpenStack,
это Amazon, но сзади не дают расслабиться Eucaliptus, продукт наших друзей из
одноименной компании, и CloudStack, разрабатываемый на кладбище
opensource-проектов, Apache Software Foundation.

Вскоре, в октябре 2013, выходит следующая версия OpenStack, с кодовым
именем "Havana", и наш коллега, инженер Red Hat и участник проектов
Fedora и Asterisk, `Russel
Bryant <https://www.openhub.net/accounts/russellb>`__ в своем блоге
рассказал о `грядущих изменениях в и
нововведениях <http://russellbryantnet.wordpress.com/2013/05/13/openstack-compute-nova-roadmap-for-havana/>`__.

В этом году Red Hat `доработала распределенную файловую систему
GlusterFS до полного соответствия требованиям
OpenStack <https://www.redhat.com/about/news/archive/2013/4/gluster-is-openStack-ready>`__,
и `полностью открыла все ее
компоненты <https://www.opennet.ru/opennews/art.shtml?num=36865>`__. Но
на самом деле, надо признать, подход GlusterFS к распределенным сетям
критикуется некоторыми специалистами. Например, на прошедшей конференции
`RICON <http://ricon.io/>`__, организуемой разработчиками Riak (который
с недавних пор `доступен в Fedora из
коробки <https://fedoraproject.org/wiki/Features/Riak>`__), инженером
Seagate, James Hughes, было сказано, что *"Any distributed filesystem
like GlusterFS or Ceph that tries to preserve the POSIX API will go the
way of the dodo bird"*. Разработчик GlusterFS и
`CloudFS/HekaFS <https://fedoraproject.org/wiki/HekaFS>`__, инженер Red
Hat и участник Fedora, `Jeff
Darcy <https://fedoraproject.org/wiki/User:Jdarcy>`__ несогласен как
минимум полностью с утверждением о скором вымирании этих систем, хотя-бы
потому, что `GlusterFS поддерживает сразу несколько API для доступа к
данным <http://hekafs.org/index.php/2013/05/object-mania/>`__, и
постепенно становящимся неактуальным POSIX не является исключительным
механизмом для доступа к данным в GlusterFS.

Кстати, возвращаясь к конкурентам OpenStack, `Jeff Darcy
<https://fedoraproject.org/wiki/User:Jdarcy>`__ приводит `интересные графики по
IO для хранилищ у OpenStack и конкурентов
<http://hekafs.org/index.php/2013/05/performance-variation-in-the-cloud/>`__.
Обратите внимание, когда будете выбирать решение, - ситуация очень непростая, а
цены отличаются существенно.

Уже `известный вам </content/Новая-версия-openstack-folsom>`__ наш коллега,
участник Fedora и член технического комитета OpenStack, `Mark McLoughlin
<https://www.openhub.net/accounts/markmc>`__, регулярно публикует отчеты с
заседаний управлющих советов OpenStack - `за май 2013
<https://blogs.gnome.org/markmc/2013/06/05/may-30th-openstack-foundation-board-meeting/>`__
и `за июнь 2013
<https://blogs.gnome.org/markmc/2013/06/29/june-27th-openstack-foundation-board-meeting/>`__.
По нашему мнению, это высокая степень открытости проекта, и процесса принятия
решений внутри него, что выгодно отличает OpenStack от многих других
организаций и компаний, занимающихся OpenSource.

Помимо организационных вопросов `Mark
McLoughlin <https://www.openhub.net/accounts/markmc>`__ публикует и статьи
технического характера. Одна из последних, это его `обзор различных
способов асинхронного программирования в
Python <https://blogs.gnome.org/markmc/2013/06/04/async-io-and-python/>`__
(на котором написано очень многое в OpenStack).

В блоге `Mirantis <https://www.mirantis.com/>`__ на Habrahabr появилось
еще несколько статей по OpenStack-тематике. `Почитайте обязательно, если
интересуетесь
вопросом <https://habrahabr.ru/users/mirantis_openstack/topics/>`__.
