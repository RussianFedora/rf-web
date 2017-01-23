.. title: Разработка SELinux-модуля для приложения
.. slug: razrabotka-selinux-modulia-dlia-prilozheniia
.. date: 2017-01-23 20:05:26 UTC+03:00
.. tags: HOWTO, security, selinux, перепост
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

На Хабрахабре `опубликовали статью <https://habrahabr.ru/post/320100/>`_, посвященную настройке SELinux:

        .. rubric:: Давным-давно, в далекой-далекой стране
           :name: давным-давно-в-далекой-далекой-стране

        |image1|\ … государственная служба NSA разработала систему безопасности
        для ядра и окружения Linux, и назвала ее SELinux. И с тех пор люди
        разделились на две категории: disabled/permissive и enforcing. Сегодня я
        покажу вам путь Силы и переведу на другую сторону всех желающих.

        .. rubric:: Предположения
           :name: предположения

        В тексте будет содержаться много технической информации, поэтому автор
        предполагает, что читатель:

        -  Имеет какое-то приложение (демон), которое должно работать с SELinux
        -  Просмотрел разницу между
           `DAC <https://en.wikipedia.org/wiki/Discretionary_access_control>`__,
           `MAC <https://en.wikipedia.org/wiki/Mandatory_access_control>`__ и
           `RBAC <https://en.wikipedia.org/wiki/Role-based_access_control>`__
        -  Знаком с администрированием Linux
        -  Что-то читал про SELinux и может расшифровать
           user\_u:user\_r:user\_home\_t:s0
        -  Имеет под рукой CentOS 7
        -  На котором установлены пакеты setools-console, policycoreutils-devel,
           selinux-policy-devel
        -  И включен SELinux в режиме permissive с политикой targeted или
           minimum

        Это все про вас? Тогда поехали!

        .. rubric:: Базовые типы
           :name: базовые-типы

        В качестве подопытного я взял
        `jnode <https://habrahabr.ru/post/208414/>`__ — достаточно типичное
        приложение, которое общается по сети, ходит в базу, читает конфиги,
        пишет свои данные и tmp-файлы и мониторит свое состояние (cpu, mem,
        disk).
        Создадим файл **jnode.te** (te = Type Enforcement)
        С чего нужно начать писать модуль? С описания базовых типов:
        ::

            policy_module(jnode, 1.0.0)
            # тип для процесса
            type jnode_t;
            # тип для исполняемого файла
            type jnode_exec_t;
            # тип для конфиг-файлов
            type jnode_conf_t;
            # тип для кэша ( аналог /var/cache/ )
            type jnode_cache_t;
            # тип для лог-файла
            type jnode_log_t;
            # тип для временных файлов
            type jnode_tmp_t;
            # тип для порта, который слушает jnode ( протокол binkp )
            type binkp_port_t;

        Почему так много? Потому, что это разные **категории** доступа для
        системы, например:

        -  **jnode\_exec\_t** будет исполняемым для всех и к нему будут
           применены правила перехода типов.
        -  **jnode\_t** будет типом процесса и именно на него будут вешаться все
           разрешения.
        -  **jnode\_conf\_t** будет r/o для приложения и r/w для администратора.
        -  **jnode\_cache\_t** будет append\_only для приоложения и r/w для
           администратора.
        -  **jnode\_log\_t** будет append\_only для приложения и r/w для
           syslog/logrotate/journald
        -  **jnode\_tmp\_t** будет r/w для приложения и denied для всех
           остальных.
        -  **binkp\_port\_t** нужен для управления портами, которые может
           слушать приложение.

        .. rubric:: Лирическое отступление
           :name: лирическое-отступление

        Теоретически, почти на этом месте ( добавив только правило перехода )
        можно прекратить писать модуль, скомпилировать его, установить в систему
        и промаркировать файловую систему при помощи chcon. После этого собрать
        логи при помощи утилиты **audit2allow** и получить несколько сотен
        абсолютно непонятных строк, которые будут что-то разрешать. Из них в
        дальнейшем получится модуль, который даже будет работать. Но понимания
        это вам не добавит, не так ли?
        Поэтому я предлагаю другой путь: читать заголовочные файлы и выбирать
        там то, что вам нужно. В **/usr/share/selinux/devel/include/** можно
        найти несколько сотен **.if**-файлов, в которых содержатся стандартные
        макросы базовой политики SELinux. К сожалению, вам придется использовать
        grep и cat самостоятельно, я лишь покажу несколько основных макросов и
        то, как они облегчают жизнь.

        .. rubric:: Макросы атрибутов
           :name: макросы-атрибутов

        Для облегчения жизни в SELinux существует понятие **attribute** — некого
        контейнера типов, (к) которому тоже можно назначать права доступа. Таким
        образов, добавив свой новый тип в тот или иной аттрибут мы автоматически
        выдаем ему стандартные права для этого атрибута. Чтоб не запоминать все
        эти атрибуты есть уже готовые макросы, которые размечают типы по
        атрибутам (часто по нескольким). Смотрите:
        ::

            #  это конфиг-файлы
            files_config_file(jnode_conf_t)
            # это какие-то файлы
            files_type(jnode_cache_t)
            # это лог-файлы
            logging_log_file(jnode_log_t)
            #  это временные файлы
            files_tmp_file(jnode_tmp_t)
            # а это порт
            corenet_port(binkp_port_t)

        .. rubric:: Макросы стандартных разрешений
           :name: макросы-стандартных-разрешений

        Когда типы определены, можно назначить стандартное поведения для
        приложения. Для этого тоже воспользуемся макросами, они достаточно легко
        находятся по ключевым словам и делают код человекочитаемым:
        ::

            # Макрос приложения: добавляет тип jnode_t в список приложений
            # и разрешает ему стартовать из типа  jnode_exec_t
            application_domain(jnode_t, jnode_exec_t)
            # Макрос демона: добавляет тип jnode_t в список демонов,
            # разрешает его запускать через systemd
            # и назначает переход: если systemd запустит файл с типом jnode_exec_t,
            # то процесс получит тип jnode_t
            init_daemon_domain(jnode_t, jnode_exec_t)
            # разрешает типу jnode_t исполнять стандартные бинарники ( /bin, /usr/bin )
            corecmd_exec_bin(jnode_t)
            # разрешает типу jnode_t подключать библиотеки
            libs_use_ld_so(jnode_t)
            # разрешает типу jnode_t читать состояние системы ( cpu, memory )
            kernel_read_system_state(jnode_t)
            # разрешает типу jnode_t писать в /tmp
            files_rw_generic_tmp_dir(jnode_t)
            # разрешает типу jnode_t читать конфиг сети ( /etc/resolv.conf итд )
            sysnet_read_config(jnode_t)
            # разрешает типу jnode_t получать случайные числа из /dev/(u)random
            dev_read_rand(jnode_t)
            # разрешает типу jnode_t получать аттрибуты файловой системы ( свободное место )
            fs_getattr_xattr_fs(jnode_t)
            # разрешает типу jnode_t делать dns resolve
            sysnet_dns_name_resolve(jnode_t)
            # разрешает типу jnode_t ходить в /var/log ( r/o )
            logging_search_logs(jnode_t)
            # назначает правило: логи, которые создает процесс jnode_t, 
            # будут иметь тип jnode_log_t
            logging_log_filetrans(jnode_t, jnode_log_t, file)
            # назначает правило: tmp-файлы, которые создает процесс jnode_t, 
            # будут иметь тип jnode_tmp_t
            files_poly_member_tmp(jnode_t, jnode_tmp_t)
            # разрешает jnode_t делать bind() на любой адрес
            corenet_tcp_bind_generic_node(jnode_t)
            # разрешает jnode_t общаться с postgresql по unix-сокету
            postgresql_stream_connect(jnode_t)
            # разрешает jnode_t общаться с postgresql по сети
            corenet_tcp_connect_postgresql_port(jnode_t)

        .. rubric:: Файл контекстов
           :name: файл-контекстов

        Теперь пришла пора привязать созданные типы к файловой системе. Создадим
        файл **jnode.fc** ( fc = File Context ).
        ::

            # исполняемый файл
            /opt/jnode/jnode.run        --  gen_context(system_u:object_r:jnode_exec_t)
            # все что r/o для сервиса назовем "конфигом"
            /opt/jnode(/.*)?            gen_context(system_u:object_r:jnode_conf_t)
            /opt/jnode/jar(/.*)         gen_context(system_u:object_r:jnode_conf_t)
            # и отдельно сами конфиги
            /opt/jnode/point/.*\.cfg        gen_context(system_u:object_r:jnode_conf_t)
            # сюда сервис сможет добавлять файлы ( но не удалять )
            /opt/jnode/fileechoes(/.*)?         gen_context(system_u:object_r:jnode_cache_t)
            /opt/jnode/point(/.*)?          gen_context(system_u:object_r:jnode_cache_t)
            # тут будут появляться и исчезать временные файлы и папки
            /opt/jnode/(inbound|temp)(/.*)?     gen_context(system_u:object_r:jnode_tmp_t)
            # а сюда будут писаться логи
            /var/log/jnode(/.*)? gen_context(system_u:object_r:jnode_log_t)

        .. rubric:: Сборка и установка
           :name: сборка-и-установка

        Создадим какую-нибудь папку и положим туда файлы **jnode.te** и
        **jnode.fc**. Перейдем туда и выполним сборку:
        ::

            [root@jnode jnode]# make -f /usr/share/selinux/devel/Makefile 
            Compiling targeted jnode module
            /usr/bin/checkmodule:  loading policy configuration from tmp/jnode.tmp
            /usr/bin/checkmodule:  policy configuration loaded
            /usr/bin/checkmodule:  writing binary representation (version 17) to tmp/jnode.mod
            Creating targeted jnode.pp policy package
            rm tmp/jnode.mod.fc tmp/jnode.mod

        Установим модуль командой **semodule -i jnode.pp** и включим его
        командой **semodule -e jnode**.
        Назначим номер порта для типа binkp\_port\_t: **semanage port -a -t
        binkp\_port\_t -p tcp 24554**.
        Теперь необходимо переназначить контексты в соответствии с файлом
        контекстов:
        **restoreconn -Rv /opt/jnode**. Запускаем сервис через systemctl и
        начинаем ждать.

        .. rubric:: Финальный audit2allow
           :name: финальный-audit2allow

        Через некоторое время (час, сутки — зависит от активности сервиса) можно
        выполнить команду **audit2allow -b -r -t jnode\_t** и посмотреть, что
        еще приложение просит помимо того, что ему уже было дано. Разрешений
        получится немного — может 10-15 строчек, причем не все из них ему
        реально нужны. Тут уже решать вам — что оставить, а что убрать. В
        «ненужной» части замените allow на dontaudit — это избавит от
        повторяющегося мусора в логах. Кстати, обновите версию модуля — это
        позволит ядру понять, что его нужно обновить.

        .. rubric:: setenforce 1
           :name: setenforce-1

        Когда **audit2allow** покажет «пусто» — это значит, что все работает по
        плану и можно включать enforcing. Поздравляю, вы нашли Силу.
        Распоряжайтесь ею с умом.

        .. rubric:: Полезные ссылки
           :name: полезные-ссылки

        - `selinuxproject.org/page/AVCRules <https://selinuxproject.org/page/AVCRules>`__ — описание allow-правил
        - `selinuxproject.org/page/TypeRules <https://selinuxproject.org/page/TypeRules>`__ — описание type\_ правил
        - `selinuxproject.org/page/ObjectClassesPerms <https://selinuxproject.org/page/ObjectClassesPerms>`__ — список классов и разрешений доступов
        - `danwalsh.livejournal.com <http://danwalsh.livejournal.com/>`__ — блог «отца» SELinux в RedHat и самой refpolicy

        .. |image1| image:: https://habrastorage.org/files/2cd/1b2/b38/2cd1b2b38bed4afe9873520219ade62b.png
           :width: 200px

Автор статьи также оставил интересный ответ, почему просто не использовать трюк с audit2allow:

        Q: А просто добавлять выхлоп audit2allow пока приложение не заведётся в модуль,
        а потом действительно денёк покурить и один раз повторить напоследок не проще? 

        A: Проще, но:
        - audit2allow не делает правила по переходам типов ( type_transition, type_member итд )
        - audit2allow делает две сотни правил вида allow service_t long_file_type_t:lnk_file { getattr };
        - если не включить типы в нужные атрибуты ( что audit2allow тоже не умеет делать ), то придется писать для каждого нового типа разрешения от всех других типов ( включая unconfined_t ), что еще в сотню раз увеличит размер модуля.
        - в итоге понять, к чему именно приложение попросило доступ — сложнее, чем погрепать два часа по include и найти все необходимые макросы. 
