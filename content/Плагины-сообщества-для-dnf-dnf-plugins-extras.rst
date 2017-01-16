.. title: Плагины сообщества для DNF (dnf-plugins-extras)
.. slug: Плагины-сообщества-для-dnf-dnf-plugins-extras
.. date: 2014-12-16 15:11:53
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


Как сообщает наш коллега и участник DNF Community Team, `Igor
Gnatenko <https://github.com/ignatenkobrain>`__:
Сегодня мы запустили новый проект
`dnf-plugins-extras <https://github.com/rpm-software-management/dnf-plugins-extras>`__,
где могут находиться абсолютно любые плагины для DNF с любым количеством
внешних зависимостей.

Очень скоро в Fedora появится одноимённый пакет. После чего вы сможете
предложить написать какой-нибудь инетересный плагин, отправить сообщение
об ошибке в уже существующем плагине в RedHat Bugzilla. Pull реквесты
так же с удовольствием рассматриваются.

На данный момент уже написан один плагин -
`snapper <http://rpm-software-management.github.io/dnf-plugins-extras/index.html>`__.

Он создаёт снимки файловой системы каждую транзакцию
(установка/удаление/обновление пакетов) через
`snapper <http://snapper.io/>`__ демон, который предоставляет очень
удобные возможности по управлению снэпшотами.

**Q**: Почему просто не добавлять плагины сообщества в dnf-plugins-core?
**A**: Мы хотим сохранить core плагины минимальными (без сторонних
зависимостей)
`Анонс на официальном
сайте <http://dnf.baseurl.org/2014/12/16/community-plugins-for-dnf/>`__
