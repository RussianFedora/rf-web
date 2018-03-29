.. title: Скандал с Python-коммьюнити
.. slug: skandal-s-python-kommiuniti
.. date: 2018-03-29 15:50:57 UTC+03:00
.. tags: python, community, redhat
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Наши коллеги очень активно используют Python, и не только разрабатывают
продукты с его использованием, но и `принимают
<https://lwn.net/Articles/723949/>`_ `активное
<https://lwn.net/Articles/725114/>`_ `участие
<http://pyvideo.org/pycon-us-2017/optimizations-which-made-python-36-faster-than-python-35.html>`_
`в его разработке <https://lwn.net/Articles/727973/>`_. Именно поэтому как
громом среди ясного неба грянуло `Twitter-сообщение
<https://twitter.com/ncoghlan_dev/status/975252367632359424>`_ нашего бывшего
коллеги, Nick Coghlan - активного разработчика Python и, как некоторые
полагают, главного кандидата в BDFL после возможного ухода с этого поста Guido
van Rossum.

Дело обстояло так. В Python `нашли проблему
<https://bugs.python.org/issue33021>`_ - вызов fstat() иногда блокирует `GIL
<https://ru.wikipedia.org/wiki/Global_Interpreter_Lock>`_. Был предложен патч,
его приняли в master (Python3) и закрыли тикет. Но пользователь, сообщивщий о
проблеме, потребовал переоткрыть тикет и сбэкпортировать патч в
production-версию, то есть в Python2, который будет использоваться еще сколько
лет в RHEL. Nick разозлился, начал обзываться "корпоративными паразитами" и
отправил пользователя жаловаться в Red Hat.

Мы не можем полностью согласиться с его жестокими словами. Как минимум, Red Hat
и дружественные компании являются спонсорами PyCon довольно давно:

* `2018 <https://us.pycon.org/2018/sponsors/>`_ - Ansible (Gold level)
* `2017 <https://us.pycon.org/2017/sponsors/>`_ - Ansible (Gold level), OpenShift (Gold level)
* `2016 <https://us.pycon.org/2016/sponsors/>`_ - Ansible (Platinum level), OpenShift (Silver level)
* `2015 <https://us.pycon.org/2015/sponsors/>`_ - Red Hat (Gold level)
* `2014 <https://us.pycon.org/2014/sponsors/>`_ - Red Hat (Gold level), OpenShift (Gold level)
* `2013 <https://us.pycon.org/2013/sponsors/>`_ - Red Hat (Platinum level), OpenShift (Platinum level)
* `2012 <https://us.pycon.org/2012/sponsors/>`_ - OpenShift (Gold level)

Будем следить за дальнейшим развитием событий.
