.. title: Fedora 26
.. slug: fedora-26
.. date: 2017-07-11 17:52:01 UTC+03:00
.. tags: fedora
.. category: Fedora Changes
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Официально объявили о выходе `Fedora 26 <https://fedoramagazine.org/fedora-26-is-here/>`_.

`На OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=46837>`_ уже перечислили наиболее
`заметные <https://docs.fedoraproject.org/en-US/Fedora/26/html/Release_Notes/index.html>`__
`изменения <http://fedoraproject.org/wiki/Releases/26/ChangeSet>`__ в
Fedora 26:

-  В состав включён выпуск рабочего стола `GNOME
   3.24 <https://www.opennet.ru/opennews/art.shtml?num=46239>`__ с
   поддержкой режима ночной подсветки, новым приложением для просмотра
   кулинарных рецептов, улучшением области уведомлений и расширением
   поддержки самодостаточных пакетов Flatpak;
-  В инсталлятор Anaconda
   `добавлен <https://fedoraproject.org/wiki/Changes/AnacondaBlivetGUI>`__
   `blivet-gui <https://fedoraproject.org/wiki/Blivet-gui>`__ с
   реализаций альтернативного интерфейса для разбивки разделов с
   поддержкой LVM (включая LVM cache, LVM RAID, Thin LVM), Btrfs
   (включая Btrfs RAID, подразделы и снапшоты), MD RAID, шифрования
   накопителя при помощи LUKS;
-  `Добавлена <https://blogs.gnome.org/uraeus/2017/03/22/another-media-codec-on-the-way/>`__
   поддержка кодека для многоканального кодирования звука AC-3 (Dolby
   Digital), срок действия патентов на который
   `истёк <https://www.opennet.ru/opennews/art.shtml?num=46225>`__ и
   который теперь можно использовать без оплаты лицензионных отчислений.
   AC-3 применяется в стандартах цифрового телевидения (ATSC, DVB), на
   дисках DVD и Blu-ray, в системах потокового интернет-вещания с
   поддержкой объёмного звука 5.1.
-  `Развивается <https://fedoraproject.org/wiki/Changes/Modular_Server_Preview>`__
   предварительный вариант `модульной серверной
   редакции <https://www.opennet.ru/opennews/art.shtml?num=45879>`__
   дистрибутива, в которой конечные приложения поставляются в виде
   отдельно обновляемых модулей, жизненный цикл которых не привязан к
   другим приложениям и основной начинке дистрибутива;
-  `Сформирован <https://fedoraproject.org/wiki/Changes/BaseRuntime>`__
   первый выпуск Base Runtime, модуля с базовой операционной системой,
   который может выступать в качестве основы для сборки и как
   зависимость для модулей с приложениями. Base Runtime является основой
   модульного выпуска Fedora 26 Server. Для сборки модулей в
   инфраструктуре
   `запущен <https://fedoraproject.org/wiki/Changes/ModuleBuildService>`__
   сервис Module Build Service;
-  Пакетный менеджер DNF обновлён до версии
   `2.0 <https://www.opennet.ru/opennews/art.shtml?num=45730>`__, в
   состав которой включён плагин Repoquery для поиска пакетов во внешних
   репозиториях (аналог "rpm -q" для удалённого репозитория). Добавлена
   команда "dnf check" для проверки целостности локальной БД packagedb и
   вывода информации о возможных проблемах. Добавлена команда "dnf
   upgrade-minimal", позволяющая обновить каждый пакет до самой свежей
   версии с улучшениями или исправлениями ошибок и уязвимостей;
-  Для сборки пакетов
   `задействован <https://fedoraproject.org/wiki/Changes/GCC7>`__ выпуск
   набора компиляторов `GCC
   7 <https://www.opennet.ru/opennews/art.shtml?num=46487>`__.
   `Обновлён <https://fedoraproject.org/wiki/Changes/Fedora26CFlags>`__
   применяемый по умолчанию набор флагов компиляции для C/C+, прекращено
   использование флага "-mtune=atom". Ранее запланированные для
   включения флаги "-Werror=implicit-function-declaration" и
   "-Werror=implicit-int" пока оставлены неактивными;
-  В качестве реализации pkg-config
   `задействован <https://fedoraproject.org/wiki/Changes/pkgconf_as_system_pkg-config_implementation>`__
   пакет pkgconf, предоставляющий улучшенные средства обработки файлов
   .pc и стабильный библиотечный ABI/API для интеграции с приложениями;
-  Для сохранения и обработки core-дампов по умолчанию
   `задействован <https://fedoraproject.org/wiki/Changes/coredumpctl>`__
   сервис systemd-coredump. Для вывода списка core-дампов и их
   извлечения из БД Journal предложена утилита coredumpctl;
