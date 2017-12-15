.. title: systemd 236
.. slug: systemd-236
.. date: 2017-12-15 15:40:44 UTC+03:00
.. tags: systemd, amazon, 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

`Официально вышел systemd 236
<https://lists.freedesktop.org/archives/systemd-devel/2017-December/039996.html>`_.

Среди нововведений можно отметить следующее:

* Поддержка конфигурационных файлов *tmpfiles.d* для пользователей (они должны
  размещаться в директории ``~/.config/user-tmpfiles.d/``).
* Теперь можно посмотреть все доступные варианты в загрузочном меню с помощью
  ``bootctl list``.
* Появилась возможность посмотреть, что будет сделано при операции с сервисом с
  помощью команды ``systemctl --dry-run``.

Ну и многое другое. Коллеги-аналитики уже анонимно обсуждают `новость на
OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=47749>`_.

Почти синхронно было объявлено, что недавно вышедшая `вторая версия
самодельного дистрибутива Amazon Linux переходит на systemd
<https://aws.amazon.com/about-aws/whats-new/2017/12/introducing-amazon-linux-2/>`_.
Новости от Amazon в последнее время `идут просто прекрасные
</posts/amazon-web-services-sobralis-perevodit-na-kvm/>`_.
