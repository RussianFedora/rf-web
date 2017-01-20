.. title: Как наши участники улучшают Linux десктоп
.. slug: Как-наши-участники-улучшают-linux-десктоп
.. date: 2013-08-02 17:12:29
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Aleksander
Morgado <https://www.openhub.net/accounts/aleksander_morgado>`__, инженер
дружественной нам компании `Lanedo <http://www.lanedo.com/>`__,
продолжает рассказывать о проблемах, с которыми они столкнулись при
разработке современной системы управления модемами. На этот раз он
рассказывает о нашей любимой теме - багах в проприетарных прошивках. Как
известно, качество биосов, UEFI и прочего firmware для видеокарт,
сканнеров, сетевых карт, модемов всегда было гораздо хуже "обычного"
кода, в т.ч. и проприетарного. Aleksander приводит еще `три вопиющих
примера головотяпства традиционно криворуких
firmware-программистов <http://www.lanedo.com/2013/qmi-modems-firmware-workaround-lte/>`__
в своем блоге. Но любое раздолбайство дает возможность совершить
профессиональный подвиг, и Aleksander описывает то, как эти три ошибки
(`отсутствие требуемого заголовка на
пакете <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/drivers/net/usb/qmi_wwan.c?id=6ff509af3869ccac69dcf8905fc75b9a76951594>`__,
`жестко зашитый
MAC-адрес <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/drivers/net/usb/qmi_wwan.c?id=6483bdc9d76fb98174797516a19d289eb837909e>`__,
`неправильный USB Communication Device
Descriptor <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/drivers/net/usb/qmi_wwan.c?id=cc6ba5fdaabea7a7b28de3ba1e0fe54d92232fe5>`__)
были исправлены участником Debian, `Bjørn
Mork <https://github.com/bmork>`__ и участником Fedora, `Dan
Williams <https://www.openhub.net/accounts/dcbw>`__. Исправления уже
доступны в ядре 3.10, которое уже доступно в репозиториях для Fedora 18
и Fedora 19.

Участник Fedora KDE SIG `Lukáš
Tinkl <https://fedoraproject.org/wiki/User:Ltinkl>`__ подводит итог
тому, что `они за месяц сделали для
KDE <http://ltinkl.blogspot.ru/2013/07/this-month-july-in-red-hat-kde.html>`__.

Среди прочих есть упоминание о фиче Fedora 20, `о которой вы уже
знаете </content/Новые-фичи-fedora-20>`__ - KDE переводится с KDM на
SDDM. Новость привлекла внимание `Aaron
Seigo <https://www.openhub.net/accounts/aseigo>`__, который в своей ленте
Google+ `очень высоко оценил это изменение Fedora и назвал это
образцовым примером сотрудничества upstream/downstream
разработчиков <https://plus.google.com/107555540696571114069/posts/5Q6a74h47JK>`__.

Это один из примеров наших руководящих принципов - все изменения мы
продвигаем в апстрим, помогая его изменять в нужную нам сторону.

Иногда слышны беспочвенные утверждения, что-де Fedora Community не
интересуется тем, что интересно мифическому "простому пользователю", так
вот, это неверно. Наши участники приложили руку практически ко всем
десктопным компонентам - от GNOME и KDE, до отдельных компонент,
наподобие NetworkManager, и поддержки оборудования в ядре.

