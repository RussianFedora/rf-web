.. title: В Fedora 30 не будет Python 2
.. slug: v-fedora-30-ne-budet-python-2
.. date: 2018-03-28 16:11:00 UTC+03:00
.. tags: python, eol
.. category: Fedora Changes
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Интересное предложение поступило - `отказаться и полностью удалить Python2 из
Fedora 30
<https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/2XDT6S62SEN4KGWQCOUYKXLBYVTKJ5VI/>`_.
Дело в том, что Python2 уже 10 лет поддерживается силами добровольцев, но с
`первого января 2020 года его разработка будет окончательно заброшена <https://smoogespace.blogspot.cz/2018/03/15-year-warning-python2-will-be-end-of.html>`_.

Прямо сейчас в Fedora есть около 3000 пакетов, которые требуют только Python2,
и после 2020 года нужно будет либо их поддерживать самим (вместе с Python2),
либо просто выкинуть их на мороз. Среди мэйнтейнеров Python-пакетов в Fedora
главенствует идея, что лучше отказаться от Python2, чем заниматься поддержкой
Python2-пакетов. Если достигнем консенсуса, то начнем выбрасывать пакеты,
которые имеют Python3-аналоги, а от их Python2-версий никакие другие пакеты из
официальных репозиториев Fedora не зависят.

Если что-то пойдет не так, то предлагается добавить compatibility-пакет
python27. Мы так иногда делаем, когда проблема не решается простым апгрейдом
зависимых пакетов, так что для нас это вполне допустимо.
