.. title: Новый фронтэнд для libvirt
.. slug: Новый-фронтэнд-для-libvirt
.. date: 2013-06-28 23:41:48
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Инженер IBM и разработчик Qemu/KVM, `Anthony
Liguori <https://www.openhub.net/accounts/aliguori>`__, в своей ленте
Google+
`анонсировал <https://plus.google.com/109316704354866510115/posts/d38trgeiV3r>`__
новый проект - фронтэнд для libvirt, написанный на HTML5,
`kimchi <https://github.com/kimchi-project/kimchi>`__. Если кому-то
(как, например, лично мне) не нравится интерфейс virt-manager, а virsh
кажется слишком уж низкоуровневым, то этот новый проект выглядит как
неплохая замена. У кого есть аккаунт на GitHub, то присоединяйтесь -
форкайте и дописывайте функциональность!
А в это время `Rich W.M. Jones <http://people.redhat.com/~rjones/>`__
уже написал пару новых плагинов для своего
`nbdkit <https://github.com/libguestfs/nbdkit>`__, о котором вы `уже
слышали </content/Новый-проект-rich-wm-jones-nbdkit>`__ - `плагин для
прозрачной работы с дисками, сжатыми с помощью
xz <https://rwmj.wordpress.com/2013/06/24/xz-plugin-for-nbdkit/>`__, и
`плагин для использования функционала из VMware
VDDK <https://rwmj.wordpress.com/2013/06/27/vmware-vddk-for-nbdkit/>`__.

Теперь диски VMDK можно открывать и с помощью открытых приложений, и с
помощью проприетарных блобов от VMware.

