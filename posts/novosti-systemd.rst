.. title: Новости systemd
.. slug: novosti-systemd
.. date: 2017-07-03 18:51:49 UTC+03:00
.. tags: systemd, oops, meson
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

В systemd обнаружили баг, который `уже закрыли, как NOTABUG
<https://github.com/systemd/systemd/issues/6237>`_. Исторически заведено так,
что в Linux-системе нельзя создать пользователя с именем, начинающимся с цифры.
Однако, если в unit-файле systemd указать такого пользователя (как подсказывает
анонимный коллега-аналитик, случайно указать пользователя 0nginx), то поведение
systemd будет неожиданно - сообщение об ошибке будет выведено только, если
такого пользователя в системе не заведено, иначе сервис будет запущен от рута.
Ошибка это или нет, уже `решают анонимные комментаторы на OpenNET.ru
<https://www.opennet.ru/opennews/art.shtml?num=46798>`_

Недавно обнаружили и другую ошибку в systemd, гораздо более неприятную. При
использовании systemd-resolved, и при захвате злоумышленником контроля над
DNS-сервером, `он может прислать специальный ответ, который позволит ему
удаленно выполнить произвольный код в системе с systemd-resolved
<http://openwall.com/lists/oss-security/2017/06/27/8>`_. Уже `поправили
<https://github.com/systemd/systemd/pull/6214>`_. Бывает, что.

Сам Lennart занят другими делами. Он `переписал rsync
<http://0pointer.net/blog/casync-a-tool-for-distributing-file-system-images.html>`_,
добавив функционала из Git и назвав полученное - casync. Сразу после этого он
`написал еще одну утилиту для создания образов системы
<http://0pointer.net/blog/mkosi-a-tool-for-generating-os-images.html>`_ -
mkosi. Результат сразу пригоден для использования с systemd-nspawn, и, видимо,
для этого и затевалось.

Ставшая ежегодной конференция systemd.conf переименована в `"All Systems Go!"
<http://0pointer.net/blog/all-systems-go-2017-cfp-open.html>`_. Но особых
новостей уже не ожидаем, только истории успеха. Последний раз мы слышали про
адаптацию сервиса под systemd в марте этого года - `SSSD был переведен на
socket- и DBUS-активацию
<http://blog.fidencio.org/2017/03/sssd-dbussocket-activation-2nd-try_4.html>`_,
так что стандарт окончательно принят сообществом.

Из больших и интересных новостей о самом systemd - `собираются отказаться от
Autotools в пользу Meson <https://github.com/systemd/systemd/pull/6266>`_. На
Meson переходит все больше и больше проектов.
