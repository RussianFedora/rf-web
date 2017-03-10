.. title: Релиз Fedora 17 Beefy Miracle и RFRemix 17 
.. slug: Релиз-fedora-17-beefy-miracle-и-rfremix-17
.. date: 2012-05-29 18:23:58
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: mama-sun

**Это архивная статья**


| Итак, это наконец свершилось! Релиз откладывали 3 раза, но теперь он
  состоялся. В рассылках Fedora `официально
  объявлено <http://lists.fedoraproject.org/pipermail/announce/2012-May/003075.html>`__
  о выходе Fedora 17 Beefy Miracle. Сайт
  `fedoraproject.org <https://fedoraproject.org/>`__, а образы новой
  версии `доступны <https://fedoraproject.org/ru/get-fedora>`__ для
  скачивания. `Обновление с помощью
  yum <http://wiki.russianfedora.pro/index.php?title=Обновление_Fedora_%28или_RFRemix%29_с_помощью_yum>`__
  также возможно.

| **Наиболее заментные изменения в Fedora 17:**

-  возможность использования GNOME Shell без 3D-драйверов,
-  обновление версий программ (в том числе KDE 4.8, GNOME 3.4, GIMP 2.8,
   ядро Linux 3.3, PHP 5.4, GCC 4.7),
-  перенос исполняемых файлов и библиотек из корневого раздела в /usr,
-  использование по умолчанию динамического межсетевого экрана
   firewalld,
-  интеграция системы virt-sandbox для запуска приложений в
   изолированных окружениях,
-  включение в состав дистрибутива XAPI (Xen API) для управления
   гипервизором Xen,
-  задействование по умолчанию OpenJDK7,
-  обавление GUI-интерфейса GNOME Boxes для управления виртуальными
   машинами и организации удалённого доступа.


| 
| Одновременно с Fedora cостоялся релиз сборки RFRemix, базирующейся на
  репозиториях Fedora, RPM Fusion и Russian Fedora. RFRemix 17 основан
  на kernel 3.3.4, glibc 2.15, GNOME 3.4.1, KDE 4.8.3, XFCE 4.8, LXDE.

  «Из коробки» включены LibreOffice 3.5.3, Firefox 12, Chromium 21,
  мультимедийные кодеки, поддержка Adobe Flash и проприетарные драйвера
  к видеокартам NVIDIA. Описание основные нововведений Fedora 17
  доступны на wiki проекта.

| **Основные отличия RFRemix 17 от Fedora 17:**

-  Поддержка репозиториев RPM Fusion и Russian Fedora в установщике;
-  Наличие быстрых сценариев для установки в меню загрузчика;
-  Наличие сценариев установки различных рабочих столов (GNOME, KDE,
   XFCE, LXDE, Enlightment и минимальные установки GNOME и KDE);
-  Вынужденное увеличение размера live-образов (>700 мб), что позволило
   уместить на них больше пакетов (например, Libre Office);
-  Исправление проблемы установки пакетов с локализацией (kde-l10n,
   libreoffice-langpack и т. п.) в процессе установки;
-  Взможность выбора различных клавиатурных комбинаций для смены
   раскладок (для русского языка). По умолчанию используется Alt+Shift;
-  Дополнительный экран в Firstboot для быстрой настройки системы (выбор
   между KDM и GDM, включение некоторых полезных настроек в GNOME,
   включение комбинации Ctrl+Alt+Backspace), возможность выбора режима
   работы sudo;
-  Пакет Freetype собран с поддержкой subpixel rendering;
-  Словарь hunspell для русского языка содержит как русские, так и
   английские словари;
-  Система мониторинга Smolt отсылает в качестве названия дистрибутива
   не Fedora, а RFRemix.


| 
| **Новшества RFRemix 17 по сравнению с предыдущими версиями:**

-  Добавлена клавиатурная комбинация Caps для смены раскладки;
-  В состав live-образов добавлена утилита
   `grub-customizer <http://wiki.russianfedora.pro/index.php?title=Grub_Customizer>`__
   для конфигурации grub2, а так же пакеты fuse-encfs, tcplay и
   realcrypt для работы с шифрованием в Ubuntu;
-  В шрифт Cantarell добавлены символы кириллицы;
-  Из загрузчика убрана опция установки Live-образа на жёсткий диск, так
   как она не функционирует должным образом.


| 
| Для загрузки доступны установочные DVD образы, Live-образы с GNOME,
  KDE, LXDE, XFCE, образ сетевой установки, файлы разницы между Fedora
  17 и RFRemix 17. Загрузка возможна через зеркала, торренты и jigdo.


-  Установочные диски
   [`i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/17/RFRemix/i386/iso/>`__]
   [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/17/RFRemix/x86_64/iso/>`__]
-  Образы Live [
   `i686 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/17/Live/i686>`__
   ] [
   `x86\_64 <http://mirrors.rfremix.ru/mirrorlist?path=releases/RFRemix/17/Live/x86_64/>`__]
-  Торренты [
   `i386 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/17/RFRemix/i386/torrents/>`__]
   [
   `x86\_64 <http://mirror.yandex.ru/fedora/russianfedora/releases/RFRemix/17/RFRemix/x86_64/torrents/>`__
   ]

| 
| Кроме того, рады сообщить, что у нас появились три зеркала. Огромное
  спасибо администраторам за поддержку:

-  `mirror.neolabs.kz <http://mirror.neolabs.kz/fedora/russianfedora/>`__
-  `mirror.nl.as6453.net <http://mirror.nl.as6453.net/fedora/russianfedora/>`__
-  `ftp.byfly.by <http://ftp.byfly.by/pub/fedoraproject.org/russianfedora>`__

| 
| Следующая версия Fedora и RFRemix ожидается в ноябре 2012 года.

