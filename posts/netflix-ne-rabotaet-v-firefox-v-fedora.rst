.. title: Netflix не работает в Firefox в Fedora
.. slug: netflix-ne-rabotaet-v-firefox-v-fedora
.. date: 2017-04-10 18:55:23 UTC+03:00
.. tags: netflix, firefox, html5
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Наш коллега, `Jiří Eischmann <https://plus.google.com/112174839778779720402/about>`_, которому не повезло быть платным клиентом неудобного проприетарного т.н. "легального" стриминг-сервиса Netflix, поделился своей проблемой - `Netflix блокирует пользователей Fedora по юзерагенту в браузере Firefox <https://eischmann.wordpress.com/2017/04/10/netflix-blocks-fedora-users/>`_. Причем, все выглядит так, что блокируют они только Fedora, т.к. если заменить это слово в User-Agent, скажем, на название другого дистрибутива, то включается их HTML5-плейер.

Технически, они не блокируют, а переключают на страницу с плейером на основе Silverlight, но понятно, что это считай что просто блокировка.

Мы очень опечалены тем, что `Иржи так приходится страдать из-за того, что он сознательно выбрал честный легальный неудобный сервис, вместо удобного нелегального <https://lurkmore.to/%D0%9C%D1%8B%D1%88%D0%B8_%D0%BF%D0%BB%D0%B0%D0%BA%D0%B0%D0%BB%D0%B8,_%D0%BA%D0%BE%D0%BB%D0%BE%D0%BB%D0%B8%D1%81%D1%8C%E2%80%A6>`_, и надеемся, что Netflix пропатчит свой фронтэнд.

.. raw:: html

        <iframe src="//coub.com/embed/izw34?muted=false&autostart=false&originalSize=false&startWithHD=false" allowfullscreen="true" frameborder="0" width="640" height="400"></iframe>

.. class:: align-center

**Когда друзья просят тебя рассказать про волшебный мир torrent-сайтов, где есть всё!**
