.. title: Erlang получает поддержку systemd!
.. slug: erlang-получает-поддержку-systemd
.. date: 2013-12-19 01:01:33
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Языки программирования постепенно обрастают библиотеками для работы с
systemd </content/Коммьюнити-haskell-делает-первые-шаги-навстречу-systemd>`__.

`Holger Winkelmann <https://github.com/hwinkel>`__, основатель компании
`Tavelping GmbH <http://www.travelping.com/>`__ и ее управляющий, в
рассылке разработчиков Erlang
`анонсировал <http://thread.gmane.org/gmane.comp.lang.erlang.general/71041>`__
выход `ejournald <https://github.com/travelping/ejournald>`__,
библиотеки для работы с Journald, и
`lager\_journald\_backend <https://github.com/travelping/lager_journald_backend>`__,
бэкенда Journald для популярного фреймворка ведения журнала событий,
`Lager <https://github.com/basho/lager>`__, в свою очередь
разработанного нашими друзьями из `Basho <http://basho.com/>`__.

Travelping, это довольно известная среди телеком-специалистов компания,
которая производит высокопроизводительные AAA-решения, SDN-системы для
облачных инфраструктур, embedded-системы, и заказное ПО с высокими
требованиями по надежности. Понятно, что это как раз ниша для
современной системы контроля за сервисами, systemd. Однако до сих пор не
было решения по журналированию, используя Journald, и приходилось либо
писать в файлики, "вручную", либо использовать syslog (например,
`так <https://github.com/lemenkov/erlsyslog>`__). Теперь есть такая
библиотека.

Продолжается `работа над интеграцией systemd и
EPMD </content/Коммьюнити-haskell-делает-первые-шаги-навстречу-systemd>`__,
ключевого элемента распределенных Erlang-систем. Наш товарищ, участник
коммьюнити openSUSE, `Matwey V. Kornilov <https://github.com/matwey>`__,
представил `еще один вариант совместной работы этих
компонентов <https://github.com/matwey/otp/commits/systemd>`__. Мы
обязательно попробуем включить его патчи в ближайшую сборку Erlang.

