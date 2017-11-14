.. title: Вышла Fedora 27
.. slug: vyshla-fedora-27
.. date: 2017-11-14 17:46:32 UTC+03:00
.. tags: fedora, rfremix
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Релиз Fedora 27 выпущен официально. RFRemix 27, адаптированный для русскоговорящих пользователей, однако, задержится на несколько дней.

`Список изменений <https://fedoramagazine.org/announcing-fedora-27/>`_.

Загрузить Fedora 27 можно `здесь <https://getfedora.org/>`_.

`Инструкция по созданию загрузочной USB-флешки <https://www.easycoding.org/?p=1081>`_.

`Инструкция по установке драйверов NVIDIA <https://www.easycoding.org/?p=1036>`_.

Если вы пользователь более ранних релизов Fedora, то должны обновиться штатно посредством dnf:

1. sudo dnf upgrade --refresh
2. sudo dnf install dnf-plugin-system-upgrade
3. sudo dnf system-upgrade download --releasever=27
4. sudo dnf system-upgrade reboot

Репозитории RPMFusion и Russian Fedora уже полностью поддерживают Fedora 27.
