.. title: BLKDISCARD, BLKZEROOUT, BLKDISCARDZEROES, BLKSECDISCARD
.. slug: blkdiscard-blkzeroout-blkdiscardzeroes-blksecdiscard
.. date: 2014-03-13 00:31:36
.. tags: kernel, util-linux
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Rich WM Jones обращает наше внимание на ряд новых ioctl - BLKDISCARD,
BLKZEROOUT, BLKDISCARDZEROES, BLKSECDISCARD. Ну, новые они относительно - в
ядре с 2010 года, а поддержка в userspace-программах начала появляться недавно
(например, `в util-linux добавили примерно год назад
<https://github.com/karelzak/util-linux/commit/d964b66>`__), т.е., например, в
Debian они будут доступны года с 2017.

Rich заметил, что данные ioctl никак не документированы, хотя наши коллеги уже
упоминают их в своих докладах (например, `Paolo Bonzini на прошедшем недавно
DevConf <https://www.youtube.com/watch?v=dlbz9CA3kHE>`__) и решил исправить
положение, `перечислив их функциональность
<http://rwmj.wordpress.com/2014/03/11/blkdiscard-blkzeroout-blkdiscardzeroes-blksecdiscard/>`__
и ограничения (если есть):

-  BLKDISCARD - требует от блочного устройства удалить все блоки,
   попадающие в указанный диапазон. Есть ограничение - блочное
   устройство может игнорировать этот ioctl. Что будет прочитано после
   выполнения этой функции никак не стандартизируется, и может заполнить
   указанный диапазон нулями, случайными числами, или просто
   проигнорировать запрос целиком, оставив все, как есть.

-  BLKZEROOUT - то же, что и BLKDISCARD, но требует заполнить указанный
   диапазон нулями. Ядро вынуждено реализовать этот функционал само, и
   устройство тут никак не помогает.

-  BLKDISCARDZEROES - запрашивает у устройства, будет ли оно обнулять
   секторы, удаленные при помощи вызова BLKDISCARD. Если ответ
   положительный, то BLKZEROOUT не требуется.

-  BLKSECDISCARD - то же, что и BLKDISCARD, но без какой-либо
   возможности восстановления. Обязано вернуть EOPNOTSUPP, если
   устройство не в состоянии этого сделать.

В RHEL 6.5 и выше, утилита blkdiscard уже доступна в составе пакета
util-linux-ng.
