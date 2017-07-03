.. title: Arch перешел на systemd-logind
.. slug: arch-перешел-на-systemd-logind
.. date: 2012-10-31 10:32:43
.. tags: archlinux, systemd
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Когда мы услышали недавно новость о том, что ищутся добровольцы
поддерживать SysV-скрипты в Arch Linux, стало понятно, что это веселая
шутка такая. Переход на systemd подразумевает то, что все замшелые
костыли рано или поздно будут выкинуты. А иначе зачем переходить? Чтоб
тянуть совместимость?

На днях участники коммьюнити Arch Linux вколотили новый гвоздь - `отказались от
ConsoleKit <https://www.archlinux.org/news/consolekit-replaced-by-logind/>`__,
который некоторое время назад тоже был передовой технологией, пока `внезапно
<https://lurkmore.to/Внезапно>`__ не стал устаревшей маргинальной поделкой.
Теперь система будет работать полноценно лишь если была загружена с помощью
systemd. Новость уже обсуждается на `OpenNET.ru
<https://www.opennet.ru/opennews/art.shtml?num=35208>`__.
