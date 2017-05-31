.. title: Вышел NetworkManager 1.4
.. slug: Вышел-networkmanager-14
.. date: 2016-09-02 16:48:46
.. tags: networkmanager
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Наш коллега, Lubomir Rintel,
`анонсировал <https://blogs.gnome.org/lkundrak/2016/08/24/networkmanager-1-4/>`__
выход NetworkManager версии 1.4. `Новость уже обсуждалась на
OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=45026>`__.

В этой версии продолжилась работа над манипуляциями с MAC-адресами, о
которой `мы вам уже
рассказывали </content/networkmanager-перешел-на-gdbus>`__. Напомним,
что использование полностью случайно генерируемого MAC-адреса имеет
побочный эффект. Некоторые провайдеры привязывают авторизацию к
MAC-адресу, поэтому постоянно выдавать случайный MAC будет не очень
удобно для пользователя. Для этих случаев было предусмотрен режим
работы, когда MAC генерируется случайно, но в дальнейшем в указанной
сети не меняется. Подробнее об этом нововведении
`рассказал <https://blogs.gnome.org/thaller/2016/08/26/mac-address-spoofing-in-networkmanager-1-4-0/>`__
в своем блоге наш коллега, инженер Red Hat, `Thomas
Haller <https://www.openhub.net/accounts/thom311>`__.
