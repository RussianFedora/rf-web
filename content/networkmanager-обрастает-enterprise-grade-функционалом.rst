.. title: NetworkManager обрастает Enterprise-grade функционалом
.. slug: networkmanager-обрастает-enterprise-grade-функционалом
.. date: 2014-03-12 23:14:27
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Основной аудиторией NetworkManager становятся не наши коллеги с
ноутбуками, подключающиеся к Wi-Fi, а пользователи серверных / облачных
систем. У них одним из требований к приложению обычно является "ничего
лишнего", и `Dan Williams <https://www.openhub.net/accounts/dcbw>`__ пошел
им навстречу. Недавно он `анонсировал отделение от NetworkManager ряда
функциональных
компонентов <http://blogs.gnome.org/dcbw/2014/03/04/spin-class/>`__. В
отдельные плугины были выделен функционал по управлению соединениями
ATM, Bluetooth, и WWAN. В дальнейшем Dan планирует выделить управление
WLAN в отдельный плагин, т.к. оно зачастую `не
нужно <https://lurkmore.to/Не_нужен>`__ в виртуалках.

Но не только перераспределением кода внутри NM заняты наши коллеги.

Недавно участник проектов Fedora и GNOME, инженер Red Hat, `Dan
Winship <https://fedoraproject.org/wiki/User:Danw>`__, уже известный вам
по `работе над новым CLI для NetworkManager, основанным на
curses </content/Короткие-новости-18>`__ и по `удалению кода из
Glib </content/Из-glib-удалили-поддержку-операционных-систем-из-1990х>`__,
за два коммита включил в NM
`поддержку <http://cgit.freedesktop.org/NetworkManager/NetworkManager/commit/?id=4bfb430>`__
`VxLAN <http://cgit.freedesktop.org/NetworkManager/NetworkManager/commit/?id=42df06e>`__
(см. `статью в
википедии <https://ru.wikipedia.org/wiki/Virtual_Extensible_LAN>`__).

Работа заняла у него более полугода, и проводилась в рамках `разработки
RHEL 7 <https://bugzilla.redhat.com/1066705>`__. А вы, кстати, в вашем
облаке используете SDN или bridge?
