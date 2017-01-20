.. title: OpenCL в Fedora
.. slug: opencl-в-fedora
.. date: 2013-10-22 10:36:55
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Положение с OpenCL по сравнению с `ситуацией годичной
давности </content/Текущий-статус-и-планы-на-opencl-в-fedora>`__ начало
улучшаться. `В Mesa включили поддержку
ICD <http://cgit.freedesktop.org/mesa/mesa/commit/?id=6230f7>`__, что
позволит устанавливать и использовать разные реализации OpenCL от разных
разработчиков, в т.ч. и проприетарные (мы уже говорили, что в OpenGL
`тоже запланировали переход на новый ABI с аналогичной
архитектурой </content/Новости-xorg-drm2-dri3-dri-next-egl-отказ-от-glx>`__,
и практически `завершили
запланированное </content/Коротко-новости-графической-подсистемы>`__). К
сожалению, пока Mesa в Fedora собрана без этой функциональности, но
`мэйнтейнеров Mesa уже попросили пересобрать ее с поддержкой
ICD <https://bugzilla.redhat.com/887628#c8>`__.

В остальном, все кусочки уже в наличии, в т.ч.
`pocl <https://admin.fedoraproject.org/pkgdb/acls/name/pocl>`__,
полноценная реализация OpenCL на CPU (без GPU), которую можно
рассматривать как "эталонную" (в смысле "референсную", а не
"идеальную"), и работа по сбору из кусочков полноценной платформы для
разработки с OpenCL и его использованием уже началась. Работу взялся
выполнить инженер Red Hat и разработчик oVirt, `Fabian
Deutsch <https://www.openhub.net/accounts/fabiand>`__. Он планирует
оформить это, как `фичу Fedora
21 <https://fedoraproject.org/wiki/User:Fabiand/Changes/OpenCL>`__.

