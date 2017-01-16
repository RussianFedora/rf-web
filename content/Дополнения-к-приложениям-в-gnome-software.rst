.. title: Дополнения к приложениям в GNOME Software
.. slug: Дополнения-к-приложениям-в-gnome-software
.. date: 2014-06-14 14:13:47
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


| После того момента, как мы показали миру GNOME Software Center, люди
  захотели `добавить в него немного
  функционала <https://bugzilla.gnome.org/show_bug.cgi?id=709476>`__.

  Одна из вещей, которая была очень важна для разработчиков Eclipse -
  способ установки расширений к основной программе, что показалось нам
  отличной идеей. Мы хотели сделать это настолько универсальным, чтобы
  её могли использовать другие проекты, как gedit и другие модульные
  приложения в составе GNOME и KDE. Мы сознательно не предоставляем
  такую функциональность для Chrome или Firefox, поскольку эти
  приложения сделают намного лучше это задание, чем GNOME Software.

| Недавно Ричард Хьюз (Richard Hughes) добавил специальный тип
  компонентов в
  `AppStream <http://www.freedesktop.org/software/appstream/docs/>`__ -
  дополнения.

| AppStream - XML стандарт, созданный для удобства распространения
  приложений через центры приложений в разных дистрибутивах. На данный
  момент уже активно используется в дистрибутивах: Fedora, openSUSE. В
  ближайшее время так же будет использоваться в ArchLinux и Debian.

| Создание специального metainfo.xml для каждого плагина позволит
  пользователю устанавливать доп. компоненты. Плагины для текстовых
  редакторов, мультимедиа кодеки и пр.

| Как выглядит обычный metainfo.xml, заметки и как его использовать
  можно посмотреть в `блоге
  Ричарда <http://blogs.gnome.org/hughsie/2014/06/11/application-addons-in-gnome-software/>`__
| Kalev Lember в настоящее время работает над интерфейсом плагинов в
  GNOME Software, Richard Hughes только завершил поддержку metainfo.xml
  в `обработчике
  AppStream <https://github.com/hughsie/createrepo_as>`__, так что не
  стоит ожидать видимость новых функций до GNOME 3.14 и Fedora 21.

| Рекомендуем использовать `утилиту для проверки AppStream
  файлов <https://github.com/hughsie/appstream-glib>`__ - appstream-util
  (входит в состав libappstream-glib). К сожалению в выпущеной версии
  0.1.7 отсутствуют некоторые возможности, которые вы, наверное, хотели
  бы использовать. Среди них:

-  Проверка metainfo.xml.in файлов (используется при локализации) - `fix
   #1 <https://github.com/hughsie/appstream-glib/commit/255a5b600f3b9d6c9b7b18a5a0251114b86cfe3d>`__,
   `bug #2 <https://github.com/hughsie/appstream-glib/issues/2>`__, `fix
   #2 <https://github.com/hughsie/appstream-glib/commit/383d8b04164c878cdc3cddd465de13eff976618e>`__;
-  При проверке одновременно множества файлов при неудачной проверке
   одного из файлов программа завершает свою работу -
   `bug <https://github.com/hughsie/appstream-glib/issues/1>`__,
   `fix <https://github.com/hughsie/appstream-glib/commit/e24fbe5510cce422c17460ce2f2088a0331cba4f>`__;
-  Установка AppData и MetaInfo файлов (можно использовать во время
   тестирования) -
   `fix <https://github.com/hughsie/appstream-glib/commit/c8da94a61228c9931a4f41cd20b63baa2bf95f93>`__;
-  Ну и куда же без автодополнения в Bash - `fix
   #1 <https://github.com/hughsie/appstream-glib/commit/9a2c7a5fec10847b57ba598bc6ca4db4a14f3928>`__,
   `fix
   #2 <https://github.com/hughsie/appstream-glib/commit/f7236af615acddadb6aa6d2d602259081d5188f1>`__.


| 
| Ричард написал статью в своём блоге о том, как разработчики могут
  интегрировать свои дополнения с KDE и GNOME центрами приложений. Мы с
  Ричардом с удовольствием поможем на данном этапе. Если у вас есть свои
  пакеты в своих репозиториях, то они не появятся автоматически в
  центрах приложений. Вы должны специальным образом обработать их.

  Пример того, как можно это сделать - `в нашей
  рассылке <https://lists.fedoraproject.org/pipermail/ru-users/2014-June/000053.html>`__.

  Надеюсь, в скором времени мы внедрим все эти новые технологии у нас,
  т.к. мы стараемся максимально повторить процессы Fedora Project.

| **Наши контактные данные**:
| **Richard Hughes**:

-  **IRC**: hughsie on freenode and gimpnet
-  **Email**: richard AT hughsie DOT com

**Igor Gnatenko**

-  **IRC**: ignatenkobrain on freenode and gimpnet
-  **Email/Jabber**: `RussianFedora
   профиль <http://ru.fedoracommunity.org/users/ignatenkobrain>`__

| 
| Мы уже написали много патчей, отправили багов:
| **Evolution RSS**: https://bugzilla.gnome.org/show\_bug.cgi?id=731553
| **GEedit plugins**:
  https://bugzilla.gnome.org/show\_bug.cgi?id=731632,
  https://git.gnome.org/browse/gedit-code-assistance/commit/?id=789e7b9f5569f5b7067c60c7c1f205b52265a9f5
| **Eclipse plugins**:
  https://bugs.eclipse.org/bugs/show\_bug.cgi?id=437245
| **Claws-mail plugins**:
  http://www.thewildbeast.co.uk/claws-mail/bugzilla/show\_bug.cgi?id=3210
| Итого на сегодняшний момент написано:

-  **Richard Hughes**: **1** плагин (metainfo), **9** багрепортов;
-  **Igor Gnatenko**: **45** плагинов (metainfo), **3** багрепорта.


| 
| **Источник**:
  http://blogs.gnome.org/hughsie/2014/06/11/application-addons-in-gnome-software/
