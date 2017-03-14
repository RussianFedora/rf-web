.. title: Open CASCADE и Fedora - хэппиэнд!
.. slug: open-cascade-и-fedora-хэппиэнд
.. date: 2014-06-20 08:49:39
.. tags: legal, opencascade
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

После `перелицензирования Open CASCADE под свободной лицензией
</content/open-cascade-и-fedora>`__ сразу `продолжилась работа по включению его
в Fedora <https://bugzilla.redhat.com/458974>`__. Само собой, одна библиотека,
это не очень интересно, и заодно `продолжили работу по включению FreeCAD
<https://bugzilla.redhat.com/459125>`__. После снятия нетехнических ограничений
работа пошла быстро, и оба пакета уже доступны! Пробуйте:

::

        Dependencies resolved.

         
        ================================================================================
         Package                      Архитектура
                                             Версия                       Репозиторий
                                                                                  Размер
        ================================================================================
        Установка:
         freecad                      x86_64 0.13-7.fc20                  updates  14 M
         Coin2                        x86_64 2.5.0-19.fc20                fedora  1.9 M
         libspnav                     x86_64 0.2.2-6.fc20                 fedora   12 k
         python-collada               noarch 0.4-4.fc20                   fedora  168 k
         python-pivy                  x86_64 0.5.0-6.hg609.fc20           fedora  2.8 M
         SoQt                         x86_64 1.5.0-10.fc20                fedora  238 k
         xerces-c                     x86_64 3.1.1-5.fc20                 fedora  880 k
         zipios++                     x86_64 0.1.5.9-10.fc20              fedora   72 k
         OCE-modeling                 x86_64 0.15-3.fc20.1                updates  13 M
         freecad-data                 noarch 0.13-7.fc20                  updates  49 M
         OCE-ocaf                     x86_64 0.15-3.fc20.1                updates 1.7 M
         OCE-foundation               x86_64 0.15-3.fc20.1                updates 2.9 M
         python-dateutil              noarch 1.5-7.fc20                   fedora   85 k
         SIMVoleon                    x86_64 2.0.1-16.fc20                fedora  112 k
         OCE-visualization            x86_64 0.15-3.fc20.1                updates 1.5 M
         freeimage                    x86_64 3.10.0-16.fc20               fedora  224 k
         gl2ps                        x86_64 1.3.8-3.fc20                 fedora   54 k
         smesh                        x86_64 5.1.2.2-10.svn55.fc20        updates 1.0 M
         PyQt4                        x86_64 4.10.2-5.fc20                updates 3.0 M
         python-matplotlib            x86_64 1.3.1-3.fc20                 updates  30 M
         pyparsing                    noarch 2.0.1-1.fc20                 fedora   96 k
         stix-math-fonts              noarch 1.1.0-5.fc20                 fedora  286 k
         texlive-dvipng-bin           x86_64 3:svn30845.0-5.20131226_r32488.fc20
                                                                          updates  62 k
         python-matplotlib-data       noarch 1.3.1-3.fc20                 updates 2.1 M
         python-matplotlib-tk         x86_64 1.3.1-3.fc20                 updates  74 k
         stix-fonts                   noarch 1.1.0-5.fc20                 fedora  1.3 M
         python-matplotlib-data-fonts noarch 1.3.1-3.fc20                 updates 985 k
         qtwebkit                     x86_64 2.3.3-7.fc20                 updates  10 M
         qt-mobility                  x86_64 1.2.2-0.5.20120224git.fc20   fedora  3.0 M
         phonon                       x86_64 4.7.1-1.fc20                 updates 220 k
         kde-filesystem               x86_64 4-46.fc20                    fedora   48 k
         libqzeitgeist                x86_64 0.8.0-10.fc20                fedora   72 k
         texlive-dvipng               noarch 3:svn29821.1.14-5.fc20       updates  44 k
         numpy                        x86_64 1:1.8.0-4.fc20               updates 2.9 M
         python-nose                  noarch 1.3.0-1.fc20                 fedora  272 k
         phonon-backend-gstreamer     x86_64 2:4.7.1-1.fc20               updates 146 k
         
        Результат операции
        ================================================================================
        Установка   36 Packages
         
        Объем загрузки: 143 M
        Объем изменений: 364 M
        Продолжить? [y/N]: 
