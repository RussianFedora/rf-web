.. title: Разработчики CoreOS перешли на Kubernetes
.. slug: razrabotchiki-coreos-pereshli-na-kubernetes
.. date: 2017-02-11 12:30:23 UTC+03:00
.. tags: coreos, fleet, kubernetes, containers, eol
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Разработчики CoreOS `официально объявили
<https://coreos.com/blog/migrating-from-fleet-to-kubernetes.html>`_ о том, что
утилита fleet, о которой мы вам `периодически рассказывали
</categories/fleet/>`_, больше не поддерживается. Ее пользователям
рекомендовано перейти на Kubernetes.

Архитектура fleet оказалась довольно ограниченной. Например, ее `не рекомендуют
использовать в кластерах на сто узлов и больше
<https://github.com/coreos/fleet#current-status>`_. В то же время, в Kubernetes
таких проблем не наблюдается.
