.. title: Разработка SELinux-модуля для пользователя
.. slug: razrabotka-selinux-modulia-dlia-polzovatelia
.. date: 2017-02-24 20:01:04 UTC+03:00
.. tags: HOWTO, selinux, перепост
.. category: начинающим
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

На Хабрахабре `продолжили <https://habrahabr.ru/post/322476/>`_ публикацию статей, посвященную настройке SELinux:

        .. rubric:: Разработка SELinux-модуля для пользователя tutorial
           :name: разработка-selinux-модуля-для-пользователя-tutorial
           :class: post__title

        .. rubric:: Это вторая статья из цикла
           :name: это-вторая-статья-из-цикла

        |image1|
        
        Сегодня мы поговорим о SELinux-пользователях, их создании,
        привязке, правам и другим вещам.
        Зачем это делать? Есть много причин. Для меня главной причиной было
        выдать доступ для техподдержки для рутинных операций (таких как ребут,
        чистка логов, диагностика итд), но без доступа к критичным данным и
        изменению системных функций.

        .. rubric:: Предположения
           :name: предположения

        В тексте будет содержаться много технической информации, поэтому автор
        предполагает, что читатель:

        -  Прочитал `прошлую статью <https://habrahabr.ru/post/320100/>`__
        -  Имеет под рукой CentOS 7
        -  На котором установлены пакеты setools-console, policycoreutils-devel,
           selinux-policy-devel, policycoreutils-newrole
        -  И включен SELinux в режиме enforcing с политикой targeted или minimum

        Это все про вас? Тогда поехали!

        .. rubric:: Пользователи и роли
           :name: пользователи-и-роли

        Основное назначение пользователей — хранить список ролей, которые он
        может использовать.
        Пользователи по-умолчанию уже представлены в политике targeted или
        minimum, можете посмотреть командой **semanage user -l**.

        |image2|

        Как известно из прошлой статьи, именно **роли** являются контейнерами
        для **типов**, а именно на типы вешаются все необходимые правила.
        Таким образом, пользователь просто расширяет это дерево, создавая больше
        возможных вариантов. Обратите внимание: если у пользователя есть та или
        иная роль, он может **самостоятельно** переключиться в нее, используя
        команду **newrole**. Таким образом, разрешив пользователю роль sysadm\_r
        или unconfined\_r, вы автоматически даете ему неограниченные права на
        систему.

        .. rubric:: Пользователи и пользователи
           :name: пользователи-и-пользователи

        Между Unix-пользователем (тем, который имеет UID) и
        SELinux-пользователем (тем, который имеет контекст) есть тонкая связь,
        которой можно управлять при помощи команды **semanage login**. Связь это
        односторонняя: id -Z user1 вам ничего не покажет. Специальный
        пользователь **\_\_default\_\_** обозначает всех пользователей, не
        перечисленных в системе.

        |image3|

        .. rubric:: Создание пользователя (простой способ)
           :name: создание-пользователя-простой-способ

        Самый простой способ создать пользователя из готовых ролей —
        использовать **semanage user -a**.
        Предположим, нам нужен просто новый пользователь с дополнительным
        набором ролей:

        |image4|

        Таким образом мы получили пользователя, который имеет возможность
        админить web. Теперь мы можем задать для него пользователя:

        |image5|

        .. rubric:: Контекст
           :name: контекст

        Об этом мало где пишут, но мало просто создать пользователя. Если его
        контекст отличается от **default\_context**, для него необходимо
        настроить файл контекстов. Подробнее см. `man
        user\_contexts <http://man7.org/linux/man-pages/man5/user_contexts.5.html>`__.
        Настроим файл и для webadm\_u:

        |image6|

        .. rubric:: Проверка
           :name: проверка

        Зайдем под пользователем webadm:

        |image7|

        Сменим uid на 0 и попробуем что-нибудь «сломать»:

        |image8|

        Сменим роль на webadm\_r и попробуем теперь:

        |image9|

        Что и требовалось доказать — мы сделали админа, который может админить
        только веб. К сожалению, количество ролей «по-умолчанию» сильно
        ограничено. Список можно посмотреть
        `тут <https://selinuxproject.org/page/RefpolicyBasicRoleCreation>`__.

        .. rubric:: Создание пользователя (правильный способ)
           :name: создание-пользователя-правильный-способ

        Давайте сделаем все тоже самое, но например для администрирования
        **docker**, причем напишем его с нуля.
        Модуль будет очень простой. Что нам нужно разрешить?

        #. Вход по ssh
        #. Доступ к sudo (UNIX-права никто не отменял)\*
        #. Администрирование файлов, папок и сервиса докера
        #. Исполнение бинарников докера (docker, runcon)
        #. Коннект к сокету докера

        Прим.: группа docker на последней версии CentOS7 не имеет доступа к
        /run/docker.sock по-умолчанию.

        Напишем модуль и контекст-файл:
        ::

            # новый модуль
            policy_module(dockeradm, 1.0.3)
            # объявляем новую роль
            role dockeradm_r;
            # стандартный шаблон для НЕ-админа
            userdom_unpriv_user_template(dockeradm)
            # разрешаем dac_override
            allow dockeradm_t self:capability { dac_override dac_read_search };
            # разрешаем sudo
            sudo_role_template(dockeradm, dockeradm_r, dockeradm_t)
            # разрешаем управлять файлами и папками контейнеров
            container_admin(dockeradm_t)
            # разрешаем исполнять исполняемые файлы контейнера
            container_runtime_exec(dockeradm_t)
            # разрешаем коннект к сокетам контейнера
            container_stream_connect(dockeradm_t)
            # макрос gen_user создает пользователя так-же, как semanage user -a
            # он всегда должен быть в самом конце файла
            gen_user(dockeradm_u, dockeradm, dockeradm_r, s0, s0)

        Скомпилируем и установим модуль:

        |image10|

        Настроим пользователя и контекст:

        |image11|

        Проверим, что нас пускает в систему:

        |image12|

        Проверим наши права:

        |image13|

        Как говорит Apache, **It works!**

        .. rubric:: Подведение итогов
           :name: подведение-итогов

        Создание SELinux-пользователей — важный шаг к созданию полноценного
        рабочего окружения, в котором каждый сотрудник занимается своим делом и
        при этом не мешает другим. Будь то хостинг-провайдер, студия разработки
        или банк, всегда есть ситуации, когда разделение доступа необходимо.
        Включайте SELinux и наслаждайтесь :)

        -  `selinux <https://habrahabr.ru/search/?q=%5Bselinux%5D&target_type=posts>`__,
        -  `setenforce
           1 <https://habrahabr.ru/search/?q=%5Bsetenforce%201%5D&target_type=posts>`__,
        -  `linux <https://habrahabr.ru/search/?q=%5Blinux%5D&target_type=posts>`__,
        -  `centos <https://habrahabr.ru/search/?q=%5Bcentos%5D&target_type=posts>`__,
        -  `policy\_module <https://habrahabr.ru/search/?q=%5Bpolicy_module%5D&target_type=posts>`__,
        -  `user <https://habrahabr.ru/search/?q=%5Buser%5D&target_type=posts>`__