-  Python
   `обновлён <https://fedoramagazine.org/python-3-6-0-fedora-26/>`__ до
   версии 3.6.0. В состав включена обучающая среда `Python Classroom
   Lab <https://fedoraproject.org/wiki/Changes/PythonClassroomLab>`__;
-  Задействованы новые выпуски Glibc 2.25, PHP 7.1, Go 1.8, Ruby 2.4,
   GHC (Haskell) 8.0, LDC (язык D) 1.1.0, Boost 1.63.0, Zend Framework
   3, BIND 9.11;
-  Из поставки
   `удалён <https://fedoraproject.org/wiki/Changes/RetireSynapticsDriver>`__
   драйвер для тачпадов xorg-x11-drv-synaptics, вместо которого следует
   использовать xorg-x11-drv-libinput;
-  На системах AARCH64
   `включена <https://fedoraproject.org/wiki/Changes/aarch64-48bitVA>`__
   поддержка 48-разрядного виртуального адресного пространства;
-  B интерфейсе Fedora Media Writer добавлена возможность записи на
   SD-карты системных образов для ARM-архитектуры;
-  `Подготовлена <https://fedoraproject.org/wiki/Changes/LXQt_Spin>`__
   spin-сборка с рабочим столом
   `LXQt <https://www.opennet.ru/opennews/art.shtml?num=45801>`__ (Qt
   Lightweight Desktop Environment), развиваемым объединённой командой
   разработчиков проектов LXDE и Razor-qt;
-  `Подготовлен <https://fedoraproject.org/wiki/Changes/ContainerMinimalImage>`__
   новый минималистичный образ для создания изолированных контейнеров,
   содержащий минимально возможный набор компонентов, но при этом, в
   отличие от Atom, включающий полноценный пакетный менеджер dnf и
   возможность устанавливать произвольные пакеты из штатных
   репозиториев;
-  OpenSSL обновлён до версии
   `1.1.0 <https://www.opennet.ru/opennews/art.shtml?num=45027>`__ с
   поддержкой алгоритмов
   `scrypt <https://ru.wikipedia.org/wiki/Scrypt>`__,
   `X25519 <https://en.wikipedia.org/wiki/Curve25519>`__ (`RFC
   7748 <https://tools.ietf.org/html/rfc7748>`__), стандарта
   `Certificate
   Transparency <https://www.certificate-transparency.org/>`__,
   потокового шифра `ChaCha20 <http://cr.yp.to/chacha.html>`__ и
   алгоритма аутентификации сообщений (MAC)
   `Poly1305 <http://cr.yp.to/mac.html>`__. Прекращена поддержка
   устаревших технологий, в том числе удалены компоненты, обеспечивающие
   работу SSLv2, Kerberos, 40- и 56-разрядных шифров. Из набора шифров
   по умолчанию исключены алгоритмы
   `RC4 <https://www.opennet.ru/opennews/art.shtml?num=42907>`__ и
   `3DES <https://www.opennet.ru/opennews/art.shtml?num=45023>`__;
-  `Включено <https://fedoraproject.org/wiki/Changes/SSSDCacheForLocalUsers>`__
   определение параметров всех пользователей через NSS-модуль SSSD
   (System Security Services Daemon), обеспечивающий более высокую
   производительность за счёт кэширования содержимого локальных баз в
   памяти;
-  В качестве реализации PKCS#11 вместо Coolkey
   `задействован <https://fedoraproject.org/wiki/Changes/Replace_Coolkey_with_OpenSC>`__
   пакет OpenSC, что позволило расширить спектр поддерживаемых
   дистрибутивом смарт-карт;
-  В репозиторий включён пакет
   `snapd <https://github.com/snapcore/snapd>`__ с инструментарием для
   управления самодостаточными пакетами в формате
   `snap <https://www.opennet.ru/opennews/art.shtml?num=44601>`__. Для
   начала работы с пакетами в формате Snap пользователям Fedora Linux
   теперь достаточно выполнить "sudo dnf install snapd", после чего
   можно использовать утилиту snap. В момент первой установки snap в
   систему будет установлен snap-пакет core c набором базовых библиотек
   для функционирования пакетов snap. Так как для изоляции в snap
   используется механизм AppArmor, который не поддерживается в Fedora,
   то пакеты запускаются без применения изоляции, т.е. нужно соблюдать
   осторожность и не устанавливать непроверенные приложения.

Одновременно для Fedora 26 `введены в строй <http://rpmfusion.org/>`__
"free" и "nonfree" репозитории проекта RPM Fusion, в которых доступны
пакеты с дополнительными мультимедиа приложениями (MPlayer, VLC, Xine),
видео/аудио кодеками, поддержкой DVD, проприетарными драйверами AMD и
NVIDIA, игровыми программами, эмуляторами.
