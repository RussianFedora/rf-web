.. title: GNOME и другие проекты переезжают на GitLab
.. slug: gnome-i-drugie-proekty-pereezzhaiut-na-gitlab
.. date: 2018-06-04 11:56:36 UTC+03:00
.. tags: gnome, freedesktop, mesa, gimp, gitlab, pagure, github, microsoft, docker
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

В последний месяц было довольно много анонсов миграций крупных проектов с
каких-то базовых Git-хостингов на GitLab. Сначала `FreeDesktop объявил, что
переходит на GitLab
<https://lists.freedesktop.org/archives/mesa-dev/2018-May/195634.html>`_ (но
там все только началось), а закончился месяц с официальным `объявлением о
перезде на GitLab от проекта GNOME
<https://www.gnome.org/news/2018/05/gnome-moves-to-gitlab-2/>`_. Гномеры
`переезжали практически целый год
<https://www.mail-archive.com/desktop-devel-list@gnome.org/msg28741.html>`_,
так что у FreeDesktop все только началось. Например, `переезд Mesa стартовал
несколько дней назад
<https://lists.freedesktop.org/archives/mesa-dev/2018-May/195634.html>`_.

Проект GIMP `тоже наконец-то решился перейти на GitLab
<https://www.gimp.org/news/2018/05/31/gimp-has-moved-to-gitlab/>_`. Будем
надеяться, что переход на современную платформу улучшит ситуацию с
прозрачностью всего процесса разработки.

Даже Debian `сменили свой устаревший форк SourceForge
<https://www.linux.org.ru/news/debian/14236552>`_, alioth.debian.org, `на
GitLab <https://salsa.debian.org/public>`_.

Проблема с GitLab, насколько мы помним, ровно одна - его тяжело поддерживать
самостоятельно. В Fedora GitLab включить так и не получилось, `хотя пытались
<https://fedoraproject.org/wiki/GitLab>`_. Наши коллеги, окончательно
отчаявшись разбраться с его кодовой базой, даже написали свой Git-хостинг, `Pagure
<https://pagure.io>_`.

Но посмотрим. Возможно с ростом популярности, кодовая база GitLab
стабилизируется, и техподдержка упростится. Строго говоря, основной конкурент -
GitHub, вообще проприетарен, и поддерживать его самостоятельно просто
невозможно. К счастью, переход с GitHub на GitLab `крайне прост
<https://docs.gitlab.com/ee/user/project/import/github.html>`_.

Если кто не знает, функция перехода на GitLab будет востребована в ближайшее
время, так как говорят, что `Microsoft покупает GitHub
<https://www.bloomberg.com/news/articles/2018-06-03/microsoft-is-said-to-have-agreed-to-acquire-coding-site-github>`_.
Это `плохая
<https://jacquesmattheij.com/what-is-wrong-with-microsoft-buying-github>`_ и
`предсказуемая <https://twitter.com/jasonfried/status/430871267881672704>`_
новость, поэтому мы в целом ожидали чего-то подобного. Гитлабовцы новостью
довольны, и `еле скрывают эмоции
<https://about.gitlab.com/2018/06/03/microsoft-acquires-github/>`_.

Кстати, следите за Docker Hub - там точно такая же ситуация (кровоточащий
деньгами, но крайне популярный сервис).
