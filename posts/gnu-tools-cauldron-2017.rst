.. title: GNU Tools Cauldron 2017
.. slug: gnu-tools-cauldron-2017
.. date: 2017-09-08 13:46:31 UTC+03:00
.. tags: gcc, llvm, gdb
.. category: мероприятия
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Уже сегодня, в Праге, в Карловом университете, начнется очередная конференция `GNU Tools Cauldron <https://gcc.gnu.org/wiki/cauldron2017>`_, которая будет идти до 10 сентября. Наши коллеги, конечно, там будут, так что заезжайте, если у вас есть возможность приехать в ЕС (открытый шенген или безвиз).

Несмотря на новости от конкурентов, особенно `доросшего до версии 5 LLVM <https://www.opennet.ru/opennews/art.shtml?num=47154>`_, GCC и остальные сопутствующие утилиты не выглядят отстающими. Из последних новостей, навскидку:

.. role:: strike

* Наш коллега, инженер Red Hat и участник Fedora, `David Malcolm
  <https://fedoraproject.org/wiki/User:Dmalcolm>`_, недавно `предложил включить
  в GCC поддержку Microsoft Language Server Protocol
  <https://gcc.gnu.org/ml/gcc-patches/2017-07/msg01448.html>`_ (протокол,
  основанный на JSON, разработка одноименной компании для создания более
  интеллектуальных IDE).
* Он же предложил другой интересный функционал - :strike:`включить поддержку
  Clang` добавить `поддержку внешних анализаторов текста
  <https://gcc.gnu.org/ml/gcc-patches/2017-08/msg00416.html>`_. Некоторые
  участники коммьюнити уже засомневались, будет ли это работать с лицензионной
  точки зрения, но идея взять лучшее из двух миров - соблазнительная.
* Как вы знаете, `только что приняли очередной стандарт С++, под названием
  C++17 <https://herbsutter.com/2017/09/06/c17-is-formally-approved/>`_. Само
  собой, в обсуждении стандартов С++ `инженеры Red Hat постоянно принимают
  самое непосредственное участие
  <https://developers.redhat.com/blog/2017/08/29/red-hat-at-the-iso-c-standards-meeting-july-2017-parallelism-and-concurrency/>`_.
  Так вот, `в GCC уже начали работу по реализации стандарта C++20
  <https://gcc.gnu.org/ml/gcc-patches/2017-07/msg01234.html>`_. Отдельно,
  `обратите внимание на поддержку C++17 и предыдущих стандартов в компиляторах
  <http://en.cppreference.com/w/cpp/compiler_support>`_. Кто теперь кого
  догоняет? Вот то то же.

Ну и напоследок - прекрасный короткий видеоурок по GDB.

.. youtube:: PorfLSr3DDI
   :align: center
