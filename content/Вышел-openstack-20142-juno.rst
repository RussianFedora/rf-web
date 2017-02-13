.. title: Вышел OpenStack 2014.2 Juno
.. slug: Вышел-openstack-20142-juno
.. date: 2014-10-17 14:51:13
.. tags: openstack, clouds, statistics, mirantis, rackspace, redhat, sdn, oin, патенты, legal, docker
.. category: статистика
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Наконец-то вышел `OpenStack 2014.2
Juno <http://www.openstack.org/software/juno/press-release>`__ (новость
уже `обсуждается на
OpenNET.ru <http://www.opennet.ru/opennews/art.shtml?num=40851>`__).

Интересно сравнить участие компаний по `сравнению с предыдущим 2014.1
Icehouse <>`__.

+------------+-------------+
| **Было**   | **Стало**   |
+------------+-------------+
| |image0|   | |image1|    |
+------------+-------------+

Отрадно видеть, что наши соотечественники из Mirantis подвинули
Rackspace и теперь на четвертом месте по вкладу в релиз. Ну, понятно,
что Red Hat делает больше всех, а вот второе место HP и медленное
сползание Rackspace может удивить лишь тех, кто не слышал, `что
происходит </content/Облачные-новости-1>`__ (и
`еще </content/hewlett-packard-купил-eucaliptus>`__). Кстати, все
заметили какой компании на диаграммах нет? А туда же - хвастаются, что
мол умеют работать с OpenStack. Как такое возможно без активного участия
в проекте - нам непонятно.

В новшествах OpenStack 2014.2 довольно много всего, но особо бы хотелось
отметить `сетевую
подсистему <https://wiki.openstack.org/wiki/ReleaseNotes/Juno#OpenStack_Network_Service_.28Neutron.29>`__.

По списку новых плугинов видно, что движение в сторону SDN очень
серьезное. Мы не раз уже говорили, и повторимся, что SDN, это следующая
(или уже нынешняя) горячая тема.

Недавно Linux Foundation `объявило о создании открытой платформы для
виртуализации компонентов сетей, Open Platform for NFV Project
(OPNFV) <http://www.linuxfoundation.org/news-media/announcements/2014/09/telecom-industry-and-vendors-unite-build-common-open-platform>`__.

Платформа будет построена на базе уже готовых компонентов, таких, как
Linux, OpenStack, OpenDaylight, и т.п., о чем с гордостью
`сообщил <http://www.opendaylight.org/blogs/2014/09/rise-open-opendaylight-and-opnfv>`__
в корпоративном блоге `известный вам Neela
Jacques </content/Текущая-ситуация-на-рынке-виртуализации-x86-систем>`__.

Red Hat, разумеется, собирается играть активную роль в этом проекте, и
обладает собственным видением ситуации (и многочисленными разработчиками
и неофициальным влиянием на другие коммьюнити опенсорс-разработчиков.
Ознакомьтесь с выступлением `Chris
Wright <https://www.linkedin.com/pub/chris-wright/1/385/b73>`__ на
`Collaboration Summit
2014 <https://events.linuxfoundation.org/events/archive/2014/collaboration-summit>`__:
...и
`комментариями <http://blogs.gnome.org/markmc/2014/10/02/network-function-virtualization-the-opportunity-for-openstack-and-open-source/>`__
нашего коллеги, Mark McLoughlin, на эту тему. Можно полагать, что если
будет реализована хотя бы часть задуманного в рамках создания открытой
виртуализированной распределенной архитектуры, то проприетарные системы
уже никогда не догонят открытые. Не поэтому ли
`некоторые </content/vmware-выпускает-свой-продукт-на-базе-openstack>`__
проприетарные вендоры присоединяются к OpenStack? Ну, может не только
потому, но в т.ч. и потому.

На самом деле у проприетарных вендоров будет в руках сильное оружие (и
хороший источник дохода) - патенты. Т.к. законы США распространяются на
весь мир, то не учитывать роль патентных троллей нельзя. Open Invention
Network недавно `предупредило честных людей, что у коммьюнити OpenStack
нет никаких возможностей защищать своих пользователей и разработчиков от
патентных
троллей <http://www.theregister.co.uk/2014/10/02/oin_openstack_warning/>`__.
Сейчас OIN расширяет свой защитный экран на OpenStack, и уже
прикрывается 33 Python-пакета. Сейчас `к OIN начали активно подключаться
новые
пользователи <http://www.infoworld.com/article/2690911/open-source-software/oin-grows-despite-trolls-facing-hard-times.html?utm_content=buffer0ffea>`__.
Проняло даже стартапы и азиатские компании, которые, как и некоторые
отечественные игроки рынка, раньше не верили, что законы США
распространяются и на них. Неудивительно, т.к. ущерб от американских
патентных троллей `стабильно
растет <https://gigaom.com/2014/10/08/patent-trolling-pays-since-2010-trolls-have-made-3-times-as-much-money-in-court-as-real-companies/>`__.

И напоследок о хорошем. `Вышел Docker
1.3 <https://blog.docker.com/2014/10/docker-1-3-signed-images-process-injection-security-options-mac-shared-directories/>`__.


.. |image0| image:: https://bitergia.files.wordpress.com/2014/04/top10companiesicehouse.jpg
   :width: 400px
   :target: http://blog.bitergia.com/2014/04/17/the-openstack-icehouse-release-activity-and-organizations/
.. |image1| image:: https://bitergia.files.wordpress.com/2014/10/top10orgsjuno.jpg
   :width: 400px
   :target: http://blog.bitergia.com/2014/10/15/the-openstack-juno-release-activity-and-organizations/
