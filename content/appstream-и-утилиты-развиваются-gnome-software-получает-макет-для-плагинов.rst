.. title: AppStream и утилиты развиваются. GNOME Software получает макет для плагинов.
.. slug: appstream-и-утилиты-развиваются-gnome-software-получает-макет-для-плагинов
.. date: 2014-06-18 02:20:15
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


| В продолжение `предыдущей новости про новый стандарт AppStream и GNOME
  Software </content/%D0%94%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BA-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%D0%BC-%D0%B2-gnome-software>`__.

| **Краткое содержание**:

-  createrepo\_as сливается с проектом appstream-glib
-  createrepo\_as переименовывается в appstream-builder
-  appstream-builder получает поддержку автодополнения в bash
-  appstream-builder научился работать с пакетами, в которых
   одновременно содержатся AppData и MetaInfo
-  GNOME Software получил макеты для дополнений к приложениям

::

    12∶34
    hughsie: ignatenkobrain_l, hey
             i'm thinking of perhaps merging createrepo_as with appstream-glib
             and just shipping an appstream-glib-builder subpackage
             this means we can easily get the tools onto the various buildservers without an extra package to review/install/etc
             it also means when the appstream spec changes i only have to do the change in one project...
             i wanted to know what you thought

| После недолгих обсуждений было принято решение о слиянии
  createrepo\_as и appstream\_glib.

| Утилита для генерации AppStream мета-данных
  `createrepo\_as <https://github.com/hughsie/createrepo_as>`__ была
  `перенесена <https://github.com/hughsie/appstream-glib/commit/1284b3fa0addf21070c6d9ce697623a04862cdde>`__
  в проект
  `appstream-glib <https://github.com/hughsie/appstream-glib>`__ и
  переименована в appstream-builder. После этого appstream-builder
  `получил поддержку автодополнения в
  bash <https://github.com/hughsie/appstream-glib/commit/ce8b3fe287177587ba2c348c3c294a09714b3867>`__.

| В Fedora evince разделён на несколько пакетов - evince, evince-libs,
  evince-dvi, evince-djvu. Я отправил `патч для добавления в них
  MetaInfo <https://bugzilla.gnome.org/show_bug.cgi?id=731708>`__. Так
  же мы `получили сообщение от команды
  Xfce <https://mail.xfce.org/pipermail/xfce4-dev/2014-June/030766.html>`__
  о том, что у них плагины поставляются вместе с приложениями. И тут мы
  подумали, а ведь есть же такие проекты, которые поставляют плагины
  вместе с собой. Например,
  `parole <http://git.xfce.org/apps/parole/tree/src/plugins>`__,
  `gedit <https://git.gnome.org/browse/gedit/tree/plugins>`__,
  `evince <https://git.gnome.org/browse/evince/tree/backend>`__. Что
  будет, если в одном пакете будет одновременно поставляться и AppData,
  и MetaInfo? А будет всё очень просто. В центрах приложений при
  открытии такого приложения будут отображаться плагины, которые
  установлины и их можно будет удалить. Конечно же с самой программой!
  Ричард предложил следующее:

::

    19:40
    hughsie: kalev, ignatenkobrain_ I'm thinking of suppressing the metainfo file from the AppStream XML if the metainfo file has the same package name as its parent -- sane?

| После недолгих раздумий мы решили так и сделать.

| `Теперь <https://github.com/hughsie/appstream-glib/commit/162fcc4aecda03a8e598b8deb73ddec473d7cb70>`__
  appstream-builder, если находит в одном пакете (rpm, deb, etc.)
  одновременно AppData и MetaInfo - он просто игнорирует MetaInfo. Т.е.
  в центрах приложений мы не будем видеть этот плагин (который обозначен
  в metainfo).

| Теперь немного о GNOME Software.

| `Allan Day <https://wiki.gnome.org/AllanDay>`__ `добавил макет для
  дополнений к приложениям в GNOME
  Software <https://github.com/gnome-design-team/gnome-mockups/commit/4a5be526de97668529f2b00f16a4e6c20a268e2c>`__.

| |GNOME Software App addons mockup|
| Как вы видите сверху - при установке приложения можно будет отметить,
  какие дополнительные плагины нужно установить, снизу - макет того, как
  можно будет устанавливать плагины для уже установленного приложения. К
  сожалению, пока потыкать кнопки нельзя. `Kalev
  Lember <http://fedoraproject.org/wiki/User:Kalev>`__ работает над
  этим.

| Команда `GTG <http://gtgnome.net/>`__ в личной переписке согласилась
  принять патчи для добавления MetaInfo к их плагинам.


.. |GNOME Software App addons mockup| image:: https://raw.githubusercontent.com/gnome-design-team/gnome-mockups/4a5be526de97668529f2b00f16a4e6c20a268e2c/software/version2/software-app-addons.png
   :width: 640px
   :height: 480px
