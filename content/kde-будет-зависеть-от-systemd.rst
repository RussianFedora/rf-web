.. title: KDE будет зависеть от systemd
.. slug: kde-будет-зависеть-от-systemd
.. date: 2014-08-15 14:52:44
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


KDE теперь будет зависеть от systemd. Ну, пока не очень сильно, но если
вы выберете вариант для Wayland, то kwin\_wayland скоро будет требовать
наличия logind. Об этом нам сообщил `Martin
Gräßlin <https://www.openhub.net/accounts/mgraesslin>`__ в `своей ленте
Google+ <https://plus.google.com/+MartinGräßlin/posts/Pw31EE21BXV>`__.

Мы уже устали говорить, что systemd, это будущее, и прятаться от него
вам не стоит - все равно не получится, т.к. `уже больше двух лет назад
было решено избавляться от общих компонентов в популярных DE, вынося их
в
systemd </content/Часть-функциональности-gnome-kde-и-xfce-переносят-в-systemd>`__.

Конечно, дистрибутивов без systemd уже почти не осталось, и несколько
оставшихся постепенно перейдут на него по умолчанию. Как вы думаете,
когда Gentoo откажется от своего велосипеда, OpenRC?
