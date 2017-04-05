.. title: Итоги очередной пересборки всех почти 12 тысяч пакетов Fedora
.. slug: Итоги-очередной-пересборки-всех-почти-12-тысяч-пакетов-fedora
.. date: 2012-07-23 09:34:19
.. tags: gcc
.. category: Fedora Changes
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Недавно закончилась очередная пересборка всего дерева пакетов Fedora, в
этот раз запущенная не новой версией GCC, а двумя фичами, о которых `вы
наверняка уже слышали </content/Одобрены-новые-фичи-fedora-18>`__ -
`использование специализированной утилиты для сжатия
DWARF-секций <https://fedoraproject.org/wiki/Features/DwarfCompressor>`__
и
`MiniDebuginfo <https://fedoraproject.org/wiki/Features/MiniDebugInfo>`__.

Полный ребилд занял примерно три дня и по его результатам `не собралось
более 600 пакетов <http://fedorapeople.org/~ausil/f18-failures.html>`__,
а успешно прошло пересборку - почти 11 тысяч. Среди поломанных пакетов
есть и те, что находятся в ведении отечественных мэйнтейнеров - у Оксаны
Курышевой не собрался
`flush <http://koji.fedoraproject.org/koji/taskinfo?taskID=4256133>`__
из-за несовместимости с новым autotools, у Павла Алексеева поломался
`php-pecl-runkit <http://koji.fedoraproject.org/koji/taskinfo?taskID=4288770>`__,
`printoxx <http://koji.fedoraproject.org/koji/taskinfo?taskID=4290475>`__,
`sim <http://koji.fedoraproject.org/koji/taskinfo?taskID=4305525>`__ и
`slim <http://koji.fedoraproject.org/koji/taskinfo?taskID=4305722>`__, у
Константина Рябицева -
`email2trac <http://koji.fedoraproject.org/koji/taskinfo?taskID=4253954>`__
и
`pathfinder <http://koji.fedoraproject.org/koji/taskinfo?taskID=4276889>`__,
у Павла Жукова поломаны
`matreshka <http://koji.fedoraproject.org/koji/taskinfo?taskID=4270514>`__,
`zeromq-ada <http://koji.fedoraproject.org/koji/taskinfo?taskID=4316290>`__
и
`zyGrib <http://koji.fedoraproject.org/koji/taskinfo?taskID=4316623>`__,
у Петра Леменкова (т.е. меня) похоже самый большой список поломок -
`erlang-bitcask <http://koji.fedoraproject.org/koji/taskinfo?taskID=4254158>`__,
`leveldb <http://koji.fedoraproject.org/koji/taskinfo?taskID=4267406>`__,
`libmcrypto <http://koji.fedoraproject.org/koji/taskinfo?taskID=4268295>`__,
`libmikey <http://koji.fedoraproject.org/koji/taskinfo?taskID=4268305>`__,
`libmnetutil <http://koji.fedoraproject.org/koji/taskinfo?taskID=4268324>`__,
`libmsip <http://koji.fedoraproject.org/koji/taskinfo?taskID=4268358>`__,
`libmstun <http://koji.fedoraproject.org/koji/taskinfo?taskID=4268368>`__,
`libmutil <http://koji.fedoraproject.org/koji/taskinfo?taskID=4268388>`__,
`nrpe <http://koji.fedoraproject.org/koji/taskinfo?taskID=4274563>`__,
`openser <http://koji.fedoraproject.org/koji/taskinfo?taskID=4275879>`__,
`pspp <http://koji.fedoraproject.org/koji/taskinfo?taskID=4290677>`__,
`stratagus <http://koji.fedoraproject.org/koji/taskinfo?taskID=4307099>`__.

Поломки, это ничего страшного, рутинный рабочий момент - появляются
новые версии ПО, надо патчить старый софт, чтоб он работал с новым, и мы
вполне успеем починить все поломки к выходу Fedora 18.
