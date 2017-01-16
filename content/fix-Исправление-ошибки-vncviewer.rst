.. title: [FIX] Исправление ошибки vncviewer
.. slug: fix-Исправление-ошибки-vncviewer
.. date: 2012-09-02 15:55:42
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: elemc

**Это архивная статья**


На данный момент, начиная с Fedora 15 vncviewer (из пакета tigervnc)
некорректно отображает шрифты в русской локали.

Ошибка уже набившая оскомину как пользователям
`RFRemix <http://redmine.russianfedora.ru/issues/631>`__ в частности,
так и пользователям
`Fedora <https://bugzilla.redhat.com/show_bug.cgi?id=725218>`__ в общем.

*Akira TAGOH* предложил `решение
проблемы <https://bugzilla.redhat.com/attachment.cgi?id=594340>`__.

Мы проверили патч - он действительно работает.

В хранилище RFRemix fixes пересобранный пакет уже есть.

Для тех, кто не пользуется RFRemix - пакет можно взять
`отсюда <http://koji.russianfedora.ru/koji/buildinfo?buildID=1764>`__
или
`отсюда <http://koji.russianfedora.ru/koji/buildinfo?buildID=1765>`__ .
Надеемся, что в скором будущем данный пакет пересоберут и в хранилище
Fedora.

