.. title: AAC кодек включают в Fedora
.. slug: aac-kodek-vkliuchaiut-v-fedora
.. date: 2017-10-12 21:04:32 UTC+03:00
.. tags: aac, codec, патенты, legal, gstreamer 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Официально `объявлено
<https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/F64JBJI2IZFT2A5QDXGHNMPALCQIVJAX/>`_
о начале процедуры включения библиотеки, реализующей кодек для `формата AAC
<https://ru.wikipedia.org/wiki/Advanced_Audio_Coding>`_. В этот раз не
сообщается никаких подробностей о состоянии патентов, и гадать мы пока не будем. Напомним, что оперировать
запатентованными алгоритмами можно, например, если у владельца патентов
конкретно к вам нет претензий, если у вас есть договор о кросс-лицензировании,
или если вы покрываетесь патентной защитой от одного из известных патентных
пулов.

Включена будет модифицированная версия известной библиотеки - `Fraunhofer FDK
AAC в версии для Android <https://www.iis.fraunhofer.de/en/ff/amm/impl.html>`_,
которая, что интересно, в немодифицированном виде участниками Fedora
рассматривается, как `несвободное, хотя и открытое ПО
<https://github.com/rpmfusion/fdk-aac>`_. Учитывая, что и про конкретные
поддерживаемые возможности модифицированной библиотеки явно ничего сказано не
было, видимо изменить пришлось много. Также сразу будет включен плагин для GStreamer.
