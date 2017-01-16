.. title: PackageKit 1.0.0
.. slug: packagekit-100
.. date: 2014-09-12 16:54:23
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Richard Hughes `анонсировал PackageKit
1.0.0 <http://thread.gmane.org/gmane.comp.freedesktop.packagekit/6595>`__.

В этом релизе отказались от плагинов - от них лишь проблемы. Вся
функциональность, которая хоть кем-то затребована, была перенесена в
дерево проекта. Были удалены бэкенды для conary, opkg, smart, yum - их
никто не поддерживал уже очень давно. Richard недавно `собрал список
проблем в имеющихся
бэкендах <http://thread.gmane.org/gmane.comp.freedesktop.packagekit/6584>`__,
и его услышали - бэкенды для alpm, aptcc, hif, zypp были обновлены.

