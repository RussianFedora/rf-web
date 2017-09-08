.. title: OpenStack Pike (16я версия) и другие новости
.. slug: openstack-pike-16ia-versiia
.. date: 2017-09-07 15:13:19 UTC+03:00
.. tags: openstack, clouds, etcd, docker, kubernetes, google, pivotal, vmware
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Довольно незаметно для публики `вышла новая версия OpenStack под кодовым
названием Pike <https://www.openstack.org/software/pike/>`_. Это багфикс релиз
к недавно вышедшему дистрибутиву `OpenStack Ocata
<https://www.openstack.org/software/ocata/>`_.

В 16й версии OpenStack можно выделить следующие изменения:

* Давно ожидаемая поддержка Python 3.5.
* В Cinder, сервисе блочных хранилищ, появилась функция "откатиться к
  снапшоту".
* В Cinder добавили возможность расширять объем блочных устройств без
  отключения от виртуальных машин.
* В Ironic, сервисе по развертыванию узлов на bare-metal машинах, появилась
  функция rolling-обновлений.
* Swift, объектное хранилище, получила поддержку кодов избыточности (erasure
  coding) для лучшего восстановления работоспособности и данных при сбоях.
* В Nova, основном компоненте OpenStack, управляющем работой виртуальных машин,
  внутренняя архитектура Cells обновлена до второй версии, в которой должны
  быть исправлены ограничения масштабируемости (протестировано в CERN, NeCTAR,
  eBay, PayPal и Rackspace).
* Новый компонент - etcd. Его предлагают использовать для достижения консенсуса
  в сети.
* Cinder теперь может работать отдельно от целого OpenStack, выступая как
  внешнее устройство хранения для традиционных систем на физических машинах,
  виртуалках, контейнеров, управляемых с помощью Docker или Kubernetes.
* Улучшенная интеграция между Ironic и Neutron, сервисом сетевых служб. Теперь
  компоненты OpenStack, развернутые с помощью Ironic на физических машинах,
  могут быть подключены к сетям, управляемым Neutron.

В целом видно движение вперед.

К сожалению, до нас все чаще доходят `слухи о разочаровании вендоров в
OpenStack <https://www.infoworld.com/article/3193605/private-cloud/serverless-computing-will-drive-out-openstack-private-clouds.html>`_. Мол, слишком сложно, и лучше сразу делать что-то свое на базе,
например, Kubernetes. Немного другая ниша, но тем не менее - `Google, Pivotal,
и VMware собрались и вложили аж почти 3 гигабакса
<http://www.businessinsider.com/google-vmware-pivotal-team-up-for-kubernetes-service-2017-8>`_,
чтобы реализовать облачное решение на базе именно Kubernetes. Альянс нацелен на
противодействие Microsoft, Docker Inc. и Red Hat (Red Hat OpenShift). Планы
амбициозные, но немного настораживает то, что Kubernetes требует 3 миллиардов
долларов для доработки, поэтому еще непонятно, как и когда все заработает.

С другой стороны, есть и `история успеха Kubernetes в GitHub
<https://githubengineering.com/kubernetes-at-github/>`_, где его используют для
развертывания приложений на базе `их облака из физических машин
<https://githubengineering.com/githubs-metal-cloud/>`_. Получается, что он уже
готов для десктопа.

Появились и те, кто сомневается в перспективах самого Kubernetes - например,
`Matt Asay из Adobe
<https://www.infoworld.com/article/3204597/open-source-tools/kubernetes-days-may-be-numbered-as-open-source-changes.html>`_
и `Boris Renski из  Mirantis
<https://www.mirantis.com/blog/is-kubernetes-repeating-openstacks-mistakes/>`_. Посмотрим.
