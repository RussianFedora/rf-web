.. title: Будущие фичи Fedora 21
.. slug: Будущие-фичи-fedora-21
.. date: 2014-03-13 15:23:55
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| `График выхода Fedora
  21 <http://borntobeopen.blogspot.ru/2014/03/getting-closer-to-fedora-21-schedule.html>`__
  пока только утряхивается, а фичи будущего релиза уже начали
  появляться. Неопределенность с графиком привела к тому, что большое
  количество фич до сих пор не было анонсировано, и в списке находились
  лишь известные с `октября </content/Планы-по-переходу-на-python-3>`__
  и `ноября </content/Короткие-новости-17>`__ 2013 года `базовая
  поддержка OpenCL в Fedora
  21 <https://fedoraproject.org/wiki/Changes/OpenCL>`__, `Python3 по
  умолчанию <https://fedoraproject.org/wiki/Changes/Python_3_as_Default>`__
  и `обновление Python3 до версии
  3.4 <https://fedoraproject.org/wiki/Changes/Python_3.4>`__. Но
  определенность позволила начать планировать свои возможности, и наши
  коллеги сразу предложили ряд фич:

-  `Перевод приложений с cron jobs на timer-юниты
   systemd <https://fedoraproject.org/wiki/Changes/cron-to-systemd-time-units>`__.

-  `Унификация системных
   крипто-политик <https://fedoraproject.org/wiki/Changes/CryptoPolicy>`__.

   Это еще один шажок в сторону унифицированного общесистемного
   криптографического фреймворка, с централизованным управлением. Сейчас
   планируется ввести общесистемную установку уровня безопасности. В
   идеале, изменяя некий текстовый файл, системный администратор
   установит минимальный размер ключей, список допустимых
   криптоалгоритмов и т.п. для всей системы. Все крипто-библиотеки и
   крипто-приложения должны учитывать установленные параметры. Работы
   довольно много - это не 11 новых обоев, но мы надеемся, что наши
   коллеги успеют.

-  `Переименование фонтов Lohit Oriya и Lohit Punjabi в Lohit Odia и
   Lohit
   Gurmukhi <https://fedoraproject.org/wiki/Changes/Lohit_Odia_Gurmukhi>`__,
   как того требует правительство индийского штата Орисса.

-  `Общесистемная политика доступа к
   смарт-картам <https://fedoraproject.org/wiki/Changes/PcscAccessControl>`__.

   Ну тут все понятно. Планируется запретить неавторизованным
   пользователям и/или процессам доступ к смарт-картам.

-  `Удаление виртуальной "Provides: python-setuptools-devel" и
   соответствующих BuildRequires/Requires из
   rpm-пакетов <https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel>`__.

-  `Обновление Ruby до версии
   2.1 <https://fedoraproject.org/wiki/Changes/Ruby_2.1>`__.


| 
| На подходе еще пачка фич.

