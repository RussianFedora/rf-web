.. title: systemd теперь может импортировать контейнеры Docker
.. slug: systemd-теперь-может-импортировать-контейнеры-docker
.. date: 2014-12-19 12:28:46
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Продолжается отказ от Docker, как от средства манипуляции контейнерами.

Вслед за новостью о том, что CoreOS переходит на свое собственное
решение, о чем `мы вскользь
упомянули </content/coreos-отказывается-от-btrfs>`__, systemd `получил
возможность напрямую импортировать контейнеры
Docker <https://github.com/systemd/systemd/commit/7264832>`__. Учитывая
высокую интеграцию systemd, понятно, что оперировать контейнерами с
помощью него будет удобнее и надежнее.

В новой фиче нам особенно понравилось то, что `Lennart старательно
избегает слова
Docker <https://github.com/systemd/systemd/blob/7264832/src/import/import-dck.c#L103-106>`__,
что `в systemd теперь включен
JSON-парсер <https://github.com/systemd/systemd/commit/e7eebcf>`__
(давно бы так!), и что `systemd теперь требует
cURL <https://github.com/systemd/systemd/blob/7264832/src/import/curl-util.c>`__.

Давно пора было включить зависимость от cURL!
