.. title: Опять изменения в Fedora 33
.. slug: f-33-new-features-3
.. date: 2020-07-17 16:53:54 UTC+03:00
.. tags: arm, btrfs, gnome, cmake, dmraid, haskell, glibc, llvm, node.js, networkmanager, python, openldap, sid, swap, zram, nano, vim
.. category: Fedora Changes
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Одобрили еще несколько фич будущей Fedora 33.

- `Aarch64 Pointer Authentication & Branch Target Enablement <https://fedoraproject.org/wiki/Changes/Aarch64_PointerAuthentication>`_. Технология повышения безопасности кода на соответствующей платформе.
- `По умолчанию будет использоваться файловая система btrfs <https://fedoraproject.org/wiki/Changes/BtrfsByDefault>`_. Договориться по этой фиче было непросто. Некоторое время назад, у нас было полно историй про то, как кто-то начал использовать файловой системой для /home и быстро потерял все данные. Плюс в RHEL её отключили. Посмотрим, что получится в этот раз. Наши коллеги пока сдержанно отзываются, но `отмечают <https://blog.verbum.org/2020/07/14/on-btrfs/>`_ ценность fs для контейнеров и виртуалок.
- `Переход на приемлемое для апстрима решение для индикации успешности загрузки <https://fedoraproject.org/wiki/Changes/CleanupGnomeHiddenBootMenuIntegration>`_. Сейчас мы используем Fedora-специфичные патчи для GNOME, чтобы не показыватьв загрузчике пункты меню, которые не привели к успешной загрузке. К сожалению, они в таком состоянии, что послать в апстрим их не получится, и требуют переработки.
- `RPM-макросы CMake будут исправлены, чтобы автоматически делать out-of-tree builds <https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds>`_. Сейчас сборка по умолчанию происходит в той директории, куда распаковались исходники. Сам апстрим проекта не рекомендует этого и мы будем поддерживать их в этом.
- Удаление пакетов `pytoml <https://fedoraproject.org/wiki/Changes/DeprecatePytoml>`_, `mod_php <https://fedoraproject.org/wiki/Changes/drop_mod_php>`_, `zanata <https://fedoraproject.org/wiki/Changes/Zanata_removal>`_.
- Отключить `активацию dmraid при первом запуске системы <https://fedoraproject.org/wiki/Changes/DisableDmraidOnFirstRun>`_. Сейчас она копируется прямо с LiveCD. Заодно `удалить device-mapper-multipath с LiveCD <https://fedoraproject.org/wiki/Changes/RemoveDeviceMapperMultipathFromWorkstationLiveCD>`_. Если вам надо, то ставьте сами.
- Обновление `GHC до версии 8.8 <https://fedoraproject.org/wiki/Changes/GHC_8.8_and_LTS16>`_, `Glibc до версии 2.32 <https://fedoraproject.org/wiki/Changes/GLIBC232>`_, `LLVM до версии 11 <https://fedoraproject.org/wiki/Changes/LLVM-11>`_, `LXQt до версии 0.15.0 <https://fedoraproject.org/wiki/Changes/LXQt_0.15.0>`_, `Node.js до версии 14 <https://fedoraproject.org/wiki/Changes/Nodejs14x>`_.
- `Обновление IBus до версии 1.5.23 <https://fedoraproject.org/wiki/Changes/IBus_1.5.23>`_. Это изменение поможет тем, кто пока еще почему-то не использует GNOME, так как там лучше интеграция с xcb.
- `Включение EarlyOOM в версии для KDE <https://fedoraproject.org/wiki/Changes/KDEEarlyOOM>`_. Наверное, KDE в этом нуждается.
- `Настройки модульных репозиториев будут поставляться в отдельном пакете <https://fedoraproject.org/wiki/Changes/ModularReposSubpackage>`_.
- `Переход на другой формат записей для NetworkManager <https://fedoraproject.org/wiki/Changes/NetworkManager_keyfile_instead_of_ifcfg_rh>`_.
- `Полный запрет на прекомпилированный байткод для питона <https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3>`_.
- `Прекращается поставка non-threaded версии OpenLDAP <https://fedoraproject.org/wiki/Changes/OpenLDAPwithoutNonthreadedLibraries>`_.
- `Интеграция python extras в RPM <https://fedoraproject.org/wiki/Changes/PythonExtras>`_.
- `Макрос %{__python} будет вызывать ошибку при сборке RPM <https://fedoraproject.org/wiki/Changes/PythonMacroError>`_.
- Включение в систему `Storage Instantiation Daemon <https://fedoraproject.org/wiki/Changes/SID>`_, сервис, который будет централизованно управлять и настраивать устройства хранения.
- `Swap будет располагаться на ZRAM <https://fedoraproject.org/wiki/Changes/SwapOnZRAM>`_, виртуальном разделе, расположенном в памяти. Непонятно, почему с 32 гигами оперативы все ещё нужет свап, но, видимо, такова наша судьба.
- `По умолчанию будет использоваться nano, а не vim <https://fedoraproject.org/wiki/Changes/UseNanoByDefault>`_.

И наконец важнейшее! `Нескучные анимированные обои! <https://fedoraproject.org/wiki/Changes/DefaultAnimatedBackground>`_.
