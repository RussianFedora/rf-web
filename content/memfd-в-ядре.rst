.. title: memfd в ядре
.. slug: memfd-в-ядре
.. date: 2014-03-26 10:17:52
.. tags: memfd, kernel, kdbus
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**

С момента `появления kdbus </content/Перенос-d-bus-в-ядро-linux>`__ в рабочем
состоянии в ядре, разработчиков других подсистем ядра интересовала одна
интересная реализованная в нем функциональность, memfd. Если совсем
по-простому, то это участок памяти с присоединенным к нему дескриптором,
который можно передавать между процессами, что позволило реализовать zero-copy
передачу сообщений в kdbus. Разработчики других подсистем ядра (особенно
графической, где копирование туда-сюда может сильно замедлить работу) постоянно
либо писали что-то свое, либо обдумывали что-то подобное, и как только увидели
рабочую реализацию, то сразу начали `интересоваться
<https://lwn.net/Articles/580249/>`__, нет ли планов по выделению этой
функциональности в отдельную подсистему.

Планы, конечно, были, и вот, наконец-то, участник Arch Linux, `David Herrmann
<http://dvdhrm.wordpress.com/about-me/>`__, `предложил первый вариант
независимой от kdbus подсистемы memfd для включения в ядро
<https://thread.gmane.org/gmane.comp.video.dri.devel/102241>`__. Его работа уже
получила положительные отклики от `Greg Kroah-Hartman
<https://plus.google.com/111049168280159033135/posts/KGHK5JNZQuU>`__ и `Lennart
Poettering
<https://plus.google.com/+LennartPoetteringTheOneAndOnly/posts/TEy9286sTNu>`__.

|image0|

**Участники коммьюнити радуются, услышав о включении memfd в ядро.**

.. |image0| image:: http://cdn.gifbay.com/2013/08/emma_watson_approves-79273.gif
   :target: http://www.gifbay.com/gif/emma_watson_approves-79273/
