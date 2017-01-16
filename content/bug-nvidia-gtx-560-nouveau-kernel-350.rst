.. title: [BUG] nvidia GTX 560 + nouveau + kernel 3.5.0
.. slug: bug-nvidia-gtx-560-nouveau-kernel-350
.. date: 2012-09-02 15:35:54
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: elemc

**Это архивная статья**


В ядрах версии выше 3.5.0 обнаружился неприятный
`баг <https://bugzilla.redhat.com/show_bug.cgi?id=850763>`__ с nouveau.

В текстовом режиме все отлично работает, а при входе в Х-ы экран мигает,
предупреждения ядра сыпятся — кошмар! :)
Тем, у кого это проявляется эта ошибка, совет: откатывайтесь к ядру
3.4.6-4, пока иных вариантов нет.

Ну и конечно подписываемся
`RHBZ#850763 <https://bugzilla.redhat.com/show_bug.cgi?id=850763>`__,
подтверждаем.

