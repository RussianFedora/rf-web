.. title: CentOS для ARM
.. slug: centos-для-arm
.. date: 2014-03-27 12:54:57
.. tags: centos, arm, 
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

`Неопределенность с поддержкой ARM в
CentOS </content/centos-начинает-набирать-скорость>`__ была недолгой.
Karanbir Singh объявил, что `планируется пересборка RHEL и для
ARM <http://www.karan.org/blog/2014/03/26/the-arm-plan-for-centos/>`__.

Для EL6 поддержки уже не будет, хотя желающие всегда могут
воспользоваться другой пересборкой EL6 - Red Sleeve Linux, `о которой мы
уже
рассказывали </content/Еще-одна-пересборка-rhel-для-arm-микропроцессоров>`__.

Проблема в том, что EL6 довольно старовата для ARM, и многих интересных
фич из ядра, gcc, glibc там уже не будет. А вот работа над EL7 еще вовсю
идет, и у участников CentOS есть возможность на нее влиять.

Будет задействовано оборудование `Veridis, ARM as a Service
Cloud <http://www.boston.co.uk/solutions/viridis/viridis-cloud.aspx>`__,
работающее под управлением Fedora 19.
