.. title: Улучшения в видеодрайверах для X.org от участников Fedora
.. slug: Улучшения-в-видеодрайверах-для-xorg-от-участников-fedora
.. date: 2012-09-12 10:25:38
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Пока Wayland еще не вышел, продолжается работа по модернизации и
улучшению X.org. Инженер Red Hat, `Ben
Skeggs <https://www.openhub.net/accounts/darktama>`__, `написал открытую
firmware для топовых видеокарт
NVIDIA <http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=261c16a6a044eb1e58f3b839ce2aff18bcf8eebe>`__
(раньше требовались манипуляции с проприетарными драйверами), а его
коллега `David Airlie <https://www.openhub.net/accounts/airlied>`__
представил на рассмотрение `первый вариант реализации независимого
управления энергопотреблением для систем с несколькими
видеокартами <https://thread.gmane.org/gmane.comp.video.dri.devel/73709>`__
(сейчас, несмотря на реализацию долгожданного `GPU
offloading </content/Переключающаяся-графика-скоро-в-linux>`__ в X.org
1.13 все видеопроцессоры одновременно работают, что делает бессмысленным
какой-либо offloading).

