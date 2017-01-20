.. title: Поддержка голосовых кодеков в Fedora
.. slug: Поддержка-голосовых-кодеков-в-fedora
.. date: 2012-09-13 17:07:34
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Как многие уже слышали, IETF одобрило
`принятие <http://www.opennet.ru/opennews/art.shtml?num=34812>`__
`стандартом <https://www.linux.org.ru/news/multimedia/8221347>`__
новейшего универсального аудиокодека от Xiph.org - Opus. В репозиториях
Fedora он доступен с ноября 2011 (пока еще не в EPEL), и
заинтересованные разработчики уже используют его в своих проектах, а вот
пользователям повезло чуть меньше. Firefox пока собран без его
поддержки, а `gstreamer собран с его поддержкой совсем
недавно <https://bugzilla.redhat.com/show_bug.cgi?id=845764#c4>`__.

Другие пользовательские приложения пока не собраны с его поддержкой.

Ситуация с iLBC, `о котором мы уже
рассказывали </content/ситуация-с-аудиокодеком-ilbc-в-fedora>`__, еще
немного улучшилась - `пакет с ним прошел
review <https://bugzilla.redhat.com/show_bug.cgi?id=845221>`__ и `собран
для всех актуальных версий Fedora и
EPEL <https://admin.fedoraproject.org/updates/search/ilbc>`__. Теперь
ждем пересборки VoIP/IM-приложений с ним.

