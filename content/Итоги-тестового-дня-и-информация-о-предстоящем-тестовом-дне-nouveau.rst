.. title: Итоги тестового дня и информация о предстоящем тестовом дне Nouveau
.. slug: Итоги-тестового-дня-и-информация-о-предстоящем-тестовом-дне-nouveau
.. date: 2013-04-23 23:56:10
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


| Завтра (24.04.2013) продолжается цикл тестовых дней графической
  подсистемы в Fedora.

| Второй тестовый день пройдёт уже под знамёнами
  `Nouveau <http://ru.wikipedia.org/wiki/Nouveau>`__ графики.

  Подробности на `официальной
  странице <https://fedoraproject.org/wiki/Test_Day:2013-04-24_Nouveau>`__.

  Тестирование драйверов Radeon будет проводится завтра. Так же можно
  тестировать всю неделю.

| Даже если вы пользуетесь другим дистрибутивом - присоединяйтесь, т.к.
  решения проблем и улучшения в Fedora всегда передаются в апстрим и
  постепенно придут и в ваш дистрибутив.

| Ждём вас в
  `jabber-конференции <xmpp:fedora@conference.jabber.ru?join>`__ Russian
  Fedora. Если по каким-либо причинам вы не смогли и/или не хотите
  написать в конференцию, то вы можете связаться со мной
  `напрямую <http://russianfedora.pro/users/ignatenkobrain>`__. Я с
  удовольствием выслушаю и постараюсь помочь.

| Теперь расскажу немного о том, что было мной замечено интересного
  сегодня.


-  Тесты Wayland пропали со страницы в wiki, на что Matrix ответил, что
   планирует сделать отдельный тестовый день Wayland в июне, т.к. нужна
   подготовка

    ::

        Martix:  adamw: ignatenkobrain I may do special Rawhide's Wayland Test Day in June, when things settle in, perhaps including toolkits and SPICE
        Martix:  that a lot of new stuff and need preparation, packaging, etc

-  `Небольшой
   баг <https://bugzilla.redhat.com/show_bug.cgi?id=924708>`__ в GDM,
   который мешал нормальной работе SELinux, на который adamw быстро
   отреагировал

    ::

        adamw:  ignatenkobrain: huh, you're right, let me see if I can fix up those permissions
        adamw:  ignatenkobrain: no, it's fine, i know what the problem is, just trying to get it fixed
        adamw:  that file's permissions are at 0600, i'm finding someone to change them to 0644

-  На тестовом дне были замечены участники Russian Fedora
   `moonhawk <https://fedoraproject.org/wiki/User:M0nhawk>`__,
   `elemc <https://fedoraproject.org/wiki/User:Elemc>`__

Хочу поблагодарить тех, кто уже поучаствовал в тестовом дне и/или
собирается участвовать.

