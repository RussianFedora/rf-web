.. title: Проблемы с зеркалами репозиториев на Украине
.. slug: problemy-s-dostupom-na-ukraine
.. date: 2017-05-31 15:22:11 UTC+03:00
.. tags: yandex, политика, санкции
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Поступают сведения, что у пользователей с Украины появились проблемы с dnf/yum
при обновлении системы. Дело в том, что менеджер пакетов получает российские
адреса в списке mirrorlist, которые запрещены на Украине. Проблема, к
сожалению, политическая, но для нее есть ряд технических временных решений. В
Yum можно было в ``/etc/yum/pluginconf.d/fastestmirror.conf`` добавить
следующие опции:

::

        [main]
        ...
        # Exclude slow/overloaded mirrors
        exclude=mirror.slow.com, ftp.slow.mirror.com

Работает-ли это в DNF - честно говоря, непонятно, но есть и другие варианты.
