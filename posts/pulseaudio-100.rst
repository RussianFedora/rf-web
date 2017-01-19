.. title: PulseAudio 10.0
.. slug: pulseaudio-100
.. date: 2017-01-19 17:35:45 UTC+03:00
.. tags: pulseaudio, openssl, compatibility
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Вышел `PulseAudio 10 <https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/10.0/>`_. Из изменений этой версии хочется отметить использование по умолчанию функционала `memfd </content/memfd-в-ядре/>`_, впервые включенного в `PulseAudio 9.0 </content/pulseaudio-90/>`_, и полная поддержка OpenSSL 1.1.0, с которой `у нас много проблем <https://bugzilla.redhat.com/1383740>`_ при подготовке к `Fedora 26 <https://fedoraproject.org//wiki/Changes/OpenSSL110>`_. Это обновление OpenSSL оказалось настолько болезненное, что `его уже внесли в список типичных анти-паттернов разработки <https://www.mail-archive.com/tech@openbsd.org/msg36437.html>`_. К сожалению, ситуация для криптобиблиотек довольно типичная. Они, порой, как будто специально внедряют антипаттерны разработки.

Эти и другие изменения уже обсуждаются коллегами-аналитиками на `OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=45884>`_ и на `ЛОРе <https://www.linux.org.ru/news/multimedia/13158064>`_.
