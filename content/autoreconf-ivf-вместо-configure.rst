.. title: Autoreconf -ivf вместо ./configure
.. slug: autoreconf-ivf-вместо-configure
.. date: 2015-02-09 15:25:52
.. tags: security, debian, bitcoin
.. category: Fedora Changes
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Еще один интересный вопрос `подняли в рассылке
devel@lists.fedoraproject.org <https://thread.gmane.org/gmane.linux.redhat.fedora.devel/204014>`__
- не пересобирать ли нам autotools-скрипты всегда, вместо использования
тех, что лежат в тарболлах? На самом деле, его задают регулярно, но
мнения наших участников по нему полярно различаются.

Одна из важных задач, которая решается многими участниками - от `Debian
Community <https://wiki.debian.org/ReproducibleBuilds>`__ и
криптоанархистов из
`Tor <https://blog.torproject.org/blog/deterministic-builds-part-one-cyberwar-and-global-compromise>`__
и `Bitcoin
Foundation <https://bitcoinmagazine.com/5858/linux-distribution-packaging-and-bitcoin/>`__
до военщины разных стран и FSF, это полная повторяемость процесса
сборки, с верифицируемым результатом на каждой стадии. Для этого
необходимо пересобирать по возможности все, включая ресурсы (картинки,
фонты, документацию), протоколируя на каждом этапе, что и как
получается. К сожалению, результат выполнения *autoreconf -ivf*, на базе
описаний configure.ac и Makefile.am, зависит от точной версии autotools.

Получается, что наоборот, их пересборка уменьшает степень повторяемости
процесса создания бинарников, требуя замораживать/фиксировать еще больше
версий используемого ПО, хотя и повышает контроль над процессом.

В Debian `рекомендуется пересобирать
autotools-скрипты <https://wiki.debian.org/Autoreconf>`__, хотя и не
требуется. У нас, к сожалению, консенсуса пока нет - отдельные
мэйнтейнеры предпочитают пересобирать, другие отстаивают позицию, что
пересобирать не надо. Подождем еще пару релизов, наверное.
