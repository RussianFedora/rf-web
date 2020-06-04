.. title: Firefox 77 и аппаратное ускорение на Wayland
.. slug: firefox-77-i-apparatnoe-uskorenie-na-wayland
.. date: 2020-06-04 22:26:37 UTC+03:00
.. tags: firefox, wayland, bundled libs, vaapi
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

`Вышел Firefox 77 <https://www.mozilla.org/en-US/firefox/77.0/releasenotes/>`_
(новость уже обсуждается на `Linux.org.ru
<https://www.mozilla.org/en-US/firefox/77.0/releasenotes/>`_ и `OpenNET.ru
<https://www.opennet.ru/opennews/art.shtml?num=53072>`_).

Мы, конечно, рекомендуем устанавливать приложение из репозитория, потому что в
нем есть дополнительная функциональность, которая может быть вам интересна.
Например, у нас есть `аппаратное ускорение видео в Firefox
<https://mastransky.wordpress.com/2020/06/03/firefox-on-fedora-finally-gets-va-api-on-wayland/>`_.
Функциональность была реализована нашими коллегами `и уже рассматривается в
upstream <https://bugzilla.mozilla.org/show_bug.cgi?id=1619523>`_, так что
вскоре будет доступна и в других дистрибутивах. Пока поддерживается только
видеокарты Intel и AMD, но, наверное, рано или поздно будет поддержка и для
NVidia. Для ускорения нужно будет дополнительно установить пакеты ffmpeg, libva
и libva-utils. К сожалению, поддерживаются не все кодеки - только
H.264/VP8/VP9. На YouTube используется AVC1, а внутри Firefox еще и придется
отключить bundled libvpx (еще одно доказательство, что `bundled libs
</content/bundled-libraries-немного-статистики-и-комментариев-к-ней>`_, это
зло). Полагаем, что вскоре все эти настройки не будут требоваться.
