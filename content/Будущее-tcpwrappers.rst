.. title: Будущее tcpwrappers
.. slug: Будущее-tcpwrappers
.. date: 2014-03-21 14:37:28
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


В рассылке systemd `предложили избавиться от
tcpwrappers <http://thread.gmane.org/gmane.comp.sysutils.systemd.devel/17884>`__,
разработка которых прекратилась в 2003 году. По ходу возникшего
обсуждения, выяснилось, что из Arch Linux их выкинули года три назад, и
никто даже и не заметил (правда надо учесть размер пользовательской
базы, и для чего используют Arch), в Debian выбрасывать не собираются,
что вполне понятно, т.к. 11 лет отсутствия разработки для них это
обычное дело, и если ПО настолько древнее, то в нем все `баги
улетучились <https://ru.wikipedia.org/wiki/Виноделие#.D0.A5.D1.80.D0.B0.D0.BD.D0.B5.D0.BD.D0.B8.D0.B5_.D0.B8_.D0.B2.D1.8B.D0.B4.D0.B5.D1.80.D0.B6.D0.BA.D0.B0>`__.

Оценив ситуацию, Lennart `предложил избавиться от tcpwrappers в
Fedora <http://thread.gmane.org/gmane.linux.redhat.fedora.devel/193871>`__,
изложив свои соображения. Ко всеобщему удивлению на свет стали ползти
живые пользователи tcpwrappers.

|image0|

.. |image0| image:: https://gs1.wac.edgecastcdn.net/8019B6/data.tumblr.com/V3plvX2eRhozkyafZMCNESUZo1_500.jpg
   :target: http://onefootinthegrave.tumblr.com/post/65840112/mudwerks-mabelmoments-kapi-zombie-cows-want
