.. title: Не только шрифты из Windoz
.. slug: Не-только-шрифты-из-windoz
.. date: 2014-09-13 21:58:08
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Для некоторых наших участников до сих пор остается загадкой
непреодолимое желание некоторых наших пользователей добавить в систему
ряд известных Windoz-шрифтов. Ведь многие из нас живут без них, и
ничего!
А вот наш коллега, `Caolán
McNamara <https://www.openhub.net/accounts/caolan>`__, начал совсем уж
необычный эксперимент. `Он устанавливает в Linux-систему шрифты из Mac
OS X, и пытается их использовать в
LibreOffice <http://caolanm.blogspot.com/2014/09/more-font-support.html>`__.

Сразу скажем, что мы не уверены в законности этого действия, если у вас
нет `легально купленной копии Mac OS
X <https://btdigg.org/search?info_hash=&q=Mac+OS+X+iso>`__, но Caolán
рискнул. В результате он получил необычный результат. Шрифты в
fontconfig есть, а LibreOffice их не видит. Как обычно, для наших
коллег, Caolán не побежал жаловаться в чатик или форум, а сел
разбираться. Выяснилось, что `в LibreOffice не поддерживалась версия "2"
ttс-фонтов <http://cgit.freedesktop.org/libreoffice/core/commit/?id=02f8f89>`__,
`нужно было добавить поддержку кодировки имени фонтов, используемую в
Mac OS
X <http://cgit.freedesktop.org/libreoffice/core/commit/?id=9436ae9>`__,
`перевести Apple Language ID во внутреннее представление
LibreOffice <http://cgit.freedesktop.org/libreoffice/core/commit/?id=9a502e6>`__,
и необходимо было внести ряд других мелких изменений.

Работа еще не закончена, но уже кое что работает. Теперь вы можете нас
удивлять не только странным желанием использовать Windoz-шрифты, но и
желанием использовать Mac OS X-шрифты.

