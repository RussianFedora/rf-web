.. title: Сегодня тестовый день SSD Cache (bcache)
.. slug: Сегодня-тестовый-день-ssd-cache-bcache
.. date: 2013-10-13 13:05:08
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: i.gnatenko.brain

**Это архивная статья**


| Сегодня, в рамках `тестовых дней Fedora
  20 <https://fedoraproject.org/wiki/QA/Fedora_20_test_days>`__ будет
  проходить тестовый день посвящённый тестированию SSD Cache. А если
  точнне `bcache <http://bcache.evilpiepirate.org/>`__, т.к. dm-cache
  находится в очень плохом состоянии.

| Сегодня, после 12:00 PST (23:00 MSK) будет присутствовать автор и
  главный разработчик `bcache <http://bcache.evilpiepirate.org/>`__
  (Kent Overstreet).

| На сегодняшний день (официально) bcache есть в 2х дистрибутивах -
  Ubuntu (PPA), Fedora (основные репозитории). В рамках Fedora Project
  мы написали правильные udev правила, правильно внедрили в dracut и
  сделали очень много другой работы. Bcache - self-contained фича Fedora
  20, что означает через установщик федоры вы не можете использовать
  bcache. К F21 это уже будет wide-change, что означает интеграцию с
  установщиком.

| Не переживайте, пользователи \`distroname\`! В ближайшем будующем,
  конечно же, они появятся и в вашем \`distroname\`, поэтому не
  стесняйтесь приходить и тестировать. Все наши наработки будут переданы
  в апстрим!
| У нас подготовлены 4+ тесткейса:

-  `/home on bcache (no
   LVM) <https://fedoraproject.org/wiki/QA:Testcase_bcache-tools_home_on_bcache_(no_LVM)>`__
-  `/ on bcache (no
   LVM) <https://fedoraproject.org/wiki/QA:Testcase_bcache-tools_root_on_bcache_(no_LVM)>`__
-  `/home on bcache
   (LVM) <https://fedoraproject.org/wiki/QA:Testcase_bcache-tools_home_on_bcache_(LVM)>`__
-  `/ on bcache
   (LVM) <https://fedoraproject.org/wiki/QA:Testcase_bcache-tools_root_on_bcache_(LVM)>`__
-  `mock on bcache (no
   LVM) <https://fedoraproject.org/wiki/QA:Testcase_bcache-tools_mock_on_bcache_(LVM)>`__

| 
| Последний тесткейс даёт интересные возможности для билдсерверов по
  типу koji. Т.к. частоиспользуемые пакеты для сборки будут кешироваться
  на SSD, что должно дать неплохой прирост к производительности.

| После тестирования нужно заполнить
  `таблицу <https://fedoraproject.org/wiki/Test_Day:2013-10-13_SSD_Cache#Test_Results>`__.

| `Подробнее <https://fedoraproject.org/wiki/Test_Day:2013-10-13_SSD_Cache>`__
| Все вопросы можно (и нужно) задавать на #fedora-test-day on Freenode
  мне (ignatenkobrain) и Rolf Fokkens (rolffokkens).

