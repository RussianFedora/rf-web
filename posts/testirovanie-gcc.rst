.. title: Тестирование GCC
.. slug: testirovanie-gcc
.. date: 2017-03-03 17:54:49 UTC+03:00
.. tags: testing, gcc, systemtap
.. category: начинающим
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Не так давно `вышел SystemTap 3.1
<https://www.mail-archive.com/linux-kernel@vger.kernel.org/msg1336080.html>`_,
и в честь этого события хотелось бы поговорить о тестировании.

Наш коллега, инженер Red Hat, `David Malcolm
<https://fedoraproject.org/wiki/User:Dmalcolm>`_, опубликовал заметку о том,
`как тестируется GCC
<https://developers.redhat.com/blog/2017/02/13/testing-testing-gcc/>`_, и какие
можно ожидать улучшения.  Напомним, именно он `работал над включением
unit-тестов в кодовую базу GCC </content/gcc-все-таки-получит-unit-тесты/>`_.

Тестирование собранного ПО, это хорошо, но еще лучше, чтобы ошибки выявлялись
на этапе компиляции. Еще один наш коллега, Martin Sebor, опубликовал заметку о
том, `какие можно использовать флаги GCC
<https://developers.redhat.com/blog/2017/02/22/memory-error-detection-using-gcc/>`_
для поиска подозрительных мест в коде на ранних этапах сборки и привел примеры
ошибок в коде, выявляемых при сборке с этими флагами.

.. image:: http://s.pikabu.ru/post_img/2013/04/07/7/1365327582_998102211.gif
   :align: center

.. class:: align-center

**Разработчик не обращает внимания на предупреждения компилятора**
