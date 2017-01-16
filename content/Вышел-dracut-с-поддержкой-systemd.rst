.. title: Вышел dracut с поддержкой systemd
.. slug: Вышел-dracut-с-поддержкой-systemd
.. date: 2012-06-21 11:35:44
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Сегодня мэйнтейнер
`dracut <https://plus.google.com/116442056808259194967/about>`__ `Harald
Hoyer <https://www.ohloh.net/accounts/backslash>`__ объявил, что
`последняя версия будет полностью поддерживать
systemd <https://plus.google.com/117537647502636167748/posts/X5ApJWecafm>`__,
как систему первоначальной загрузки внутри initramfs.

Те, кто внимательно читают "Пульс проекта", `уже могли
слышать </content/Вышел-первый-релиз-systemd-после-слияния-с-udev>`__
об этом изменении. Теперь загрузка на системах с initramfs будет
полностью бесшовной, с передачей всех логов ранних этапов в syslog и еще
большим ускорением. Например, обратим внимание на результаты загрузки
системы с 12 SATA-дисками:
"Старый" initramfs без systemd:
*``Startup finished in 2547ms (kernel) + 3843ms (initramfs) + 15746ms (userspace) = 22137ms``*
"Новый" initramfs с systemd:
*``Startup finished in 3103ms (kernel) + 4253ms (initramfs) + 8824ms (userspace) = 16181ms``*
Наверное не надо и говорить, что без systemd эта же машинка загружалась
дольше минуты. Пакет с новой версией уже доступен в Rawhide (будущая
Fedora 18). Ждем systemd в RHEL 7!
