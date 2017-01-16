.. title: А мы пойдем в обход. Github over SOCKS.
.. slug: А-мы-пойдем-в-обход-github-over-socks
.. date: 2014-12-03 22:57:02
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


Методы использования github.com после блокировки:

-  Запуск ssh сессии из консоли (топорно)
-  Запуск ssh сессии через systemd (используя ssh)
-  Запуск ssh сессии через systemd (используя autossh)

| SSH нужен для того, чтобы поднять прокси. Дальше будет необходимо
  настроить браузер и gitconfig для использования socks-прокси для
  github.com.

| **Из консили (топорно)** `` $ ssh -ND 9876 username@example.com``
| Последние 2 метода очень похожи. Один использует ssh, а другой autossh
  для более удобного реконнекта после обрыва соединения.

| **Через systemd (ssh)**
| Копируем содержимое ниже в

::

    ~/.config/systemd/user/ssh-proxy.service

`` [Unit] Description=SSH proxy After=network.target  [Service] ExecStart=/usr/bin/ssh -NTC -D 9876 -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes username@example.com RestartSec=3 Restart=always  [Install] WantedBy=multi-user.target``
Запускаем

::

    $ systemctl --user daemon-reload && systemctl --user start ssh-proxy

| .
| **Через systemd (autossh)**
| Копируем содержимое ниже в

::

    ~/.config/systemd/user/ssh-proxy.service

`` [Unit] Description=SSH proxy After=network.target  [Service] Environment="AUTOSSH_GATETIME=0" ExecStart=/usr/bin/autossh -M 9999 -ND 9876 -o TCPKeepAlive=yes username@example.com  [Install] WantedBy=multi-user.target``
Запускаем

::

    $ systemctl --user daemon-reload && systemctl --user start ssh-proxy

| .
| **Настраиваем браузер**
| Ставим расширение `FoxyProxy <http://getfoxyproxy.org/>`__. Открываем
  настройки плагина. Следуем картинкам.

| |1| |2| |3| |4| |5| Теперь для github.com у нас используется локальный
  socks-прокси.

| **Настраиваем gitconfig**
  `` $ git config --global http.proxy "socks5://localhost:9876"``
| Если негодяй-провайдер вам отпилил ещё и [STRIKEOUT:ногу]\ ssh, то
  настраиваем

::

    ~/.ssh/config

| `` Host github.com     ProxyCommand nc --proxy-type socks5 --proxy localhost:9876 %h %p``
| **Ссылки**

-  https://wiki.archlinux.org/index.php/Secure\_Shell#Run\_Autossh\_automatically\_at\_boot\_via\_systemd
-  https://github.com/ignatenkobrain/ssh-proxy

.. |1| image:: http://ru.fedoracommunity.org/sites/default/files/pulse/Screenshot%20from%202014-12-03%2022%3A44%3A51.png
.. |2| image:: http://ru.fedoracommunity.org/sites/default/files/pulse/Screenshot%20from%202014-12-03%2022%3A45%3A09.png
.. |3| image:: http://ru.fedoracommunity.org/sites/default/files/pulse/Screenshot%20from%202014-12-03%2022%3A45%3A19.png
.. |4| image:: http://ru.fedoracommunity.org/sites/default/files/pulse/Screenshot%20from%202014-12-03%2022%3A45%3A35.png
.. |5| image:: http://ru.fedoracommunity.org/sites/default/files/pulse/Screenshot%20from%202014-12-03%2022%3A45%3A46.png

