.. title: Реальное использование fedmsg в быту
.. slug: Реальное-использование-fedmsg-в-быту
.. date: 2014-03-22 18:45:08
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Шина `fedmsg <http://www.fedmsg.com/en/latest/>`__ набирает
популярность. Ну, например, Fedora Java SIG использует ее, чтоб
подписавшись на несколько типов сообщений своевременно проверять размер
минимальной установки ряда интересных им пакетов при пересборке их
зависимостей. Если они видят внезапный скачок, то значит цепочка
зависимостей резко изменилась, и надо что-то делать. Но этим возможности
fedmsg не исчерпываются.

Наш коллега, инженер Red Hat и участник коммьюнити Gentoo, `Stanislav
Ochotnicky <https://www.openhub.net/accounts/sochotnicky>`__, в своем
блоге
`анонсировал <http://blog.ochotnicky.com/2014/03/21/fedwatch-running-scripts-based-on-fedmsg-messages/>`__
первый релиз приложения
`fedwatch <https://github.com/sochotnicky/fedwatch>`__. Это не только
приложение, но и мини-библиотека, позволяющая быстро писать скрипты,
запускаемые по неким событиям от fedmsg. Например, при сборке какого-то
пакета, либо при открытии заявки в багзилле. Вообще, вариантов
представляется довольно много. Другой наш коллега, `Miroslav
Suchý <https://www.openhub.net/accounts/msuchy>`__, тут же подхватил
разговор, быстро смастерив `несложный скрипт уведомления об успешном
завершении сборки в
Copr <http://miroslav.suchy.cz/blog/archives/2014/03/21/how_to_get_notification_about_your_builds_in_copr/index.html>`__.

В общем пробуйте!
