.. title: Планирующиеся изменения в Fedora 33
.. slug: planiruiushchiesia-izmeneniia-v-fedora-33
.. date: 2020-04-17 20:24:54 UTC+03:00
.. tags: binutils, berkleydb, mingw, python, openldap, rpm, llvm, rhel
.. category: Fedora Changes
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Как это у нас часто бывает, `релиз Fedora 32 откладывается из-за найденных ошибок <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/HXSBRI4LRWKKHLUH2OI4UPBKJJKGCDQR/>`_. Качество для нас крайне важно, поэтому мы лучше перенесем выпуск, но исправим найденное при тестировании. А пока мы уже начали собирать фичи следующей Fedora 33. Пока приняли следующие:

- `Binutils обновляется с версии 2.33 до 2.34 <https://fedoraproject.org/wiki/Changes/BINUTILS234>`_.
- `Образы Fedora Cloud будут обновляться каждый месяц <https://fedoraproject.org/wiki/Changes/CloudProviderImageUpdates>`_.
- `ELN, или Enterprise Linux Next <https://fedoraproject.org/wiki/Changes/ELN_Buildroot_and_Compose>`_. Очень интересное изменение, о нем расскажем чуть ниже.
- `Обновление MinGW <https://fedoraproject.org/wiki/Changes/F33MingwEnvToolchainUpdate>`_.
- `Улучшения для сборки glibc32 <https://fedoraproject.org/wiki/Changes/glibc32_Build_Adjustments>`_. Это пакет, нужный для сборки 32- и 31-битных приложений на 64-битных системах, чтобы обойти ограничения Koji.
- `Пакеты будут собираться с Link-time Optimization по умолчанию <https://fedoraproject.org/wiki/LTOByDefault>`_.
- `Обновление Make с версии 4.2 до 4.3 <https://fedoraproject.org/wiki/Changes/MAKE43>`_.
- `Модули будут доступны при сборке RPM <https://fedoraproject.org/wiki/Changes/Modules_In_Non-Modular_Buildroot>`_.
- `OpenLDAP будет поставляться с BerkleyDB и HDB, собранными как динамические библиотеки <https://fedoraproject.org/wiki/Changes/OpenLDAPwithBerkleyDBasModule>`_. Мы постепенно отказываемся от BerkleyDB, и это еще один шаг.
- `Обновление Python с версии 3.8 до версии 3.9 <https://fedoraproject.org/wiki/Changes/Python3.9>`_ и удаление пакетов с `Python 2.6 <https://fedoraproject.org/wiki/Changes/RetirePython26>`_ и `Python 3.4 <https://fedoraproject.org/wiki/Changes/RetirePython34>`_.
- `RPM 4.16.0 <https://fedoraproject.org/wiki/Changes/RPM-4.16>`_ и `перевод RPM с BerkleyDB на SQLite <https://fedoraproject.org/wiki/Changes/Sqlite_Rpmdb>`_.
- `Отказ от поддержки TLS 1.0 и TLS 1.1 и ряда слабых криптоалгоритмов <https://fedoraproject.org/wiki/Changes/StrongCryptoSettings2>`_. Они будут доступны в OpenSSL, если кому-то будет надо, но по умолчанию их использовать не получится.
- `Компиляторы CC и C++ будут выбираемы <https://fedoraproject.org/wiki/Changes/Use-Update-Alternatives-For-usr-bin-cc>`_. В будущем можно будет задействовать LLVM/Clang, например.
- `При обновлении сервисы будут перезапускаться в самом конце обновления <https://fedoraproject.org/wiki/Changes/Restart_services_at_end_of_rpm_transaction>`_. Вместо скриптлета, будет декларативное указание в сервисе systemd. Еще один шаг к декларативному подходу к управлению сервисами, вместо устаревшего процедурного, когда мы указывали не *что* нам надо делать, а *как* надо.

Так вот, про ELN. Это изменение позволит тестировать сборку пакетов в будущем RHEL. Все началось из-за слухов, что в RHEL9 в качестве x86_64 будет подразумеваться процессор с очень современным набором команд. В Fedora, в качестве базового x86_64-процессора сейчас используют старинный AMD K8 из 2003 года, в который, как говорят, игры загружались с магнитофонных кассет.

.. image:: /images/amd-k8-hardware.jpg
   :align: center

.. class:: align-center

Типичный программист работает на компьютере с процессором AMD K8.

Если в RHEL потребуют использовать более современный процессор, то любой x86_64 уже не подойдет, да и не всякое ПО соберется. Сначала `предложили не дожидаясь RHEL повысить требоваия <https://fedoraproject.org/wiki/Changes/x86-64_micro-architecture_update>`_ - отказались, так как даже в Intel не все процессоры подойдут, которые сейчас выпускаются. Затем `предложили добавить еще одну архитектуру сборки <https://fedoraproject.org/wiki/Changes/Additional_buildroot_to_test_x86-64_micro-architecture_update>`_ - процессор-то, получается, не x86_64, как мы считаем. Отказались и от этого в пользу более общего решения. Теперь в рамках этой цели сборки (наподобие f32, f31, rawhide, epel7 и т.д.) можно будет вести разработку в рамках будущего RHEL. Это будет как бы Rawhide, но в нем можно будет тестировать небольшие изменения (оптимизации, команды процессора).

