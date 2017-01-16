.. title: WebKitGTK+ выбросят после Fedora 27
.. slug: webkitgtk-выбросят-после-fedora-27
.. date: 2016-06-13 18:15:50
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Пакеты с WebKitGTK+ в Fedora серьезно затрясло. Сначала запланировали
невзирая на поломки, срочно `обновлять пакеты до самой последней
версии <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/219943>`__,
которую планируют поддерживать стабильной некоторое продолжительное
время. А затем объявили, что `WebKitGTK+ (пакеты webkitgtk и webkitgtk3)
выбрасывают из Fedora
27 <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/219956>`__,
т.к. он дырявый, и не поддерживается. Вместо него предлагается перейти
на WebKit2 (пакеты webkitgtk4). Причем WebKit для GTK2 поддерживаться
больше не будет, т.е. приложение нужно портировать сначала на GTK3,
затем на WebKit2.

Портирование на GTK3, это еще та веселая затея. Результат все равно не
будет кросс-платформенным, и `некоторые проекты решили переходить на
Qt </content/libreoffice-медленно-переходит-на-gtk3>`__. С самим WebKit
ситуация тоже интересная. `Из Qt его выбросили в пользу Google
Blink <https://wiki.qt.io/New_Features_in_Qt_5.6>`__, но, вроде бы,
`проект QtWebKit может
возродиться <http://thread.gmane.org/gmane.comp.lib.qt.devel/26208>`__
(благодаря нашим соотечественникам).

