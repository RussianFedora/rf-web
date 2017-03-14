.. title: Истекли патенты на PTP (Precision Time Protocol)
.. slug: Истекли-патенты-на-ptp-precision-time-protocol
.. date: 2012-09-21 14:18:31
.. tags: патенты, legal, ptp, ntp
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

`PTP <https://en.wikipedia.org/wiki/Precision_Time_Protocol>`__, это протокол
для точной синхронизации времени в компьютерной сети, находящийся по точности
между NTP и GPS. Он популярен среди производителей дорогостоящего сетевого
оборудования, финансовых спекулянтов и прочих игроков highload-индустрии. К
сожалению, `длинный список софтверных патентов
<http://standards.ieee.org/about/sasb/patcom/pat1390.html>`__ препятствовал
ранее включению библиотек или приложений для этого протокола в Fedora (`было
<https://bugzilla.redhat.com/556611>`__ `несколько
<https://bugzilla.redhat.com/658796>`__ `попыток
<https://bugzilla.redhat.com/807810>`__). Наконец, в апреле 2012 года Fedora
Legal Team `объявила, что патенты либо истекли, либо не являются опасными
<https://bugzilla.redhat.com/807810#c4>`__, и снова началась работа по
включению PTP приложений в Fedora - в процессе `один из форков оригинального
PTPd <https://bugzilla.redhat.com/807810>`__ и `linuxptp
<https://bugzilla.redhat.com/859193>`__.
