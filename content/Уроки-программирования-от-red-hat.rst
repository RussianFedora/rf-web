.. title: Уроки программирования от Red Hat
.. slug: Уроки-программирования-от-red-hat
.. date: 2014-03-21 14:14:08
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Security-отдел Red Hat (не "безопасники" в отечественном смысле слова)
  опубликовал пост в своем блоке, `посвященный проблеме с семейством
  функций strcpy, strcat,
  sprintf <https://securityblog.redhat.com/2014/03/12/the-trouble-with-snprintf/>`__.

  Увы, но несмотря на общее распространенное мнение, что эти функции
  использовать нежелательно, их все еще используют в разных проектах, в
  т.ч. и очень известных. Но проблема в том, что за просто так, просто
  перейдя на использование strncpy, strncat, strnprintf, программа не
  станет безопасной, волшебным образом лишившись buffer overflow. В
  заметке как раз и разбирают еще один типичный паттерн
  программирования, который теоретически (и порой, практически) приводит
  к buffer overflow. Обратите внимание, если вы разрабатываете на C, и
  если вы пока еще не видите проблем в данном фрагменте кода:

::

        /* buff is a pointer to a buffer of blen characters. */
        /* Note well: This example is now incorrect. */
        char *cp = buff;
        if ((n = snprintf(cp, blen, "AF=%d ", sau->soa.sa_family)) < 0) {
            Warn1("sockaddr_info(): buffer too short ("F_Zu")", blen);
            *buff = '';
            return buff;
        }
        cp += n,  blen -= n;

| 
| Заметили? Если нет, то
  `прочитайте <https://securityblog.redhat.com/2014/03/12/the-trouble-with-snprintf/>`__.

