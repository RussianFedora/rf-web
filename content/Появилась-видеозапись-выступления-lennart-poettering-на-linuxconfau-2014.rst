.. title: Появилась видеозапись выступления Lennart Poettering на Linux.conf.au 2014
.. slug: Появилась-видеозапись-выступления-lennart-poettering-на-linuxconfau-2014
.. date: 2014-01-12 14:29:50
.. tags: kdbus, firefox, gstreamer, html5
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Появилась видеозапись выступления Lennart Poettering на конференции
`Linux.conf.au 2014 <http://linux.conf.au/>`__, на которой рассказал о
kdbus, и его текущем состоянии:

.. raw:: html

        <center> <video controls="" width="768" height="576"><source src="http://mirror.linux.org.au/pub/linux.conf.au/2014/Friday/104-D-Bus_in_the_kernel_-_Lennart_Poettering.mp4" type="video/mp4"></video></center>


Для пользователей Firefox, у которых не показывается видео, мы хотим
сообщить, что недавно в Fedora `наконец-то Firefox был собран с
поддержкой
gstreamer <http://koji.fedoraproject.org/koji/buildinfo?buildID=489157>`__
(вы уже `могли слышать о планах на
это </content/Когда-в-fedora-будет-firefox-с-поддержкой-gstreamer>`__).

Пока собрали лишь для Rawhide (Fedora 21), но по счастливому совпадению,
получившиеся пакеты спокойно ставятся в Fedora 20, так что можете с
известной осторожностью пробовать. Еще вам понадобится установить
следующие пакеты - gstreamer-plugins-bad, gstreamer-plugins-ugly,
gstreamer-ffmpeg (как можно заметить, наши мэйнтейнеры решили не ждать
перевода Firefox на gstreamer1).

**УПД:** еще очень желательно установить `YouTube ALL
HTML5 <https://addons.mozilla.org/en-US/firefox/addon/youtube-all-html5/>`__
плагин для Firefox, который позволит переключать ролики ютуба на HTML5
принудительно.

