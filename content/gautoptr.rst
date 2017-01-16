.. title: g_autoptr ()
.. slug: gautoptr
.. date: 2015-05-05 23:27:52
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


| Вот уже некоторое время GCC поддерживает хороший способ для
  автоматической очистки переменных, когда они перестают использоваться
  -- *\_\_attribute\_\_((cleanup)).*
| Некоторое время назад, разработчик GLib, `Ryan
  Lortie <https://blogs.gnome.org/desrt/>`__,\ `добавил специальные
  макросы <https://blogs.gnome.org/desrt/2015/01/30/g_autoptr/>`__,
  чтобы упростить работу программистам по очистке памяти. Они работают
  только с GCC и Clang, так что если вы хотите собирать программу
  используя MSVC ([STRIKEOUT:кто-то ещё использует это?]) - вы не должны
  их использовать.

| Новое API лучше всего продемонстрированно на следующем примере:

::

    {
      g_autoptr(GObject) object;
      g_autoptr(gchar) tmp;
      g_auto(GQueue) queue;

      g_queue_init (&queue);
      object = g_object_new (...);
      tmp = g_strdup_printf (...);

      // no free required
    }

| Чтобы добавить поддержку собственных типов - нужно использовать
  *G\_DEFINE\_AUTOPTR\_CLEANUP\_FUNC* и подобные макросы. Это будет
  происходить автоматически, если вы используете недавно-добавленные в
  API *G\_DECLARE\_DERIVABLE\_TYPE* или *G\_DECLARE\_FINAL\_TYPE*
  макросы.

| Для тех, кто пишет на C, GLib может показаться очень удобным
  дополнением, там есть удобная реализация потоков, списков, классов
  (да-да, вы не ослышались), асинхронность, таймеры, парсеры конфигов и
  ещё много-много всего. Вы только посмотрите на
  `документацию <https://developer.gnome.org/glib/stable/>`__!
| Давайте рассмотрим более детальный пример:

::

    // gcc `pkg-config --libs --cflags glib-2.0` -g g_autoptr.c
    #include 

    G_DEFINE_AUTOPTR_CLEANUP_FUNC (gchar, g_free);

    void
    print_elem (gpointer data,
                gpointer user_data)
    {
      g_print ("GList: %s\n", (gchar *) data);
    }

    gint
    main (gint   argc,
          gchar *argv[])
    {
      g_autoptr(gchar) tmp = g_strdup ("Hello, I'm gchar!");
      g_autoptr(GList) lst = NULL;
      lst = g_list_append (lst, tmp);

      g_print ("gchar: %s\n", tmp);
      g_list_foreach (lst, (GFunc) print_elem, NULL);

      return 0;
    }

Давайте скомпилируем и запустим наш пример под valgrind и посмотрим на
утечки в памяти..

::

    $ valgrind --tool=memcheck --leak-check=full ./g_autoptr
    ==9620== HEAP SUMMARY:
    ==9620==     in use at exit: 2,094 bytes in 6 blocks
    ==9620==   total heap usage: 22 allocs, 16 frees, 68,943 bytes allocated
    ==9620== 
    ==9620== LEAK SUMMARY:
    ==9620==    definitely lost: 0 bytes in 0 blocks
    ==9620==    indirectly lost: 0 bytes in 0 blocks
    ==9620==      possibly lost: 0 bytes in 0 blocks
    ==9620==    still reachable: 2,094 bytes in 6 blocks
    ==9620==         suppressed: 0 bytes in 0 blocks

А теперь уберём g\_autoptr и ещё раз посмотрим.


::

    $ valgrind --tool=memcheck --leak-check=full ./no_g_autoptr
    ==9705== HEAP SUMMARY:
    ==9705==     in use at exit: 2,136 bytes in 8 blocks
    ==9705==   total heap usage: 22 allocs, 14 frees, 68,943 bytes allocated
    ==9705== 
    ==9705== 42 (24 direct, 18 indirect) bytes in 1 blocks are definitely lost in loss record 7 of 8
    ==9705==    at 0x4C2AC10: malloc (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==9705==    by 0x4E82769: g_malloc (in /usr/lib64/libglib-2.0.so.0.4501.0)
    ==9705==    by 0x4E99DC2: g_slice_alloc (in /usr/lib64/libglib-2.0.so.0.4501.0)
    ==9705==    by 0x4E78EE3: g_list_append (in /usr/lib64/libglib-2.0.so.0.4501.0)
    ==9705==    by 0x400848: main (no_g_autoptr.c:16)
    ==9705== 
    ==9705== LEAK SUMMARY:
    ==9705==    definitely lost: 24 bytes in 1 blocks
    ==9705==    indirectly lost: 18 bytes in 1 blocks
    ==9705==      possibly lost: 0 bytes in 0 blocks
    ==9705==    still reachable: 2,094 bytes in 6 blocks
    ==9705==         suppressed: 0 bytes in 0 blocks

Сейчас, некоторые наши коллеги, используют такие конструкции:

::

    #define GS_DEFINE_CLEANUP_FUNCTION0(Type, name, func) \
      static inline void name (void *v) \
      { \
        if (*(Type*)v) \
          func (*(Type*)v); \
      }
    #define _cleanup_error_free_ __attribute__ ((cleanup(gs_local_free_error)))
    GS_DEFINE_CLEANUP_FUNCTION0(GError*, gs_local_free_error, g_error_free)

    _cleanup_error_free_ GError *error = NULL;

Некрасиво, правда? К тому же ещё и код дублируется из проекта в проект.

