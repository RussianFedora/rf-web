.. title: DNF 0.6.3 и dnf-plugins-core 0.1.4
.. slug: dnf-063-и-dnf-plugins-core-014
.. date: 2014-12-10 12:38:10
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


| 9 декабря 2014, вышла новая версия пакетного менеджера DNF - 0.6.3.
  Вместе с ним вышла новая версия набора основных плагинов
  dnf-plugins-core - 0.1.4.
| **Новинки DNF**:

-  deltrarpm теперь включен по умолчанию
-  dnf-automatic теперь может не только отправлять результаты выполнения
   действий в почту или в stdio, но и в `motd (Message of the
   day) <https://en.wikipedia.org/wiki/Motd_%28Unix%29>`__.

-  Очень сильно ускорено автодополнение в bash за счёт использования
   sqlite в связке с dnf-plugins-core и за счёт использования python API
   без dnf-plugins-core.

-  `Несколько <https://github.com/rpm-software-management/dnf/commit/07170b6c3145a71465e0b5e8669aa7f2218e2c6d>`__
   `багфиксов <https://github.com/rpm-software-management/dnf/commit/b7fa16082d47b6e45ce93b61e0e57fc528da412a>`__
   в автодополнении в bash (например, если ввести / после команды
   install, то он не будет проверять на наличие пакета в базе, а сразу
   предложит выбрать путь к файлу)
-  Использование systemd inhibitor при транзакциях
-  Ещё очень много багфиксов

| 
| **Новинки dnf-plugins-core**:

-  Новый плагин -
   `reposync <http://dnf-plugins-core.readthedocs.org/en/latest/reposync.html>`__,
   предназначенный для синхронизирования удалённого репозитория локально
-  Новый плагин -
   `needs\_restarting <http://dnf-plugins-core.readthedocs.org/en/latest/needs_restarting.html>`__,
   предназначенный для проверки процессов на необходимость рестарта
   после обновления пакетов
-  Плагин
   `generate\_completion\_cache <http://dnf-plugins-core.readthedocs.org/en/latest/generate_completion_cache.html>`__
   теперь `хранит все данные в
   sqlite <https://github.com/rpm-software-management/dnf-plugins-core/commit/9dce5ff0d0f78c55487fa971feb68ec9a639fc17>`__
   (раньше было в текстовом файле) для ускорения поиска по нему
-  Несколько багфиксов

| 
| **Contributors**:

-  Ales Kozumplik (бывший руководитель проекта)
-  Daniel Mach
-  Igor Gnatenko
-  Jan Silhan (руководитель проекта)
-  Kushal Das
-  Michal Luscon
-  Miroslav Suchý
-  Satoshi Matsumoto
-  Tim Lauridsen
