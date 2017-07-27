.. title: Wayland и NVIDIA
.. slug: wayland-i-nvidia
.. date: 2017-07-27 14:19:35 UTC+03:00
.. tags: wayland, nvidia, gnome
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Наш коллега, `Christian Schaller <https://www.openhub.net/accounts/Uraeus>`_,
`сообщает хорошие новости
<https://blogs.gnome.org/uraeus/2017/07/26/running-wayland-on-the-nvidia-driver/>`_!
Оказывается, NVIDIA не только `работает над поддержкой Wayland
<https://www.x.org/wiki/Events/XDC2014/XDC2014RitgerEGLNonMesa/nvidia-and-compositors.pdf>`_
в своих драйверах, но уже и может кое что показать.

К сожалению, чтобы запустить на проприетарных драйверах NVIDIA
`Wayland-композиторы требуется патчить
<https://lists.x.org/archives/xorg-devel/2017-July/054118.html>`_, что довольно
трудоемко. Понятно, что какой-нибудь Weston поправить относительно легко, но
скажем сразу - кто им всерьез пользуется? А вот `дорабатывать Kwin
<https://blog.martin-graesslin.com/blog/2016/09/to-eglstream-or-not/>`_ и
Mutter, это совсем другая история.

Понимая все это, инженер NVIDIA, `Miguel A. Vico
<https://github.com/mvicomoya>`_, создал `copr-репозиторий
<https://copr.fedorainfracloud.org/coprs/mvicomoya/mutter-eglstream/>`_ для
пользователей Fedora с проприетарными драйверами NVIDIA. В этом репозитории он
выложил Mutter, собранный c `EGLStream
<https://www.khronos.org/registry/EGL/extensions/KHR/EGL_KHR_stream.txt>`_.
Теперь пользователи GNOME могут попробовать Wayland в такой причудливой
конфигурации.

Пробуйте!
