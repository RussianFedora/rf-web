.. title: Новый раунд добавления strlcpy в Glibc
.. slug: Новый-раунд-добавления-strlcpy-в-glibc
.. date: 2014-09-25 10:29:29
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| И вновь о безопасности. Наши коллеги начали новый раунд добавления
  функции strlcpy, используемой в BSD, в Glibc.

| Есть семейство библиотечных функций strcpy. Эти функции не глядя
  копируют одну строку в другую. Есть одна беда - если приемник короче
  источника, то будет переполнение буфера. Поэтому использовать их не
  рекомендуется. Вместо strcpy есть семейство strncpy, которые не
  копируют больше, чем можно. Но с этим семейством есть другая беда -
  функция будет копировать, пока есть место, и если что-то не влазит, то
  оно будет отброшено (включая нулевой байт в конце). В случае, когда
  strcpy приводит к переполнению буфера, в strncpy мы получаем байтовые
  массивы, что лучше, но тоже плохо.

| В BSD придумали еще одно усовершенcтвование - strlcpy. При
  копировании, если места больше нет, она автоматически записывает
  нулевой байт в конец. Т.е. опять получается ошибка - мы теперь получим
  обрезанную строку. С т.з. пользователя все три случая равносильно
  плохие, и вполне возможно вызовут потерю пользовательских данных,
  такова плата за приверженность традициям в софте ("работает - не
  трожь", с готовностью кричат любители заняться в одиночку юниксвэем).

| Таким образом у программистов BSD есть целых три способа написать
  неправильный код для работы со строками, а до сих пор в Glibc было
  лишь два. Ulrich Drepper `был предсказуемо против включения третьего
  неправильного
  варианта <http://www.sourceware.org/ml/libc-alpha/2000-08/msg00053.html>`__,
  т.к. какой смысл предлагать программистам писать кривой код? Но
  проблема была в коде, написанном программистами BSD - `мы насчитали 60
  программ <https://thread.gmane.org/gmane.comp.lib.glibc.alpha/45138/focus=45154>`__,
  написанных с использованием этой функции. При ее отсутствии, программы
  переключаются на некий кое-как набранный самопал, оптимизированный
  плохо, не использующий `последние разработки в
  GCC </content/Уроки-программирования-от-red-hat-fortifysource>`__, что
  гораздо хуже.

| Нашими коллегами было решено посмотреть правде в глаза. Функция
  strlcpy используется, и ее отсутствие в Glibc, это большая проблема,
  чем ее возможное наличие. Одна из недавних ошибок в SAMBA `была
  вызвана как раз самопальной реализацией
  strlcpy <https://thread.gmane.org/gmane.comp.lib.glibc.alpha/44482/focus=44527>`__.

  Принимая все это во внимание, `наши коллеги начали ее включение в
  Glibc <https://thread.gmane.org/gmane.comp.lib.glibc.alpha/45138>`__.

| Мы, кстати, рекомендуем обратить внимание на функционал glib, и
  использовать его при возможности:

::

    g_strconcat() -- concatenates a NULL-terminated list of strings
    g_strjoin() -- similar, but allows to add an optional separator
    g_strjoinv() -- concatenates an array of strings, with an optional separator
    g_strdupv() -- duplicate an array of strings
    g_strsplit() -- splits a string into an array
    g_strescape()/g_strcompress() -- escape/unescape a string
    g_strdelimit() -- change delimiter (let's say you've got a comma-delimited string and want it to be space delimited)
    g_strstrip() -- strip away leading + trailing whitespace
    g_strchomp() -- strip away leading whitespace
    g_strchug() -- strip away trailing whitespace
    g_strnfill() -- creates a string of the specified length filled with a specified character

    and of course my favourites:

    g_strdup_printf(), g_strdup_vprintf(), g_vasprintf() -- sprintf()/vsprintf() variants that allocated the necessary memory.

