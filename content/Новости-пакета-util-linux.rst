.. title: Новости пакета util-linux
.. slug: Новости-пакета-util-linux
.. date: 2012-05-21 10:28:32
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Мэйнтейнер и основной разработчик пакета
`util-linux <https://en.wikipedia.org/wiki/Util-linux>`__, инженер Red
Hat и участник Fedora `Karel
Zak <https://www.openhub.net/accounts/kzak>`__ поделился `последними
новостями <http://karelzak.blogspot.com/2012/05/eject1-sulogin1-wdctl1.html>`__.

В состав пакета теперь входит полностью переписанная утилита *eject*,
ранее распространявшаяся в виде отдельного пакета, развитие которого
было остановлено несколько лет назад. Karel переделал ее совместно с
молодым инженером Red Hat, Michal Luscon, который попал на эту должность
благодаря `своему
участию <https://fedoraproject.org/wiki/Summer_Coding_2010_student_application_-_Michal_Luscon>`__
`в летних Open Source
инициативах <https://fedoraproject.org/wiki/Summer_Coding>`__ от Fedora
и Google - напоминаем студентам, что активное участие в Open Source
проектах, это возможно самая ценная строчка в вашем резюме. А ведь порой
оно и оплачивается, как в `Google Summer of
Code </content/fedora-%D0%B8-google-summer-code-2012>`__.

Также продолжается работа по адаптации userspace ПО под нужды systemd -
в состав пакета включена еще одна утилита из пакета sysvinit-tools
(предназначенного для устаревшей системы инициализации), *sulogin*. В
предыдущих версиях была перенесена из того же sysvinit-tools утилита
*mountpoint*.
Появилась новая утилита - *wdctl*, первый вариант которой написал
`Lennart Poettering <https://www.openhub.net/accounts/mezcalero>`__. Она
предназначена для получения текущего состояния с watchdog. К сожалению,
пока у программы есть серьезные ограничения, но Karel обещает вскоре их
устранить.