.. |image1| image:: https://habrastorage.org/files/829/d07/444/829d074443b74f6a95df53a53eebfb7b.png
   :align: center
   :width: 200px
.. |image2| image:: https://habrastorage.org/files/64c/20c/918/64c20c918d5148c3953d88379bdad32e.png
   :align: center
.. |image3| image:: https://habrastorage.org/files/ac9/f41/176/ac9f41176ddc48c0a13ab559a4c78845.png
   :align: center
.. |image4| image:: https://habrastorage.org/files/8a9/6e0/bea/8a96e0beab6e4e36b274e71e9b50ebf0.png
   :align: center
.. |image5| image:: https://habrastorage.org/files/8cc/2bb/04e/8cc2bb04e9464fc0bc9d981770c4a01c.png
   :align: center
.. |image6| image:: https://habrastorage.org/files/911/3a1/a48/9113a1a48ef9422e9aaa75f60846fad8.png
   :align: center
.. |image7| image:: https://habrastorage.org/files/afd/8ed/592/afd8ed5926724579ada8ee12358e47cd.png
   :align: center
.. |image8| image:: https://habrastorage.org/files/055/362/fb1/055362fb184e413bb6a26d2bef7e9cb7.png
   :align: center
.. |image9| image:: https://habrastorage.org/files/a92/44f/dea/a9244fdeac2147519701918460b41127.png
   :align: center
.. |image10| image:: https://habrastorage.org/files/379/f4d/8a6/379f4d8a6bf4443da05519df94b93422.png
   :align: center
.. |image11| image:: https://habrastorage.org/files/5c4/9f6/41a/5c49f641a61c45a19a767f382d5f7650.png
   :align: center
.. |image12| image:: https://habrastorage.org/files/52c/35a/ddd/52c35addd0194e2589981ac40313b77b.png
   :align: center
.. |image13| image:: https://habrastorage.org/files/559/d30/6a4/559d306a4b8248ad801a7e79e57142e2.png
   :align: center
