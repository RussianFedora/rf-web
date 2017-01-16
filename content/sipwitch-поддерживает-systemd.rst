.. title: Sipwitch поддерживает systemd
.. slug: sipwitch-поддерживает-systemd
.. date: 2014-02-19 13:35:20
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Все больше и больше проектов завязываются на systemd. Дело не в
заговоре, а в том, что `systemd хорошо решает задачи, с которыми
сталкиваются
разработчики </content/systemd-с-точки-зрения-мэйнтейнера-upstream-проекта>`__.

Вот и еще один наш коллега, `David Sugar <https://github.com/dyfet>`__,
участник коммьюнити Debian и Fedora, разработчик проекта `GNU
Telephony <http://www.gnutelephony.org/index.php/GNU_Telephony>`__,
объявил в своей ленте Google+, что центральный компонент разрабатываемой
им системы, sipwitch, `будет зависеть от
systemd <https://plus.google.com/103768631862759305185/posts/LTVEerX6h2W>`__.

Благодаря тому, что все основные Linux-дистрибутивы либо уже работают на
systemd, либо переходят на него, можно смело добавлять systemd в
зависимости. Непонятно пока, как это будет собираться на BSD, но есть
серьезные сомнения в том, что на таких системах развертывают новые
решения.

