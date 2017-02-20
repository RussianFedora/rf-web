.. title: Предложен новый API для BSD-sockets
.. slug: predlozhen-novyi-api-dlia-bsd-sockets
.. date: 2017-02-20 16:51:55 UTC+03:00
.. tags: posix, rfc
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Устаревание POSIX, это не фантазия наших коллег, а `суровая реальность <http://www.cs.columbia.edu/~vatlidak/resources/POSIXmagazine.pdf>`_. Стандарт устарел и для хранения данных, и для передачи данных по сети. Если по хранению данных у нас есть варианты, то на сетевую подстистему пока никто не покушался. До недавних пор.

Martin Sustrik, инженер Google и коллега Pieter Hintjens по разработке ZeroMQ, предложил переработать `BSD sockets API <https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BA%D0%B5%D1%82%D1%8B_%D0%91%D0%B5%D1%80%D0%BA%D0%BB%D0%B8>`_. Он `создал репозиторий на GitHub <https://github.com/sustrik/dsock>`_, в котором выложил `первый вариант предложенных изменений <https://raw.githubusercontent.com/sustrik/dsock/master/rfc/sock-api-revamp-01.txt>`_ и ряд примеров.

Подозреваем, что любителей юниксвэя ждут тяжелые времена в этом году.
