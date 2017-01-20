.. title: И опять - новые "фичи" Fedora 20
.. slug: И-опять-новые-фичи-fedora-20
.. date: 2013-07-18 11:56:45
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| Теперь это уже не фичи, а "изменения", но пока по привычке называется
  по-старому. Итак, были анонсированы:

-  Пока официально не анонсированное изменение, так что чуть-чуть
   забегаем вперед - включение еще одного альтернативного десктопного
   окружения,
   `Enlightenment <https://fedoraproject.org/wiki/Changes/Enlightenment>`__,
   изначально запланированное на `Fedora
   19 </content/Новые-фичи-fedora-19>`__, но перенесенное из-за нехватки
   времени.

-  Включение
   `ACPICA <https://fedoraproject.org/wiki/Changes/AcpicaTools>`__,
   набора утилит для управления подсистемой ACPI (создание, получение из
   системы, и изменение таблиц ACPI).

-  Вторая попытка включить `Apache
   OpenOffice <https://fedoraproject.org/wiki/Changes/ApacheOpenOffice>`__.

   В первый раз `это было запланировано на Fedora
   19 </content/Новые-фичи-fedora-19-0>`__, но единственный
   заинтересованный участник в срок не уложился. Конечно непонятно, кто
   будет пользоваться этим умирающим гигантом с кладбища
   opensource-проектов, Apache Software Foundation, да еще и при живом
   LibreOffice, но пусть будет. Кстати, участник проектов Fedora и
   LibreOffice, `Caolán
   McNamara <https://www.openhub.net/accounts/caolan>`__ объявил о взятом
   новом рубеже - `300 диалоговых окон конвертированы в стандартный язык
   описаний
   GtkBuilder <http://blogs.linux.ie/caolan/2013/07/15/converting-libreoffice-dialogs-to-ui-format-300-conversions-milestone/>`__.

   Несколько месяцев назад `было всего
   150 </content/Короткие-новости-2>`__.

-  Будет доступен `GUI для
   DeveloperAssistant <https://fedoraproject.org/wiki/Changes/DeveloperAssistantGUI>`__.

   Изначально `devassistant предназначался начинающим
   разработчикам </content/Новые-фичи-fedora-19-0>`__, боящимся
   командной строки, и позволял с помощью командной строки создать
   скелеты приложений на различных языках. Вскоре народ заметил, что в
   таком описании devassistant что-то звучит не так, и решили написать к
   нему GUI.

-  `GNOME 3.10 <https://fedoraproject.org/wiki/Changes/Gnome3.10>`__.

-  `Интеграция технологии thin provisioning в
   LVM <https://fedoraproject.org/wiki/Changes/InstallerLVMThinProvisioningSupport>`__.

   Если кто не знает, то thin provisioning, это технология, позволяющая
   выделять ресурсов больше, чем фактически присутствует (подразумевая,
   что запрашивающий необязательно использует весь объем ресурсов
   сразу). Это очень выгодно в виртуализированных системах. С помощью
   данной фичи можно будет создавать при установке разделы больших
   объемов, выделяя ресурсы по запросу. Это позволит добиться большей
   плотности виртуальных машин.

-  Три нововведения, относящихся к IPA - `поддержка DNSSEC-зон в
   интегрированном в IPA
   DNS-сервере <https://fedoraproject.org/wiki/Changes/IPAv3DNSSEC>`__,
   `интерфейс для управления OTP (one-time password) в
   IPA <https://fedoraproject.org/wiki/Changes/IPAv3OTPUI>`__ (позволит
   развертывать полноценную систему двухфакторной аутентификации на базе
   IPA), `поддержка двунаправленных доверенных отношений из AD в
   IPA <https://fedoraproject.org/wiki/Changes/IPAv3TransitiveTrusts>`__
   (`подробнее о
   системе <https://fedoraproject.org/wiki/Changes/IPAv3TransitiveTrusts>`__).

-  Продолжается перенос всего в /usr. `В Fedora 20 будет официально
   запрещено устанавливать что-либо в /bin, /sbin, /lib,
   /lib64 <https://fedoraproject.org/wiki/Changes/NoBinDeps>`__.

-  `Больше не будет устанавливаться sendmail по
   умолчанию <https://fedoraproject.org/wiki/Changes/NoDefaultSendmail>`__.

   Почтовик на десктопной системе оставим для любителей юниксвэя из
   1980х.

