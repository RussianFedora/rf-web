.. title: Изменения в Fedora 33
.. slug: izmeneniia-v-fedora-33
.. date: 2020-06-05 20:35:03 UTC+03:00
.. tags: erlang, boost, java, berkleydb, dnf, ntp, glibc, systemd, perl
.. category: Fedora Changes
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Одобрили еще несколько изменений будущей Fedora 33.

- `Обновление Erlang до версии 23 <https://fedoraproject.org/wiki/Changes/Erlang_23>`_.
- `Обновление Boost до версии 1.73 <https://fedoraproject.org/wiki/Changes/F33Boost173>`_.
- `Переход на OpenJDK 11  c OpenJDK 8 <https://fedoraproject.org/wiki/Changes/Java11>`_.
- `Библиотека libdb (BerkleyDB) будет объявлена устаревшей <https://fedoraproject.org/wiki/Changes/Libdb_deprecated>`_. Мы откажемся от нее полностью в ближайшее время.
- `Будет исправлено поведение DNF при апгрейде, когда в системе были установлены модули <https://fedoraproject.org/wiki/Changes/Module_Obsoletes_and_EOL>`_. Выходит, что зря мы вообще `эти модули <https://docs.pagure.org/modularity/>`_ придумали, что ли?
- `Начальная поддержка <https://fedoraproject.org/wiki/Changes/NetworkTimeSecurity>`_ нового протокола для синхронизации времени - `NTS <https://tools.ietf.org/html/draft-ietf-ntp-using-nts-for-ntp>`_ (NTP + TLS).
- `Удаление пакета glibc-headers <https://fedoraproject.org/wiki/Changes/RemoveGlibcHeaders>`_. Его объединят с glibc-devel, где ему и место.
- `Переход на systemd-resolved <https://fedoraproject.org/wiki/Changes/systemd-resolved>`_ для получения IP-адресов доменов.

Ну и самая долгожданная новость!

- `Новая версия Perl 5.32 <https://fedoraproject.org/wiki/Changes/perl5.32>`_.

На подходе еще пачка изменений, среди которых обсуждаемое прямо сейчас - `возможность выбирать между GCC и LLVM для сборки каждого конкретного пакета <https://fedoraproject.org/wiki/Changes/CompilerPolicy>`_.
