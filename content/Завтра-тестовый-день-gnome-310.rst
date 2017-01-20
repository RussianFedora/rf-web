.. title: Завтра тестовый день GNOME 3.10
.. slug: Завтра-тестовый-день-gnome-310
.. date: 2013-10-09 14:41:34
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Всех приглашаем принять участие в `тестовом дне GNOME
  3.10 <https://fedoraproject.org/wiki/Test_Day:2013-10-10_Gnome_3.10>`__,
  который запланирован на **10-е октября**. Рекомендуем принять участие,
  даже если вы не используете Fedora. Например, пользователи Ubuntu в
  основном используют GNOME, чаще всего замаскированный небольшим
  сторонним компонентом, разработанным силами немногочисленных
  разработчиков Canonical, Unity, так что для них было б полезно
  попробовать нововведения.

| Тестовый день, это понятие растяжимое, и если не успеете сегодня, то
  поучаствуйте завтра или послезавтра.

| `Выход GNOME 3.10 уже обсуждался аналитиками ведущего интернет-сайта
  по Linux тематике <http://www.linux.org.ru/news/gnome/9626978>`__, и
  его нововведения (о которых можно, например, `почитать в блоге нашего
  коллеги, Bastien
  Nocera <http://www.hadess.net/2013/09/gnome-310-is-coming.html>`__)
  для нас уже не так уж и в новинку - ну Wayland, ну HiDPI, ну
  интеграция с большим количеством интернет-сервисов, таких, как Flickr,
  OpenStreetMap, ну более лучшее оформление. А нам уже интересно, что же
  будет в GNOME 3.12? Наш коллега, `Matthias
  Clasen <http://fedoraproject.org/wiki/User:Mclasen>`__ `начал
  планирование фич GNOME
  3.12 <https://wiki.gnome.org/ThreePointEleven/Features>`__, среди
  которых

-  Интеграция с Facebook в приложении GNOME Photos.

-  Управление git-репозитариями. Это перспективный план, с прицелом на
   будущую Gnome IDE.

-  Интеграция с journald и с systemd --user для сессий. FVWM уже
   интегрирован, так что дело за GNOME. Ну т.е. теперь systemd
   становится обязательной зависимостью для GNOME не только де-факто (о
   чем `мы уже
   говорили </content/Короткие-новости-про-основные-компоненты-системы-base-os>`__),
   но и де-юре.

-  Новые приложения - IRC клиент под названием Polari, Gnome Sound
   Recorder, и новый интерфейс у приложения для проигрывания видео.

-  Интеграция с Windows Live.

-  Интеграция с Zimbra.

-  Завершение портирования на Wayland.


| 
| Работы довольно много, но участники Fedora дела не боятся - работают
  над GNOME и в рамках должностных обязанностей, и просто так, и в
  рамках учебных программ, например Google Summer of Code. В этом году,
  в GSoC от GNOME участвовал наш коллега, `Kalev
  Lember <https://www.openhub.net/accounts/klember>`__, и не так давно он
  подвел `итог его участию в этом
  проекте <http://blogs.gnome.org/kalev/2013/09/24/wrapping-up-summer-of-code/>`__.

  GSoC этого года уже завершен, а мы рекомендуем студентам и аспирантам
  уже начать готовиться `к GSoC 2014, который уже
  анонсирован <http://www.opennet.ru/opennews/art.shtml?num=38111>`__.

| По переносу на Wayland, как обычно идут `согласно озвученному
  графику </content/Планы-gnome-на-wayland>`__. `GNOME 3.10 уже работает
  в Fedora
  20 <https://plus.google.com/100767727489577050265/posts/41KMBwqQ6tV>`__,
  и `есть инструкция по
  запуску <http://gcampax.blogspot.ru/2013/10/every-frame-matters.html>`__
  (и `еще одна от Matthias
  Clasen <http://blogs.gnome.org/mclasen/2013/10/03/gnome-wayland-in-fedora/>`__),
  правда степень работоспособности зависит от видеокарты. Пока
  поддерживается только Intel, а для карт AMD и NVIDIA потребуется
  собрать
  `xf86-video-wlglamor <https://github.com/axeldavy/xf86-video-wlglamor>`__,
  видеодрайвер, использующий
  `Glamor <http://www.freedesktop.org/wiki/Software/Glamor/>`__. А ведь
  еще есть
  `xf86-video-wayland <http://cgit.freedesktop.org/xorg/driver/xf86-video-wayland/>`__
  (который `включают в Fedora <https://bugzilla.redhat.com/1015162>`__,
  и который будет использоваться для XWayland) и
  `xf86-video-wlshm <http://cgit.freedesktop.org/~daniels/xf86-video-wlshm/>`__.

  Все это выглядит не очень прямо, но главное, что процесс идет.

| Кроме GTK3, Qt5 `также вполне работоспособен в
  Wayland <https://plus.google.com/103747673045238156202/posts/VEVVxaykKJ5>`__.

  На скриншоте, кстати, `Hawaii
  Desktop <https://github.com/hawaii-desktop>`__, альтернативное DE,
  использующее Qt5 и Wayland. Включение его в Fedora `запланировано на
  22й релиз <https://fedoraproject.org/wiki/Changes/Hawaii_Desktop>`__,
  ради чего его основной разработчик, Pier Luigi Fiorini, `перешел с
  Arch Linux на Fedora
  Rawhide <https://plus.google.com/117319527836202971314/posts/XkrS8NR6iq9>`__.

