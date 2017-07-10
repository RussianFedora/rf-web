.. title: Репозитории
.. slug: repository
.. date: 2017-07-10 13:15:47 UTC+03:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Репозиторий Russian Fedora
==========================

В рамках проекта Russian Fedora ведётся репозиторий, который подразделяется на три части:

-  **branding** – пакеты, уже существующие в Fedora Everything, которые
   нужны для смены бренда c Fedora на RFRemix. Так как мы используем
   пакеты из различных сторонних репозиториев, то смена бренда является
   необходимым требованием;
-  **fixes** – пакеты, уже существующие в Fedora Everything. В данном
   репозитории содержатся либо более новые версии пакетов, либо
   исправления ошибок;
-  **free** – пакеты со свободными лицензиями, которых нет в Fedora
   Everything;
-  **nonfree** – пакеты с несвободными лицензиями, а также пакеты
   зависящие от других пакетов с несвободными лицензиями или находящихся
   в nonfree ветке RPM Fusion (например, faac).

**Внимание!** Обновление из репозитория Fixes меняет начертание шрифтов и исправляет некоторые проблемы, например,
 отображение кириллицы в некоторых музыкальных проигрывателях. Обновление из репозитория Branding превращает Fedora в
 RFRemix. Если вы не хотите этого делать, то не следует подключать эти репозитории.
   
Подключение
-----------

Структура репозитория идентична `RPM Fusion <http://rpmfusion.org/>`__. Также для многих программ потребуется `подключить репозиторий <http://rpmfusion.org/Configuration>`__ RPM Fusion).

Для подключения репозитория необходимо выполнить следующие команды:
  

Подключение Free и Nonfree
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   su -c 'dnf install --nogpgcheck http://mirror.yandex.ru/fedora/russianfedora/russianfedora/free/fedora/russianfedora-free-release-stable.noarch.rpm http://mirror.yandex.ru/fedora/russianfedora/russianfedora/nonfree/fedora/russianfedora-nonfree-release-stable.noarch.rpm'


Подключение Fixes
~~~~~~~~~~~~~~~~~

::

   su -c 'dnf install --nogpgcheck http://mirror.yandex.ru/fedora/russianfedora/russianfedora/fixes/fedora/russianfedora-fixes-release-stable.noarch.rpm'

Подключение Branding
~~~~~~~~~~~~~~~~~~~~

::

   su -c 'dnf install --nogpgcheck http://mirror.yandex.ru/fedora/russianfedora/russianfedora/branding/fedora/russianfedora-branding-release-stable.noarch.rpm'


Все пожелания по составу репозитория и сообщения об ошибках просьба направлять в `багтрекер
<http://redmine.russianfedora.pro/>`__.


Используемые ключи
------------------

Чтобы убедиться, что ключи в вашей системе совпадают с ключами,
приведёнными здесь, можно использовать GnuPG для проверки совпадения
отпечатков ключей. Например:
::

    $ gpg --quiet --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-11-primary 
    pub  4096R/D22E77F2 2009-01-19 Fedora (11) fedora@fedoraproject.org
    Key fingerprint = AEE4 0C04 E345 60A7 1F04  3D7C 1DC5 C758 D22E 77F2


**RPM-GPG-KEY-russianfedora-nonfree-fedora**
::

    pub  1024D/1453936D 2009-01-06 Russian Fedora repository (Fedora - nonfree) packages@russianfedora.ru
    Отпечаток ключа = B4A5 CA3E 6C4D 3E7B 2FE0  FCCD 5679 A69B 1453 936D

**RPM-GPG-KEY-russianfedora-free-fedora**
::

    pub  1024D/DBB6C70D 2009-01-06 Russian Fedora repository (Fedora - free) packages@russianfedora.ru
    Отпечаток ключа = 4B7B 8DBF D222 AFE5 A289  AEDC 8318 BE83 DBB6 C70D

**RPM-GPG-KEY-russianfedora-fixes-fedora**
::

    pub  1024D/4DD65180 2009-01-06 Russian Fedora repository (Fedora - fixes) packages@russianfedora.ru
    Отпечаток ключа = 3091 90CC 9967 017F 7574  64A4 371A 3B26 4DD6 5180

**RPM-GPG-KEY-russianfedora-branding-fedora**
::

    pub  2048R/C66AD8BC 2014-01-24 Russian Fedora repository (RFRemix - branding) packages@russianfedora.ru
    Отпечаток ключа = BAE1 E151 AA9A 97BC 92AB  B962 FEF8 A6D2 C66A D8BC


Зеркалирование
--------------

Репозиторий RFRemix занимет около 400 Гб, включая образы. Для зеркалирования нужно отправить письмо на адрес
atigro@ya.ru, чтобы получить персональный доступ. В письме необходимо указать:


- IP-адрес вашего сервера;
- его имя;
- пути доступа по HTTP, FTP, RSYNC (те что имеются);
- адрес для обратной связи.


После этого следует запустить нижеприведённый скрипт, изменив в нём переменную `$FEDORA_HOME`. Необходимо, чтобы
репозиторий russianfedora находился внутри зеркала Fedora, на одном уровне с каталогом linux, так как мы используем
ссылки на некоторые пакеты из основного дерева. Скрипт следует запускать по крону раз в минуту.

::

    #!/bin/sh
    if [ -f "/var/lock/russianfedoramirror" ]; then
        echo "Another copy of russianfedoramirror script already running";
        exit 0;
    else
        touch /var/lock/russianfedoramirror;
    fi

    LOGFILE="/var/log/russianfedora-$(date +%Y%m%d"-"%H%M%S).log"

    # Sync from. Your should mail your IP to atigro@ya.ru to
    # get private access to this host and module.
    HOST="pull-mirror.yandex.net"

    # Remote timestamp file
    TRACE=".mirror.yandex.ru"

    # Temp file
    TEMP_FILE=$(mktemp)

    # Set the home directory of fedora full mirror. RFRemix
    # will mirror into this directory as we have some links
    # on Fedora packages
    FEDORA_HOME=""

    rsync --timeout=30 $HOST::rfremix/russianfedora/$TRACE $TEMP_FILE

    MD5SUM_LOCAL=$(md5sum $FEDORA_HOME/russianfedora/$TRACE | awk '{print $1}' )
    MD5SUM_REMOTE=$(md5sum $TEMP_FILE | awk '{print $1}' )

    if [ "$MD5SUM_REMOTE" != "$MD5SUM_LOCAL" ]; then

        # Let $? will not be 0
        ls /dcbhjdcbhcbjhcf > /dev/null 2>&1

        while [ $? -ne 0 ]; do
            rsync --timeout=30 -avHP --delete-after --delay-updates \
                $HOST::rfremix/russianfedora/ \
                $FEDORA_HOME/russianfedora/ > $LOGFILE 2>&1
            sleep 2;
        done

        bzip2 -9 $LOGFILE
    fi

    rm -f /var/lock/russianfedoramirror
    rm -f $TEMP_FILE

Как добавить свой пакет в репозиторий?
--------------------------------------

Если вы **хотите**, чтобы в репозитории Russian Fedora присутствовал тот или иной пакет, и **готовы** поддерживать его,
то ознакомьтесь с `Регламентом добавления пакетов
<http://wiki.russianfedora.pro/index.php/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%B0_%D0%B2_%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_RussianFedora>`__.

Если у вас остались вопросы, вы можете задать их в jabber-конференции ::

    fedora-devel@conference.jabber.ru
