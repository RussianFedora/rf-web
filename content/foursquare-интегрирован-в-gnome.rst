.. title: Foursquare интегрирован в GNOME!
.. slug: foursquare-интегрирован-в-gnome
.. date: 2015-01-06 22:59:28
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


| Наш коллега, `Damián
  Nohales <https://plus.google.com/+Dami%C3%A1nNohales>`__, писал во
  время GSoC 2014, что он работает над интеграцией GNOME Maps с
  социальными сетями, чтобы вы могли поделиться текущим местоположением
  в Facebook и Foursquare (и в Twitter если включили опцию в GNOME
  Maps).

| В `его последнем отчёте
  GSoC <http://blog.nohales.org/2014/05/gsoc-report-2-foursquare-in-gnome.html>`__
  он говорил, что хотел бы добавить эту фичу в GNOME 3.16, и как и
  хотелось, его код добавили несколько недель назад. Работа состоит из
  2-х частей:

-  **`GNOME Online Accounts (GOA) Foursquare
   provider <https://bugzilla.gnome.org/show_bug.cgi?id=729837>`__**:
   позволит пользователям добавить их аккаунт Foursquare в систему
   используя GNOME Control Center. Приложения и библиотеки смогут
   использовать этот аккаунт через API библиотеки GOA (которое
   использует внутри D-Bus для связи с демоном GOA)
-  **`Check-in в GNOME
   Maps <https://bugzilla.gnome.org/show_bug.cgi?id=731113>`__**:
   использует настроенные аккаунты Facebook и Foursquare для того, чтобы
   опубликовать текущее местоположение

| Если у вас включена поддержка геолокации в GNOME (включается в Control
  Center -> приватность) вы можете нажать на маркер, который обозначает
  текущее местоположение, затем нажать кнопку "Check in", пройти пару
  простых шагов (напр. выбрать заведение, написать комментарий), открыть
  страничку соц. сети и удостовериться что ваше местоположение было
  отправлено [STRIKEOUT:в нужные органы]. Damian надеется, что в будущем
  мы найдём более простые пути доступа к этой кнопке, т.к. сейчас она
  сильно спрятана (привет всем, кто любит скрытые фичи!).

.. raw:: html

   <div style="text-align:center">

|GNOME Maps Check-in screenshot|

.. raw:: html

   </div>

| 
| `Оригинал (содержит инструкцию по использованию аккаунта Foursquare в
  своём
  приложении) <http://blog.nohales.org/2015/01/gnome-gets-foursquare-integration.html>`__

.. |GNOME Maps Check-in screenshot| image:: http://ru.fedoracommunity.org/sites/default/files/pulse/Screenshot%20from%202015-01-06%2022_39_52.png
   :width: 100.0%
   :target: http://ru.fedoracommunity.org/sites/default/files/pulse/Screenshot%20from%202015-01-06%2022_39_52.png
