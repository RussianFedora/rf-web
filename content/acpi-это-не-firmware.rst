.. title: ACPI это не firmware
.. slug: acpi-это-не-firmware
.. date: 2014-03-22 21:31:49
.. tags: arm, acpi, canonical
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Призыв Марка Шатлворта отказаться от проприетарного firmware
</content/mark-shuttleworth-против-sbsa>`__, в частности от ACPI, продолжает
обсуждаться в блогосфере. Ну, конечно, это типичная ситуация для вбросов от
Canonical.

Уже тогда Olof Johansson `заметил
<https://plus.google.com/+OlofJohansson/posts/PnYVv3Mw7mD>`__, что Марк путает
ACPI и `SMM <https://en.wikipedia.org/wiki/System_Management_Mode#Problems>`__,
а сейчас это `подчеркнул в своем посте
<https://plus.google.com/+GraemeGregory/posts/MaEhEZzXUC9>`__ инженер Linaro,
Graeme Gregory. ACPI, это не firmware, а описание системы, дополненное
документированным байткодом, исполняющимся ядром операционной системы. Т.е. это
вполне открытый стандарт, которым `с недавних пор управляет UEFI Forum
</content/Новости-основных-компонентов-base-os>`__, а не какой-нибудь `злой
вендор <http://www.microsoft.com>`__.

Народ почти разобрался, и начал глумиться над Марком, когда в комменты к
`одобрительному посту
<https://plus.google.com/111049168280159033135/posts/bFyQKjuKfms>`__ у Greg
Kroah-Hartman пришел известный хулиган и матершинник Linus Torvalds, и
началось:

::

    LT: Is there a way to "-1" idiotic posts? ...anybody who claims that the
    regular BIOS isn't firmware is a f*cking moron. ACPI tables and AML scripts are
    firmware. Anybody who claims anything else is delusional. ...Greg
    Kroah-Hartman, why are you spreading manure like this?  Is there some PR
    workgroup shilling for ACPI that I'm unaware of? Is it due to the whole ARM
    brouhaha vs devicetree?

    GG: Linus Torvalds you fucking imbecile, see look how cool I am, I can swear
    too.  What a grown up awesome dude you are, fuck off back to your cave and shut
    up until you have worthwhile comments to make! 

Мы с интересом продолжаем следить за дискуссией двух разработчиков ядра.
Вообще, походу `у них в ядре там весело
</content/Что-происходит-на-мероприятиях-kernel-девелоперов>`__.

К сожалению, наш коллега и специалист по ACPI, Jon Masters, не участвует в
последнее время в плодотворных обсуждениях, т.к.  `готовится к Бостонскому
Марафону <https://plus.google.com/+JonMasters/posts/3FDh2kGZG2d>`__.
