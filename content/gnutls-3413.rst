.. title: GnuTLS 3.4.13
.. slug: gnutls-3413
.. date: 2016-06-08 15:35:26
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Несмотря на `недавний выход GnuTLS 3.5.0 </content/gnutls-350>`__, наш
коллега, `Nikos
Mavrogiannopoulos <https://www.openhub.net/accounts/nmav>`__, был
вынужден отвлечься, чтобы `выкатить промежуточную версию -
3.4.13 <https://thread.gmane.org/gmane.comp.encryption.gpg.gnutls.devel/8572>`__.

Оказалось, что если приложение, слинкованное с библиотекой, запущено с
setuid, то появляется возможность перезаписать произвольный файл в
системе. Напомним, что в systemd `уже используются ambient
capabilities </content/systemd-230>`__, и наверное, в большинстве
случаев запускать приложение с setuid уже необязательно. Конечно, эта
функциональность неюниксвейна, работает только на Linux, и наверняка
нарушает какой-нибудь стандарт 1987 года.

