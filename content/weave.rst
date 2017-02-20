.. title: Weave
.. slug: weave
.. date: 2014-09-09 17:25:47
.. tags: rabbitmq, weave, sdn, golang
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Наши друзья из RabbitMQ, недавно создавшие новый стартап,
`zettio <http://www.zett.io/>`__, анонсировали `еще один подход к
созданию виртуальных сетей в
кластере <http://www.infoq.com/news/2014/09/zettio_releases_weave>`__ -
`Weave <https://github.com/zettio/weave/>`__.

.. image:: https://raw.githubusercontent.com/zettio/weave/master/docs/deployment.png
   :algn: center

Weave уже традиционно написан на Go, и позволяет создавать виртуальные
сети невероятно легко. Хосты могут подключаться и отключаться
динамически, поддерживается автоконфигурация, и возможно прозрачное
объединение в сеть узлов, не все из которых видят друг друга (A видит Б,
но не видит С, а С видит Б, но не видит А, и Weave автоматически создаст
не требующую конфигурации приватную сеть из A,B и C). Опять же, отрадно
видеть еще одну реализацию `service
discovery </content/Краткий-обзор-облачных-средств-service-discovery>`__.
