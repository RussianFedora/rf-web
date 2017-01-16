.. title: Релиз Fedora 18 Spherical Cow
.. slug: Релиз-fedora-18-spherical-cow
.. date: 2013-01-15 18:45:20
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: bookwar

**Это архивная статья**


| |Fedora 18| Итак, самый ожидаемый, восьмикратно отложенный,
  вакуумно-сферический релиз **Fedora 18 Spherical Cow** официально
  состоялся!

Пожалуй самыми заметными в этом выпуске являются `новый
интерфейс <http://fedora.cz/wp-content/uploads/2012/09/anaconda-450x337.png>`__
переработанного установщика Anaconda (именно этот компонент и доставил
больше всего хлопот при тестировании) и сервис
`FirewallD <https://fedoraproject.org/wiki/FirewallD>`__, ставший
файерволом по умолчанию. При этом если вы обновляете, а не
переустанавливаете систему, активным файерволом останется iptables, а
для перехода на firewalld сервис придется установить и активировать
вручную. Также не забудьте о переносе */tmp* на *tmpfs*. Все большие
временные файлы теперь следует складывать в */var/tmp*

Остальные подробности и немаленький список нововведений можно прочесть в
`Примечаниях к
выпуску <http://docs.fedoraproject.org/ru-RU/Fedora/18/html/Release_Notes/index.html>`__
на русском языке (отдельное спасибо всем участвовавшим в переводе).


**Скачать** образы можно через
`торренты <http://torrent.fedoraproject.org/>`__ или `любыми
другими <https://fedoraproject.org/en/get-fedora-all>`__ способами.

Также вы можете воспользоваться сборкой `RFRemix
18 <http://www.russianfedora.ru/content/%D0%92%D1%8B%D1%88%D0%B5%D0%BB-rfremix-18>`__
с включенными по умолчанию дополнительными репозиториями.


-  `Install
   Guide <http://docs.fedoraproject.org/en-US/Fedora/18/html/Installation_Guide/index.html>`__
-  `Инструкция по
   обновлению <http://wiki.russianfedora.ru/index.php?title=%D0%9E%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_Fedora_%28%D0%B8%D0%BB%D0%B8_RFRemix%29_%D1%81_%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E_yum#.D0.9E.D0.B1.D0.BD.D0.BE.D0.B2.D0.BB.D0.B5.D0.BD.D0.B8.D0.B5_Fedora.28RFRemix.29_17_.D0.B4.D0.BE_Fedora.28RFRemix.29_18>`__

Следующий релиз Fedora 19 Schrödinger's Cat планируется к выпуску в
конце мая.


.. |Fedora 18| image:: https://fedoraproject.org/static/images/f18_fpo_screenshot.png

