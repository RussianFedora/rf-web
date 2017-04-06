.. title: Прекратите отключать selinux (и не принимайте советов от Valve)
.. slug: Прекратите-отключать-selinux-и-не-принимайте-советов-от-valve
.. date: 2014-03-07 23:33:29
.. tags: selinux, security, valve, canonical
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

`Мы не раз предупреждали </content/Прекратите-отключать-selinux>`__, что
SELinux не "глючит", а блокирует реальные проблемы в приложениях, и отключать
его не нужно. Если уж очень приспичило, то лучше переводить в режим permissive,
но не отключать. Конечно, из-за ошибок в библиотеках бывает, что `приложение
при SELinux в режиме permissive ведет себя иначе
</content/Почему-приложения-при-selinux-в-режиме-permissive-порой-работают-неправильно>`__,
чем при полностью выключенном SELinux, но эти случаи нечасты, и наши коллеги их
быстро поправят, если пользователи сообщат о подобной ситуации. Наш коллега,
`Elad Alfassa <https://fedoraproject.org/wiki/User:Elad>`__, обратил наше
внимание на `характерный багрепорт
<https://github.com/ValveSoftware/portal2/issues/50>`__.

Пользователь сообщает в багтрекере Valve, что `недавно выпущенная под Linux
игра Portal 2 <https://www.linux.org.ru/news/games/10226975>`__ не работает,
вываливаясь с ошибкой. Оказалось, что mp3-декодер в игре требует execheap (о
вредности execheap в свое время писали вице-президент Goldman Sachs, бывший
инженер Red Hat, `Ulrich Drepper
<http://www.akkadia.org/drepper/selinux-mem.html>`__, и нынешний мэйнтейнер
SELinux, `Dan Walsh <http://danwalsh.livejournal.com/6117.html>`__). Однако,
вместо изучения ошибки, какой-то из инженеров Valve `просто закрыл тикет
<https://github.com/ValveSoftware/portal2/issues/50#issuecomment-36927497>`__,
порекомендовав отключить SELinux. Выяснилось, что ситуация типична для Valve!
Видимо изначальная ориентация на дистрибутив для начинающих, с искусственно
заниженными стандартами (в т.ч. и по безопасности), привела к тому, что
инженеры Valve порой просто не понимают, о чем речь!

- `Team Fortress 2 on Fedora requires selinux execheap enabled
  <https://github.com/ValveSoftware/steam-for-linux/issues/43>`__
- `SELinux is preventing /home/michael/Steam/ubuntu12\_32/steam from using the
  execheap access on a process.
  <https://github.com/ValveSoftware/steam-for-linux/issues/88>`__
- `Reproducible crash entering Big Picture on Fedora 17 x64
  <https://github.com/ValveSoftware/steam-for-linux/issues/375>`__
- `Steam client cause SELinux alert on Fedora 18
  <https://github.com/ValveSoftware/steam-for-linux/issues/1471>`__
- `Steam uses 'execheap' which according to expert ' is really a bad idea'
  <https://github.com/ValveSoftware/steam-for-linux/issues/2028>`__
- `Steam, HL2 & TF2 have a security exploit in Ubuntu
  <https://github.com/ValveSoftware/steam-for-linux/issues/2073>`__
- `Steam crashes and fails to upload dump
  <https://github.com/ValveSoftware/steam-for-linux/issues/2243>`__
- `Steam client crashes after message from friend is received
  <https://github.com/ValveSoftware/steam-for-linux/issues/2470>`__

И т.п. В ходе разборок выяснилось, что инженеры Valve для проигрывания музыки
выбрали не открытое решение, а проприетарную библиотеку. Вероятно, для
кросс-платформенности, по лицензионным соображениям, а может просто по привычке
- как привыкли в Windows, так и полезли в Linux.

Обратите внимание, в некоторых комментариях четко видно, что ряд инженеров
Valve и помогавших им на начальных этапах, до перехода SteamOS на Debian,
инженеров Canonical всерьез утверждали, что это "баг с SELinux", что характерно
для начинающих пользователей Linux. И только недавно начало сквозить понимание,
что это виноват не SELinux, а приложения (mp3-библиотека), которые просто
дырявы (а SELinux просто это сообщает в `простой и понятной манере
</content/dan-walsh-представил-интеграцию-journald-и-selinux>`__).

Случай получился очень показательный. Тут и проприетарный быдлокод, для хоть
какой-то работы которого надо отключать SELinux, и дремучее неприятие и
недопонимание ситуации со стороны начинающих пользователей Linux и тех, кто в
повседневной жизни пользуется дистрибутивами без SELinux (с искусственно
заниженными требованиями безопасности). Но надо отметить и прозрачность и
гласность процесса, что позволило быстро привлечь внимание к ситуации. Это,
конечно, может стать очень сильной стороной Valve. Практика показывает, что
широкое вовлечение участников коммьюнити поможет исправить и гораздо более
тяжелые ситуации - вот почему мы, в отличие от других проектов, всячески
рекомендуем и стимулируем наших коллег и товарищей принимать деятельное участие
в жизни и нашего коммьюнити, и upstream-проектов.

Присоединяйтесь к нам и вы!

Upd. Завязалось интересное обсуждение ситуации с Valve и SELinux на `Reddit
<http://www.reddit.com/r/linux_gaming/comments/1zqv3d/valve_shows_once_more_they_dont_give_a_shit_about/>`__.

