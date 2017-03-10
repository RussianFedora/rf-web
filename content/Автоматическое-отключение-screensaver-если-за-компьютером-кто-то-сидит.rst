.. title: Автоматическое отключение screensaver, если за компьютером кто-то сидит
.. slug: Автоматическое-отключение-screensaver-если-за-компьютером-кто-то-сидит
.. date: 2012-06-26 14:28:42
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Активный участник Fedora `Harald
Hoyer <https://www.openhub.net/accounts/backslash>`__ в своей ленте
Google+ предложил proof-of-concept `автоматического отключения
screensaver в случае, когда кто-то сидит за
компьютером <https://plus.google.com/117537647502636167748/posts/9raMStT26sY>`__.

Используется встроенная видеокамера и библиотека
`OpenCV <http://opencv.willowgarage.com/wiki/>`__ (написанная при
`активном участии наших
соотечественников <https://habrahabr.ru/company/itseez/blog/146434/>`__,
между прочим). Harald предлагает разработчикам различных Desktop
Environment использовать его подход, как базис для чего-то более
функционального. Разумеется, это внесет еще одну зависимость - OpenCV.

