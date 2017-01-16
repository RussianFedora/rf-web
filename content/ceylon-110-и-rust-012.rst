.. title: Ceylon 1.1.0 и Rust 0.12
.. slug: ceylon-110-и-rust-012
.. date: 2014-10-14 18:42:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Gavin King <https://www.openhub.net/accounts/gavinking>`__ объявил о
выходе `Ceylon
1.1.0 <http://ceylon-lang.org/blog/2014/10/09/ceylon-1/>`__. Анонс уже
`обсуждают коллеги-аналитики на
OpenNET.ru <http://www.opennet.ru/opennews/art.shtml?num=40796>`__. В
целом нам кажется интересной идея языка, одинаково хорошо работающего и
в JVM, и в виртуальной машине JS, например в Node.js. Похоже, что у Red
Hat есть планы на мобильные приложения - не с этим ли связана `покупка
Red Hat компании
FeedHenry <http://www.redhat.com/en/about/press-releases/red-hat-acquire-feedhenry-adds-enterprise-mobile-application-platform>`__?
Печально, но пока язык Ceylon даже не включен в репозитории Fedora, и
чтоб попробовать его, нужно собирать самому.

Другой интересный язык, `новая версия которого была недавно
анонсирована <http://thread.gmane.org/gmane.comp.lang.rust.devel/11188>`__
и `уже тоже обсуждается коллегами-аналитиками на
OpenNET.ru <http://www.opennet.ru/opennews/art.shtml?num=40791>`__, это
`Rust <http://www.rust-lang.org/>`__. Его не то, что нет в репозиториях,
но раньше он даже не собирался в Fedora 20 и старше, настолько он
инновационен. Зато начиная с Fedora 21, и с его версии 0.12 он хоть
собирается. Язык довольно интересен. Например, `его сборщик мусора умеет
самостоятельно закрывать сокеты, файлы и освобождать прочие системные
ресурсы <http://blog.skylight.io/rust-means-never-having-to-close-a-socket/>`__.

Стоит попробовать, хотя будьте готовы к тому, что в отличие от
`Golang <https://golang.org/>`__ его синтаксис плывет от версии к
версии.

