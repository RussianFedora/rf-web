.. title: systemd на ChromeOS
.. slug: systemd-на-chromeos
.. date: 2016-07-22 16:54:53
.. tags: google, android, chromeos, selinux, pulseaudio, wayland, upstart, systemd, coreos, intel
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Потихоньку идет процесс перевода операционок от Google на современные
компоненты. Несмотря на то, что Chrome OS и Android не будут сливаться в
одну систему (т.е. `будут, но путем переноса фич
туда-сюда <http://venturebeat.com/2016/05/22/google-isnt-merging-android-and-chrome-os-its-just-stealing-their-best-parts/>`__,
а обои будут разные), и та, и эта системы пока технологически отстают от
дистрибутивов линукса. Например, `SELinux в Android включили лишь в 2012
году </content/android-начал-использование-selinux>`__, что гораздо
позже Fedora / RHEL (ну, кстати, в Ubuntu его до сих пор нет, что сильно
подрывает и `без того плохую ситуацию с безопасностью этого
дистрибутива </content/Ситуация-с-безопасностью-скачивания-дистрибутивов-и-обновлений-к-ним>`__).

`PulseAudio и Wayland были доступны на Android в качестве очень очень
экспериментальной сборки от стороннего
разработчика </content/pulseaudio-и-wayland-переносят-на-android>`__. Но
самая плохая ситуация была с системой инициализации. В Chrome OS до сих
пор используется Upstart, а в Android `самописная система инициализации
-
init <https://android.googlesource.com/platform/system/core/+/master/init>`__.

К счастью, благодаря тому, что Chrome OS основана на Gentoo, сменить
init-систему на systemd не так и сложно, что `продемонстрировали
разработчики CoreOS, заменившие Upstart на
systemd </content/coreos-новый-дистрибутив-на-базе-chromeos>`__. Тем не
менее, пока Chrome OS официально использовал лишь устаревший и
малофункциональный Upstart.

Неожиданно выяснилось, что `инженеры Intel уже несколько месяцев
работают над возможностью использовать стандартное дерево Chrome OS с
systemd <https://bugs.chromium.org/p/chromium/issues/detail?id=583671>`__.

Пока непонятно, насколько полно поддерживается systemd в Chrome OS, но
новость позитивная.

