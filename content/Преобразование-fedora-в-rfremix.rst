.. title: Преобразование Fedora в RFRemix
.. slug: Преобразование-fedora-в-rfremix
.. date: 2014-03-11 12:54:49
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Tigro

**Это архивная статья**


Вопросы о том, как магическим образом превратить Fedora в RFRemix
задавались довольно часто. И раньше тут было не мало проблем. По сути
одного подключения репозиториев RPM Fusion и Russian Fedora было
недостаточно, так как простое обновление системы разве что подправит
обновлённые и исправленные пакеты из репозитория russianfedora-fixes, а
кодеки и прочую "красоту" приходилось устанавливать вручную.


Однако теперь последние версии yum научились при обновлении системы
обрабатывать группы (которые берут из comps-файла репозитория) и
устанавливать пакеты (которых нет в системе), помеченные для
обязательной установки. Так что теперь просто подключаете пять
репозиториев (или по выбору): rpmfusion-free, rpmfusion-nonfree,
russianfedora-free, russianfedora-nonfree, russianfedora-fixes и отдаёте
команду ``yum update``. Далее пример для Fedora 20. После подключения
пакетов с настройками репозиториев Russian Fedora получаем следующее:

::

    $ sudo yum update
    Загружены модули: langpacks, refresh-packagekit
    Разрешение зависимостей
    ...
    Зависимости определены

    ==================================================================================================================================================================================
     Package                                           Архитектура             Версия                                              Репозиторий                                  Размер
    ==================================================================================================================================================================================
    Installing for group upgrade "GNOME":
     NetworkManager-openswan                           x86_64                  0.9.8.0-1.fc20                                      fedora                                        93 k
     NetworkManager-ssh-gnome                          x86_64                  0.9.1-0.5.20130706git6bf4649.fc20                   fedora                                        37 k
     clipit                                            x86_64                  1.4.2-5.fc20                                        fedora                                        73 k
     dconf-editor                                      x86_64                  0.18.0-2.fc20                                       fedora                                       127 k
     gconf-editor                                      x86_64                  3.0.1-6.fc20                                        fedora                                       1.2 M
     gnome-tweak-tool                                  noarch                  3.10.1-2.fc20                                       fedora                                       201 k
     gstreamer-ffmpeg                                  x86_64                  0.10.13-10.fc20                                     rpmfusion-free                               2.9 M
     gstreamer-plugins-ugly                            x86_64                  0.10.19-14.fc20                                     rpmfusion-free                               316 k
     gstreamer1-libav                                  x86_64                  1.2.1-1.fc20                                        rpmfusion-free                               2.8 M
     gstreamer1-plugins-bad-freeworld                  x86_64                  1.2.1-2.fc20                                        rpmfusion-free-updates                       157 k
     gstreamer1-plugins-ugly                           x86_64                  1.2.1-1.fc20                                        rpmfusion-free                               245 k
     mailnag                                           noarch                  0.5.2-4.fc20                                        fedora                                       135 k
    Installing for group upgrade "base-x":
     mesa-libGLU                                       x86_64                  9.0.0-4.fc20                                        updates                                      196 k
    Installing for group upgrade "Аудио и видео":
     paman                                             x86_64                  0.9.4-11.fc20                                       fedora                                        85 k
     paprefs                                           x86_64                  0.9.10-5.fc20                                       fedora                                        68 k
     pavucontrol                                       x86_64                  2.0-4.fc20                                          fedora                                       139 k
     pavumeter                                         x86_64                  0.9.3-11.fc20                                       fedora                                        34 k
    Installing for group upgrade "Веб-браузер Firefox":
     flash-plugin                                      x86_64                  7:11.2.202.310-1.R                                  russianfedora-nonfree                        5.5 M
    Installing for group upgrade "Основные":
     workaround-cyrillic-console                       noarch                  1.0-5.fc20.R                                        russianfedora-free                           4.1 k
    Installing for group upgrade "Стандартные":
     gpm                                               x86_64                  1.20.7-3.fc20                                       fedora                                       183 k
     mc                                                x86_64                  1:4.8.11-1.fc20                                     updates                                      1.8 M
     p7zip                                             x86_64                  9.20.1-6.fc20                                       fedora                                       616 k
    Installing for group upgrade "Шрифты":
     ubuntu-font-family                                noarch                  5:0.69-2.R                                          russianfedora-free                           526 k
     ucs-miscfixed-fonts                               noarch                  0.3-11.fc20                                         fedora                                       466 k
    Установка:
     aspell-ru                                         x86_64                  50:0.99f7-12.fc20                                   fedora                                       2.0 M
     rfremix-logos                                     x86_64                  21.0.1-1.fc20.R                                     russianfedora-fixes                          9.6 M
         замена  fedora-logos.x86_64 21.0.1-1.fc20
     rfremix-release                                   noarch                  2:20-1.R                                            russianfedora-fixes                           37 k
         замена  fedora-release.noarch 20-1
    Обновление:
     anaconda                                          x86_64                  20.25.16-1.fc20.R                                   russianfedora-fixes-updates                  2.1 M
     anaconda-widgets                                  x86_64                  20.25.16-1.fc20.R                                   russianfedora-fixes-updates                  701 k
    ...
     xdotool                                           x86_64                  1:2.20110530.1-7.fc20                               fedora                                        46 k

    Итого за операцию
    ==================================================================================================================================================================================
    Установить  27 пакетов (+63 зависимых)
    Обновить    24 пакета

    Объем загрузки: 61 M
    Is this ok [y/d/N]: 

Как видно на примере yum, обновляя группу, хочет доставить некоторые
новые пакеты в систему. "Возмущённые читатели" даже прислали по этому
поводу `баг <http://redmine.russianfedora.pro/issues/1297>`__. В принципе
тут нужно подумать, как лучше избегать установку кому-то не нужных
компонентов, но с другой стороны RFRemix для этого и придумывался.


Благодаря этой удачной особенности yum у нас появилось несколько путей
развития RFRemix'а. Но о них в следующей статье.

