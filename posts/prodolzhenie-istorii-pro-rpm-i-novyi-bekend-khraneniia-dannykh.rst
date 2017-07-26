.. title: Продолжение истории про RPM и новый бэкенд хранения данных
.. slug: prodolzhenie-istorii-pro-rpm-i-novyi-bekend-khraneniia-dannykh
.. date: 2017-07-26 15:41:29 UTC+03:00
.. tags: rpm
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Продолжается история `с новым бэкендом к RPM
</posts/rpm-vybiraet-bekend-dlia-khraneniia-dannykh/>`_. `Обновление RPM до
версии 4.14 <https://fedoraproject.org/wiki/Changes/RPM-4.14>`_ `утвердили
<https://pagure.io/fesco/issue/1747>`_ фичей Fedora 27. Rich W.M. Jones
`потребовал
<https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/TQQXD7X55WSZ6NYIAKDJCGIPRVI6PXDN/>`_,
чтобы бэкенд NDB включен не был.

На это `поступили разъяснения
<https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/K6WQFRICTKJ643A2GOKX2P3EAPGIOUJM/>`_.
Этот бэкенд по умолчанию использоваться не будет, но пользователь может его
попробовать, если установит переменную _db_backend в значение ndb и запустить rpmbuild --rebuild.
