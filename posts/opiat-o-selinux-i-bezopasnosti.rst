.. title: Опять о SELinux и безопасности
.. slug: opiat-o-selinux-i-bezopasnosti
.. date: 2017-01-19 19:12:22 UTC+03:00
.. tags: security, selinux, systemd, docker, containers, facebook, coreos, redhat
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov


В который раз `SELinux успешно блокировал очередную уязвимость <http://rhelblog.redhat.com/2017/01/13/selinux-mitigates-container-vulnerability/>`_. Вы же не настолько наивны, что его выключаете, следуя протухшим хаутушкам и советам самозваных форумных линукс-гуру? Если выключаете, то прежде, чем читать дальше, немедленно его включите обратно. В этот раз `уязвимость была в Docker <https://coreos.com/blog/cve-2016-9962.html>`_, в котором вообще `проблем с безопасностью хватает </content/docker-и-selinux/>`_, и если б не наши коллеги, то было бы еще больше.

Забавно, что когда наши коллеги указали, что стандартная инсталляция RHEL или Fedora, со включенным SELinux неуязвима для эксплойта, то у представителей Docker Inc., как это говорится, `бомбануло <https://news.ycombinator.com/item?id=13399271>`_. Неясно, связана ли такая враждебность с тем, что `Red Hat зарабатывает на Docker больше, чем Docker Inc. <http://www.techrepublic.com/article/why-red-hat-makes-more-money-on-docker-than-docker-does/>`_? Скорее всего, нет. Просто так злятся.

Вообще, с контейнерами (т.е. `просто <http://www.slideshare.net/jpetazzo/anatomy-of-a-container-namespaces-cgroups-some-filesystem-magic-linuxcon>`_ `cgroups + namespaces <https://jvns.ca/blog/2016/10/10/what-even-is-a-container/>`_) надо быть осторожными. Мы уже предупреждали вас, что `контейнеры не ограничивают приложения </content/Безопасность-docker-будущее/>`_ так, как бы это хотелось. Наши коллеги из CoreOS, например, в довесок к SELinux `добавили <https://coreos.com/blog/rkt-detect-privilege-escalation.html>`_ специальный функционал в свой конкурирующий с Docker продукт, rkt. Они даже `сделали безопасность и изоляцию основными отличительными чертами нового релиза rkt 1.14 <https://coreos.com/blog/rkt-container-engine-v1-14-0.html>`_. 

Мы идем своим путем, выстраивая систему безопасности с самого низа до верха. Внизу находится загрузчик с UEFI и SecureBoot, который позволяет, например, `блокировать ядро от изменения из userspace <http://lkml.iu.edu/hypermail/linux/kernel/1611.2/00678.html>`_. В самом ядре, в дополнение в namespaces и cgroups, наши колеги постоянно добавляют новый функционал. Недавно `Daniel
Mack <https://www.ohloh.net/accounts/zonque>`_ предложил `механизм фильтрации трафика в зависимости от cgroups, основанный на eBPF <https://www.mail-archive.com/netdev@vger.kernel.org/msg123447.html>`_, что теоретически позволит очень гибко управлять трафиком контейнеров. На этом же уровне реализован SELinux.

Выше идет система инициализации системы и/или запуска контейнеров, тот же systemd, Kubernetes, rkt, Docker, fleet. Например, помимо использования SELinux, мы можем эффективно ограничивать возможности демонов благодаря `функционалу systemd <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/UVKC7BGUC3T6TCWINUHKXGYXQ3QSYODQ/>`_. Сам systemd уже нравится не только нам, но и, например, `Facebook <https://maciej.lasyk.info/2016/Dec/16/systemd-231-latest-in-centos-7-thx-to-facebook/>`_, и очень странно, что еще остались упирающиеся. 

Из-за одной уязвимости, к тому же остановленной SELinux, мы, конечно, не призываем бойкотировать Docker, `как другие <http://www.boycottdocker.org/>`_. Просто оглянитесь вокруг - возможно вам будет удобнее управлять контейнерами используя другие механизмы (systemd, Kubernetes, rkt).