-  Увы, но время syslog на десктопе также заканчивается - `rsyslog по
   умолчанию не будет
   устанавливаться <https://fedoraproject.org/wiki/Changes/NoDefaultSyslog>`__.

   Желающие смогут его установить, само собой.

-  После нескольких лет предупреждений о том, что ntpdate является более
   неподдерживаемой технологией, настало время сделать решительный шаг -
   `ntpdate будет удален из
   системы <https://fedoraproject.org/wiki/Changes/ntpdate>`__.

   Используйте ntpd.

-  После включения CRIU делается еще один шаг в направлении надежных
   атомарных и транзакционных обновлений - `В LVM будет доступен
   rollback <https://fedoraproject.org/wiki/Changes/Rollback>`__.

-  `Обновление Ruby on Rails до версии
   4.0 <https://fedoraproject.org/wiki/Changes/Ruby_on_Rails_4.0>`__.

-  `Использование дисков SSD, как кэширующих
   устройств <https://fedoraproject.org/wiki/Changes/SSD_cache>`__. Если
   вы не в курсе, то индустрия идет в сторону, намеченную `Дмитрием
   Завалишиным <http://ru.wikipedia.org/wiki/Завалишин,_Дмитрий_Константинович>`__
   в его опередившей время системе `Фантом
   ОС <http://ru.wikipedia.org/wiki/Фантом_%28ОС%29>`__, и рано или
   поздно понятия "файловая система", "локальные хранилища файлов" и
   даже "файл", уйдут в прошлое. Но до тех пор, пока стоимость
   твердотельных накопителей не пробьет цену в 10 центов за гигабайт,
   появление персистентной памяти, состоящей из объектов и библиотек, а
   не файлов, нам точно не грозит.

-  Два изменения для SSSD - `SSSD плагин для
   CIFS <https://fedoraproject.org/wiki/Changes/SSSD_CIFS_plugin>`__,
   для тесной интеграции идентификаторов пользователей из Windows и
   Linux, и `поддержка смарт-карт в
   SSSD <https://fedoraproject.org/wiki/Changes/SSSD_Smart_Card_Support>`__.

-  `Обновление обучающего десктопного окружения Sugar до версии 1.0
   (0.100) <https://fedoraproject.org/wiki/Changes/Sugar-0.100>`__.

-  Изменение уровня мэйнтейнеров - `директории с документацией для
   пакетов более не будут иметь версию в
   пути <https://fedoraproject.org/wiki/Changes/UnversionedDocdirs>`__.

   Т.е. больше не будет /usr/share/doc/libfoo-1.2.3.4/README, а просто
   /usr/share/doc/libfoo/README.

-  `Включение Vagrant и его интеграция с
   KVM <https://fedoraproject.org/wiki/Changes/Vagrant>`__.

-  `Управление доступом в libvirt на основе
   ролей <https://fedoraproject.org/wiki/Changes/Virt_ACLs>`__. Сейчас в
   libvirt нет возможности тонко разбивать права доступа по
   пользователям (пользователь Петя может запускать виртуалки A,C,D, а
   пользователь Маша может останавливать виртуалки A-D и запускать
   E,F,G). Будет доступен role-based access ко всем объекта libvirt -
   сети, хранилища, виртуалки и т.п.
-  Продолжение работы над `first-class cloud
   images </content/Другие-варианты-fedora-19>`__, начатое еще в Fedora
   19. Теперь `официальные образы Fedora для моментального развертывания
   в облаках будут доступны на
   зеркалах <https://fedoraproject.org/wiki/Changes/VisibleCloud>`__
   вместе с другими образами. ISO-образы для CDROM ушли, а эти пришли.

   Эволюция.

-  После `успешного завершения работы над
   Node.js </content/nodejs-одобрили-для-включения-в-fedora>`__ начата
   разработка новых правил для мэйнтейнеров - `стандартное расположение
   Web-ассетов <https://fedoraproject.org/wiki/Changes/Web_Assets>`__
   (гифки, шрифты, скрипты, и т.п.). Unix, это не выбор, это жесткая
   стандартизация!
-  Включение `X2Go <https://fedoraproject.org/wiki/Changes/X2Go>`__,
   замена заброшенного nx-libs для удаленного доступа к системе по
   протоколу NX.


| 
