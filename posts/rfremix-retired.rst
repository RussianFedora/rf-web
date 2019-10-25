.. title: Разработка RFRemix прекращена
.. slug: rfremix-retired
.. date: 2019-10-25 10:00:00 UTC+02:00
.. tags: rfremix
.. category: RFRemix
.. link: 
.. backlinks: none
.. description: 
.. type: text
.. author: RussianFedora Team

Уважаемые пользователи RFRemix, а также репозиториев Russian Fedora!

Уведомляем вас, что разработка дистрибутива RFRemix, а также поддержка репозиториев Russian Fedora официально прекращены. Выход RFRemix 31 не состоится.

Статус проекта
===================

Проект выполнил свою задачу на 100%: все его наработки были приняты в официальные репозитории Fedora, а также RPM Fusion. Мейнтейнеры Russian Fedora теперь являются мейнтейнерами Fedora и RPM Fusion.

Поддержка пользователей и пакетов будет продолжена в рамках материнского проекта Fedora.

Что делать дальше?
=======================

Пользователям дистрибутива RFRemix необходимо преобразовать его в Fedora. Пользователям репозиториев Russian Fedora необходимо отключить их.

Преобразование RFRemix в Fedora
===================================

Замена пакетов с брендированием:::

    sudo dnf swap rfremix-release fedora-release --allowerasing
    sudo dnf swap rfremix-logos fedora-logos --allowerasing

Отключение репозиториев Russian Fedora:::

    sudo dnf remove "russianfedora*"

Синхронизация с эталоном:::

    sudo dnf distro-sync --allowerasing

Обновление до Fedora
=========================

После преобразования необходимо обновить дистрибутив до актуальной версии:::

    sudo dnf upgrade --refresh
    sudo dnf install dnf-plugin-system-upgrade
    sudo dnf system-upgrade download --releasever=$(($(rpm -E %fedora) + 1)) --setopt=module_platform_id=platform:f$(($(rpm -E %fedora) + 1))
    sudo dnf system-upgrade reboot

Помощь и техподдержка
=========================

Если у вас возникло какое-либо затруднение, вы всегда можете обратиться за помощью к другим участникам сообщества.

Чаты в Telegram:

  * `Russian Fedora <https://t.me/russianfedora>`_ - основной чат на русском языке.

Чаты в Matrix:

  * `#russianfedora:matrix.org <https://matrix.to/#/#russianfedora:matrix.org>`_ - основной чат на русском языке;
  * `#fedora-rpm-ru:matrix.org <https://matrix.to/#/#fedora-rpm-ru:matrix.org>`_ - технические вопросы по созданию RPM пакетов;
  * `#linux-ru-gaming:matrix.org <https://matrix.to/#/#linux-ru-gaming:matrix.org>`_ - обсуждения запуска и работы различных игр, а также клиента Steam.
