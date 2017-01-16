.. title: Новые фичи Fedora 21
.. slug: Новые-фичи-fedora-21
.. date: 2014-03-28 12:29:34
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


| И опять новые фичи:

-  `Сделать ядро Linux более
   модульным <https://fedoraproject.org/wiki/Changes/Modular_Kernel_Packaging_for_Cloud>`__,
   чтоб не устанавливать (или легко удалять) ненужные модули при
   установке в виртуальные машины.

-  `Объявить \*-javadoc пакеты
   необязательными <https://fedoraproject.org/wiki/Changes/OptionalJavadocs>`__.

   С начала массовых пересборок для ARM и переходом на Java 8,
   выяснилось, что 80% ошибок сборки возникли во время создания
   javadoc-пакетов. Было решено сделать их необязательными, чтоб не
   блокировать сборку основных пакетов. Исправление ошибок в javadoc,
   это невысокоприоритетная задача, так как полно более важных дел, но
   когда-нибудь мы может быть возьмемся и за нее.

-  `Обновление Ruby on Rails до версии
   4.1 <https://fedoraproject.org/wiki/Changes/Ruby_on_Rails_4.1>`__
