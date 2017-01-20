.. title: OpenCL в Fedora
.. slug: opencl-в-fedora-0
.. date: 2014-01-16 15:16:47
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


С `октября 2013 года </content/opencl-в-fedora>`__ ситуация с OpenCL в
Fedora еще немного улучшилась, хотя "из коробки" пока не работает.

Участник нашего коммьюнити, `Igor
Gnatenko <https://www.openhub.net/accounts/ignatenkobrain>`__,
присоединился к
`инициативе <https://fedoraproject.org/wiki/Changes/OpenCL>`__ инженера
Red Hat и разработчика oVirt, `Fabian
Deutsch <https://www.openhub.net/accounts/fabiand>`__, и предложил `ряд
изменений для
Mesa <https://github.com/fabiand/mesa-spec/compare/master...opencl>`__,
которые корректно включают поддержку OpenCL в библиотеке. Как минимум,
`можно будет запустить стандартные утилиты и получить параметры
доступных
OpenCL-драйверов <http://dummdida.tumblr.com/post/73011935640/mesas-opencl-state-tracker-on-fedora-is-around-the>`__.

К сожалению, работа еще не завершена, и необходимо `замерджить эти
изменения в Mesa в репозиторий
Fedora <https://bugzilla.redhat.com/887628>`__, и добавить еще несколько
библиотек и приложений (сейчас идет работа по включению
`beignet <https://bugzilla.redhat.com/1052393>`__).

