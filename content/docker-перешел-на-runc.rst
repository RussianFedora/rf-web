.. title: Docker перешел на runC!
.. slug: docker-перешел-на-runc
.. date: 2016-04-15 17:07:08
.. tags: docker, systemd
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Прошло менее года с момента `анонсирования стандарта Open
Containers </content/Великий-Открытый-Контейнерный-Стандарт>`__, и,
наконец-то, дело пошло. `Свежевыпущенный Docker 1.1 начал использовать
runC <https://www.opennet.ru/opennews/art.shtml?num=44246>`__, утилиту,
созданную в рамках проекта Open Containers. Это позволит добиться
гораздо лучшей совместимости с systemd, чем раньше (а `раньше было не
очень хорошо </content/Что-там-у-systemd>`__).

