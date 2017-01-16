.. title: Open CASCADE и Fedora
.. slug: open-cascade-и-fedora
.. date: 2013-12-26 13:11:29
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Open CASCADE <http://www.opencascade.org/>`__, это широко популярный в
узких кругах `продукт, сочетающий в себе набор библиотек и средств
разработки ПО, ориентированного на 3D-моделирование, в особенности
систем автоматизированного
проектирования <http://ru.wikipedia.org/wiki/Open_CASCADE_Technology>`__.

На базе фреймворка построены такие продукты, как
`SALOME <http://www.salome-platform.org/>`__,
`FreeCAD <http://www.freecadweb.org/>`__ и `ряд проприетарных
продуктов <http://www.opencascade.org/showroom/screenshots/>`__.

В проекте Fedora, разумеется, есть заинтересованные люди, которые в т.ч.
используют ПО такого уровня, и были попытки включить в репозиторий как
`Open CASCADE <https://bugzilla.redhat.com/458974>`__, так и
`FreeCAD <https://bugzilla.redhat.com/459125>`__. К сожалению, они хоть
и были, но закончились ничем. Дело в том, что Open CASCADE
распространялся под открытой, но несвободной `Open CASCADE Technology
Public
License <https://fedoraproject.org/wiki/Licensing/Open_CASCADE_Technology_Public_License>`__,
а несвободное ПО и контент запрещены к включению в Fedora. Переговоры с
разработчиками Open CASCADE об изменении условий лицензирования велись
как
`публично <http://www.opencascade.org/org/forum/thread_15859/?forum=3>`__,
так и по внутренним каналам, и в переговорах и консультациях участвовало
много известных лиц, как от Fedora Project, так и от Debian Community -
от нашего коллеги, участника Fedora Legal, юриста SFLC и патентного
адвоката Red Hat, `Richard
Fontana <http://en.wikipedia.org/wiki/Richard_Fontana>`__, до `Richard
Matthew Stallman <http://stallman.org/>`__, но все закончилось
безрезультатно. В конце концов, сообщество Debian решилось на включение
Open CASCADE несмотря на очевидное нарушение лицензии будущими
пользователями пакетов из репозиториев Debian, но потом `удалило почти
отовсюду <http://packages.debian.org/search?keywords=cascade&searchon=names&suite=all&section=all>`__.

Кстати, одна из причин, почему Debian не фигурирует в новостях про
крупные переходы с чего-нибудь проприетарного на Linux, это вот такое
студенческое раздолбайство и хипповский пофигизм по отношению к
юридическим вопросам (не единственная, конечно, причина, почему Debian
теряет популярность, и есть много других - `технологическое
отставание </content/Новости-systemd-за-прошедший-месяц-полтора>`__,
появление Canonical и создание дистрибутива Ubuntu, отсутствие
коммерческих компаний за проектом Debian и т.п.). Мы наблюдаем
интересную тенденцию - если еще лет 5 назад по вопросам лицензий народ
интересовался мнением коммьюнити Debian, то теперь, по таким проблемам,
за советом обращаются в Fedora Legal.

Проходило время, и компания-разработчик Open CASCADE начала понимать
сложившуюся ситуацию, и начала движение в сторону коммьюнити вокруг
дистрибутивов. С выходом Open CASCADE 6.5 `внимательные участники Fedora
Project заметили смягчение условий лицензионного
соглашения <http://thread.gmane.org/gmane.linux.redhat.fedora.legal/1325/focus=1327>`__,
которое, к сожалению, `в целом так и осталось
несвободным <http://thread.gmane.org/gmane.linux.redhat.fedora.legal/1325/focus=1328>`__.

Неожиданно, на форуме Open CASCADE появился
`анонс <http://dev.opencascade.org/index.php?q=node/908>`__, в котором
сообщалось, что версия 6.7.0 будет перелицензирована под LGPL 2.1. И
действительно, несмотря на отсутствие упоминания в `Release Notes к
версии
6.7.0 <=%22http://www.opencascade.org/about/news/issue199/%22>`__,
лицензия на фреймворк `была заменена на LGPL
2.1 <http://www.opencascade.org/getocc/license/>`__, а старая Open
CASCADE Technology Public License `перенесена в
архив <http://www.opencascade.org/getocc/license/license_old/>`__. К
несчастью, они не стали использовать LGPL как есть, а добавили свою
часть, и это `потребовало изучения Fedora
Legal <http://thread.gmane.org/gmane.linux.redhat.fedora.legal/2090>`__,
но мы предполагаем, что FE-Legal в этот раз одобрит лицензию, и
заинтересованные люди наконец-то смогут завершить включение этого
интересного фреймворка в Fedora.

Мы будем следить за развитием событий.

