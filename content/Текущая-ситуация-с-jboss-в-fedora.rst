.. title: Текущая ситуация с JBoss в Fedora
.. slug: Текущая-ситуация-с-jboss-в-fedora
.. date: 2012-04-20 14:45:26
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Один из разработчиков JBoss, `Marek
Goldmann <https://www.openhub.net/accounts/goldmann>`__, в своем блоге
`подвел
итоги <http://goldmann.pl/blog/2012/04/18/impressions-after-fedora-test-day-for-jboss-application-server/>`__
прошедшего недавно `тестового дня JBoss Application Server в
Fedora <https://fedoraproject.org/wiki/Test_Day:2012-04-17_JBoss_Application_Server>`__.

Почти все тесты были успешными, и удалось заметить лишь одну ошибку,
которая уже исправляется - можно считать, что в целом оно работает!
Парни провели просто огромную заботу - упаковали и включили в Fedora
`сто с лишним библиотек и
приложений <http://fedoraproject.org/wiki/JBossAS7#Current_progress>`__.

Это было очень непросто, так как традиционно Java-приложения не
отличаются высоким уровнем внимания к вопросам их распространения.

Например, некоторые (не буду указывать конкретных имен) JBoss
разработчики считают, что достаточно того, что они поставляют все, что
нужно, в одном большом ZIP-архиве (напоминаю, что именно Java-приложения
приносят наибольшее количество проблем при соблюдении правила `**No
Bundled
Libs** </content/bundled-libraries-немного-статистики-и-комментариев-к-ней>`__).

