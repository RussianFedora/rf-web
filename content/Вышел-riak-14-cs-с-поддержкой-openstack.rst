.. title: Вышел Riak 1.4 CS с поддержкой OpenStack
.. slug: Вышел-riak-14-cs-с-поддержкой-openstack
.. date: 2013-08-13 22:19:33
.. tags: riak, dds, openstack, posix, clouds
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Riak CS <http://basho.com/riak-cloud-storage/>`__, это облачное
хранилище, построенное на базе `Riak <http://basho.com/riak/>`__. До
недавнего времени оно было проприетарным дорогостоящим продуктом, и его
открытие удивило многих. Мы, разумеется, сразу стали планировать его
включение в Fedora, благо `Riak уже там
есть <http://fedoraproject.org/wiki/Features/Riak>`__. Ориентировочно
ожидается завершение работы по его включению в Fedora к 21й версии.

`Сегодня вышла версия Riak CS
1.4 <http://basho.com/riak-cs-1-4-is-now-available/>`__, в которой
впервые добавлена поддержка сервиса аутентификации OpenStack и API
хранилища данных для OpenStack. Таким образом Riak CS можно использовать
как бэкенд для хранения данных в OpenStack инсталляции. Как вы уже
слышали, `некоторые эксперты считают файловые системы с интерфейсом
POSIX вымирающим видом в
облаках </content/Поздравляем-openstack-с-третьей-годовщиной>`__, а
некоторые встретили это заявление в штыки и горячо полемизировали с
первыми. Так что появление компонента, использующего совершенно другой
подход к работе с данными можно только поприветствовать. Вот теперь мы и
проверим, кто окажется прав.

Раз уж заговорили про облака, то сделаем небольшой анонс. Очень скоро мы
анонсируем сентябрьское мероприятие совместо с
`OpenStack.ru <http://openstack.ru/>`__, посвященное облачным
технологиям - не пропустите! Обязательно приходите и пообщаемся в т.ч.
на эту тему.

На фото (из серии "наши лица") - участник Fedora доволен тем, как
работает Riak из коробки.

.. image:: https://lh4.googleusercontent.com/-_9So1xL9eKY/UJ_Frjx-c7I/AAAAAAAAHAg/QYrMLJM0P_o/s400/me_riak_t_shirt.jpg
   :align: center
   :width: 400px
   :height: 400px
   :target: https://picasaweb.google.com/lh/photo/I4WDMbYGajpJBHss6I85r9MTjNZETYmyPJy0liipFm0?feat=embedwebsite
