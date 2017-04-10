.. title: Новости GCC
.. slug: novosti-gcc
.. date: 2017-04-10 16:47:54 UTC+03:00
.. tags: gcc, oops, начинающим
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Каждая пересборка всего дерева Fedora с новым GCC выявляет разные проблемы. В
этот раз мы нашли, что `проверка -Werror=format-security
</content/Еще-немного-будущих-фич-fedora-21>`_ в определенных условиях `не
выполняется
<https://lists.fedoraproject.org/archives/list/devel-announce@lists.fedoraproject.org/thread/ZB4AC75UT3LM7POTITXOI25TCUXAUA75/>`_.
Проблема существует с 4й версии GCC. Бывает, что.

Наш коллега, инженер Red Hat, `David Malcolm
<http://fedoraproject.org/wiki/User:Dmalcolm>`_ завел `страничку для новичков
<https://dmalcolm.fedorapeople.org/gcc/newbies-guide/index.html>`_, которые бы
хотели заняться разработкой GCC. Если хотите написать для GCC фронтенд для
нового языка программирования, то начните с этого адреса.

В `блоге Red Hat Developers <https://developers.redhat.com/blog/>`_ появилась
очередная статья про GCC. В этот раз рассказывается про `проверку
-Wimplicit-fallthrough
<https://developers.redhat.com/blog/2017/03/10/wimplicit-fallthrough-in-gcc-7/>`_,
которая проверяет выражения switch..case на блоки без break или return.  Очень
своевременно, т.к. `на нас уже начали сваливаться багрепорты из-за этой
проверки <https://code.wireshark.org/review/#/c/20411/>`_.

В том же `блоге <https://developers.redhat.com/blog/>`_ появилась еще одна
интересная статья, поднимающая интересный вопрос, о котором стоит рассказать
поподробнее.

Нас часто критиковали анонимные коллеги-аналитики за то, что при обновлениях
`предлагается <https://www.linux.org.ru/news/redhat/7902931>`_ `перезагружаться
<https://www.linux.org.ru/forum/talks/12089895>`_, мол неюниксвэйно, и надо
гордиться аптаймом. Другие, кто поумнее, интересовались критериями того, `когда
надо перезагружаться после обновления
<https://www.linux.org.ru/forum/admin/13043788>`_. К сожалению, проблема в том,
что есть ситуации, когда без анализа исходного текста или хотя бы работы
приложения, непонятно как поведет себя приложение, если из под него выдернуть
используемую версию библиотеки и заменить новой.

И вот, наш коллега, инженер Red Hat, `Carlos O'Donell
<https://profiles.google.com/patofiero/about>`__, попробовал рассказать о
ситуации, когда обновляется библиотека, и два или больше приложений используют
shared memory, в которой находятся объекты т.н. `opaque data type
<https://en.wikipedia.org/wiki/Opaque_data_type>`_. Это запросто может вызвать
проблемы, и `очень непонятные для начинающих сисадминов
<https://bugzilla.redhat.com/show_bug.cgi?id=1394862>`_. Обновления без
перезапуска системы в таком случае просто приведут к неработоспособности
ряда ее сервисов.
