.. title: Random seed в облаках
.. slug: random-seed-в-облаках
.. date: 2014-02-19 15:00:20
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Мы уже говорили </content/Коротко-новости-графической-подсистемы>`__,
что пользователям любых других дистрибутивов необходимо следить за
новостями проекта Fedora и участвовать в тестовых днях, ведь проблемы, с
которыми сталкиваемся мы, появятся в ваших дистрибутивах через
полгода-год-полтора (ну или лет через 5-10, если вы используете Debian).

И вот, мы получили этому еще одно подтверждение.

`Dustin Kirkland <http://www.linkedin.com/in/dustinkirkland>`__, Cloud
Solutions Product Manager компании Canonical, `попытался описать
проблему отсутствия достаточного количества энтропии на виртуальных
машинах <http://blog.dustinkirkland.com/2014/02/random-seeds-in-ubuntu-1404-lts-cloud.html>`__,
и подходы к решению. К сожалению, он хотя и в курсе правильного ответа,
`Virtio-RNG <http://wiki.qemu-project.org/Features-Done/VirtIORNG>`__,
но вынужден отказаться от него, т.к. оно недоступно в ряде облачных
систем. Энтропию, если ее нет, взять неоткуда, поэтому его заметка
превратилась в печальную попытку вытащить себя за волосы из болота, чем
не преминул воспользоваться, чтоб похихикать известный тролль, Lennart
Poettering, `в своей ленте
Google+ <https://plus.google.com/+LennartPoetteringTheOneAndOnly/posts/K22yyHRc6hn>`__.

Наши коллеги по Fedora, разумеется, увидели проблему задолго до того,
как ее заметили в Canonical. Участник коммьюнити Fedora, разработчик
таких проектов, как kernel и bitcoin, инженер BitPay, `Jeff
Garzik <https://plus.google.com/105424721218711536033/about>`__,
`заинтересовался вопросом еще в 2008
году <http://thread.gmane.org/gmane.linux.kernel/681003>`__, и сразу
после обсуждения тогда и была добавлена необходимая поддержка в ядро.

Еще через несколько лет была добавлена поддержка в
`Qemu <http://thread.gmane.org/gmane.comp.emulators.qemu/156744>`__, и в
`libvirt <http://thread.gmane.org/gmane.comp.emulators.libvirt/73027>`__,
которая была реализована инженерами Red Hat, IBM и Collabora. В хостовых
машинах c Fedora 19 и выше все уже работает, т.к. когда все кирпичики
стали доступны, то `Virtio-RNG был оформлен фичей Fedora
19 <https://fedoraproject.org/wiki/Features/Virtio_RNG>`__. Разумеется,
Virtio-RNG будет доступен как в `выходящей в этом году
RHEL7 <https://bugzilla.redhat.com/923008>`__, так и `был бэкпортирован
в
RHEL6 <http://thread.gmane.org/gmane.comp.emulators.ovirt.user/13042/focus=13050>`__.

Так что в будущем выбирайте облачных провайдеров с облаками на основе
RHEL6 / RHEL7 или Fedora (облака на базе Fedora предлагают, например,
наши друзья из `Pantheon Systems <https://www.getpantheon.com/>`__, о
чьем облачном решении `мы уже
упоминали </content/Короткие-новости-про-облака>`__).

