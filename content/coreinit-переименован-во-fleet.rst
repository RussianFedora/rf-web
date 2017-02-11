.. title: Coreinit переименован во fleet
.. slug: coreinit-переименован-во-fleet
.. date: 2014-02-19 13:19:49
.. tags: coreos, fleet, containers
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Coreinit, проект по расширению кластерных возможностей systemd, `о
котором мы уже вскользь
упомянули </content/Новости-systemd-за-прошедший-месяц-полтора>`__,
разрабатываемый участниками проекта CoreOS (и о нем мы уже `не
раз </content/coreos-новый-дистрибутив-на-базе-chromeos>`__, и `не
два </content/Статья-о-coreos>`__ упоминали) был переименован во
`fleet <https://github.com/coreos/fleet>`__.

Fleet / coreinit, это надстройка над systemd, использующая etcd, которая
превращает его в init-систему для целого кластера. Eго переименование во
fleet было приурочено к выходу `версии
0.1.2 <https://github.com/coreos/fleet/releases/tag/v0.1.2>`__. Также, к
выходу новой версии, которой уже можно пользоваться, разработчики CoreOS
написали `обзорную статью по
fleet <https://coreos.com/blog/cluster-level-container-orchestration/>`__
и сделали видеопрезентацию:
Fleet в целом принят очень хорошо, и уже был отмечен такими видными
разработчиками systemd, как `Greg
Kroah-Hartman <https://plus.google.com/111049168280159033135/posts/f7A7tLG4sfT>`__
и `Lennart
Poettering <https://plus.google.com/+LennartPoetteringTheOneAndOnly/posts/38G8uDHBJ7G>`__.

