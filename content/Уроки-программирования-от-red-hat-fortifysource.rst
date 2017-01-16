.. title: Уроки программирования от Red Hat (FORTIFY_SOURCE)
.. slug: Уроки-программирования-от-red-hat-fortifysource
.. date: 2014-03-27 13:41:13
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Специалисты по безопасности Red Hat продолжают заметки об основных
приемах разработки безопасного ПО. На этот раз `было рассказано о
макросе
FORTIFY\_SOURCE <https://securityblog.redhat.com/2014/03/26/fortify-and-you/>`__,
который входит в состав дефолтных ключей gcc в Fedora уже достаточно
долгое время. Этот макрос включает дополнительную runtime-проверку на
соответствие размера входного буфера выходному в следующих функциях -
*memcpy, mempcpy, memmove, memset, strcpy, stpcpy, strncpy, strcat,
strncat, sprintf, vsprintf, snprintf, vsnprintf, gets*. Благодаря ему
находится, кстати, `довольно много
проблем <https://www.google.ru/search?q=site:bugzilla.redhat.com+%22buffer+overflow+detected%22>`__.

Автор заметки спускается до ассемблерных листингов, и довольно подробно
описывает поведение программы, собранной с добавлением этого макроса в
строку запуска gcc. Ознакомьтесь и если у вас самосборный дистрибутив,
обязательно убедитесь, что этот макрос входит в дефолтный набор.

