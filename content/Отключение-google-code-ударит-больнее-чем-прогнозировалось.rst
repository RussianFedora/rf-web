.. title: Отключение Google Code ударит больнее, чем прогнозировалось
.. slug: Отключение-google-code-ударит-больнее-чем-прогнозировалось
.. date: 2015-03-13 15:54:07
.. tags: google code, gitlab, gitorious
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Наш коллега, `Patrick Uiterwijk <https://github.com/puiterwijk>`__,
решил прикинуть, сколько вообще пакетов затронуты `закрытием Google
Code </content/google-code-официально-закрывается>`__ и `поглощением
GitLab B.V. хостинга
Gitorious <https://about.gitlab.com/2015/03/03/gitlab-acquires-gitorious/>`__?
Оказалось, что `довольно
много <https://thread.gmane.org/gmane.linux.redhat.fedora.devel/206007>`__.

Patrick просто погрепал по spec-файлам, так что итоговое число будет
больше, потому что есть пакеты, которые хостятся на Google Code или
Gitorious, но информация об этом в spec-файлах отсутствует. Навскидку,
например, `Vim <https://code.google.com/p/vim/>`__.

Кстати, наши упрямые коллеги, которые были не как все, уже переносят
проекты. Например, `Nikos Mavrogiannopoulos <https://github.com/nmav>`__
начал `перенос GnuTLS на
GitLab <https://thread.gmane.org/gmane.network.gnutls.general/3778>`__.

Ну хоть так, хотя, конечно, надо было бы на GitHub.

