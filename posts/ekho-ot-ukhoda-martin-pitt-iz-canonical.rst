.. title: Эхо от ухода Martin Pitt из Canonical
.. slug: ekho-ot-ukhoda-martin-pitt-iz-canonical
.. date: 2017-05-14 15:06:37 UTC+03:00
.. tags: oops, ubuntu, canonical, hr, redhat, cockpit
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Помните новость, что `Martin Pitt, человек-пароход, ушел в Red Hat
</posts/canonical-poteriala-eshche-paru-razrabotchikov/>`_? Так вот, у нее
появилось продолжение.

Мы знали, что в Canonical очень мало разработчиков, и знаем, что сейчас они
переживают тяжелые времена. Но мы даже и не подозревали, как на самом деле там
плохи дела. Недавно мы `услышали об Ubuntu-специфичной ошибке
<https://www.linux.org.ru/news/security/13413973>`_ в очередном суверенном
компоненте, `LightDM <https://ru.wikipedia.org/wiki/LightDM>`_, выбранном лишь
для того, чтобы импортозаместить аналогичный компонент GNOME. Оказывается, `про
ошибку стало известно несколько месяцев назад
<https://bugs.launchpad.net/ubuntu/+source/lightdm/+bug/1663157>`_, но
исправить они не смогли, т.к. Мartin Pitt был единственный, который разбирался
в том, что у них происходит. `Прямая речь
<https://bugs.launchpad.net/ubuntu/+source/lightdm/+bug/1663157/comments/5>`_:

        Ow. Unfortunately I don't have any information on how to fix this since
        most of the work on guest sessions and systemd was done by Martin Pitt.

        -- `Robert Ancell <https://plus.google.com/+RobertAncell>`_

Дожили. Но кое кто сообщает, что `это еще не самое плохое, что происходит
<https://www.techradar.com/news/what-happened-at-canonical>`_.

Вообще, странно все это. Ведь Martin, даже работая в Red Hat, продолжает
уделять время улучшению Ubuntu. Например, недавно он `включил в состав Debian и
Ubuntu Cockpit <https://piware.de/post/2017-05-09-cockpit-in-debian-ubuntu/>`_,
веб-интерфейс для управления системой. Она разработана инженерами Red Hat и
пойдет на замену еще одной дистроспецифичной системы управления, `Landscape
<https://landscape.canonical.com>`_, которая к тому же еще и проприетарная.
