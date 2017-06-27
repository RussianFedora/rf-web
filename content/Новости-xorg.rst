.. title: Новости X.org
.. slug: Новости-xorg
.. date: 2012-06-15 23:45:57
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Мы уже
  `сообщали </content/Переключающаяся-графика-скоро-в-linux>`__
  о том, как все обстоит в X.org Server сейчас и в целом с иксами.

  Однако Wayland будет доступен еще нескоро (хотя уже сейчас можно
  запускать `некоторые
  X11-приложения <https://www.phoronix.com/scan.php?page=news_item&px=MTExOTM>`__
  с помощью XWayland), так что приходится что-то делать с текущей
  системой. И вот, представлена серия улучшений в X.org:

-  `David Airlie <https://www.openhub.net/accounts/airlied>`__ сообщил,
   что планирует
   `выбросить <http://lists.x.org/archives/xorg-driver-ati/2012-June/023104.html>`__
   поддержку userspace modesetting из ATI видеодорайверов. Через
   несколько часов он объявил в своей ленте Google+, что `почти
   закончил <https://plus.google.com/104877287288155269055/posts/i8LFgduJZHr>`__.

   Это, конечно, плохая новость для пользователей устаревших Unix,
   которые кстати, наконец-то
   `зашевелились <http://lists.freebsd.org/pipermail/freebsd-x11/2012-June/011952.html>`__,
   приступив к портированию KMS из Linux.

-  Предложено `расширение для
   RandR <https://www.phoronix.com/scan.php?page=news_item&px=MTExNzI>`__
   для поддержки GPU offloading и прочих вещей, необходимых для систем с
   переключаемыми GPU, поддержка которых `запланирована на сентябрь
   2012 <https://www.phoronix.com/scan.php?page=news_item&px=MTExNTg>`__.

-  `Новый DDX
   API <https://www.phoronix.com/scan.php?page=news_item&px=MTEwNjE>`__.


| 
| А в это время в Wayland реализовали `аналог
  xclock <http://lists.freedesktop.org/archives/wayland-devel/2012-June/003917.html>`__.

  Готов для десктопа!
