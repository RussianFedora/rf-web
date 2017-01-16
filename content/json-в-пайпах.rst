.. title: JSON в пайпах!
.. slug: json-в-пайпах
.. date: 2015-07-24 15:15:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


А `та идея-то
жива-живехонька </content/Предложены-радикальные-изменения-в-работу-unix-pipes>`__!
Наш коллега, `Karel Zak <https://www.openhub.net/accounts/kzak>`__,
недавно потихоньку `добавил вывод в формате
JSON <http://karelzak.blogspot.com/2015/06/json-output-for-basic-tools.html>`__
в библиотеку libsmartcols, `о которой вы уже
слышали </content/Унификация-вывода-консольных-команд>`__, и началось.

После добавления в lsblk, findmnt, lslocks, и losetup, он быстро
`добавил подержку JSON в
sfdisk/libfdisk <http://karelzak.blogspot.com/2015/06/sfdisk-json.html>`__,
и планирует добавлять поддержку в другие старые утилиты. А на днях он
написал новую утилиту, `lsipc, в которой уже изначально была поддержка
JSON <http://karelzak.blogspot.com/2015/07/lsipc-new-command-to-list-ipc-facilities.html>`__.

Эта новая утилита, lsipc, идет на замену устаревшей и малофункциональной
`ipcs <http://linux.die.net/man/8/ipcs>`__, и предназначена для вывода
информации о `SysV IPC <http://www.tldp.org/LDP/lpg/node21.html>`__.

Конечно, с появлением systemd и kdbus, эта система межпроцессного
взаимодействия однозначно устарела, но ее еще используют некоторые
малоизвестные приложения - от базы данных Oracle, до браузера Firefox,
поэтому приходится ее использовать.

