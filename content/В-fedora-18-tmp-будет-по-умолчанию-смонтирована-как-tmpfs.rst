.. title: В Fedora 18, /tmp будет по умолчанию смонтирована, как tmpfs.
.. slug: В-fedora-18-tmp-будет-по-умолчанию-смонтирована-как-tmpfs
.. date: 2012-12-06 15:40:44
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`После полугода горячих
обсуждений </content/обсуждение-монтирования-tmp-как-tmpfs>`__ эта
"фича" была даже `поставлена на
удаление <https://fedorahosted.org/fesco/ticket/940>`__, но на последнем
собрании FESCo было `решено не менять изначального
решения <https://thread.gmane.org/gmane.linux.redhat.fedora.devel/171765/focus=171791>`__,
т.е. **/tmp будет по умолчанию смонтирована, как tmpfs**.
Lennart Poettering вновь сумел убедить нас в своей правоте - плюсы от
монтирования /tmp, как tmpfs, перевешивают минусы.

