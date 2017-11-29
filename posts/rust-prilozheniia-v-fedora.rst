.. title: Rust-приложения в Fedora
.. slug: rust-prilozheniia-v-fedora
.. date: 2017-11-29 18:04:46 UTC+03:00
.. tags: rust, golang, security, rhel, node.js
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Благодаря нашему коллеге, `Igor Gnatenko <https://blogs.gnome.org/ignatenko/>`_, в Fedora `начали появляться приложения на Rust <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/D7PYBU7JKGLRYR2HKRXBM6EGZZEDCK33/>`_. Само собой, что и необходимые библиотеки тоже.

Спросите, зачем вообще включать библиотеки на Golang или Rust? Ведь в этих
языках есть свои рудиментарные менеджеры зависимостей, и не лучше ли
использовать их? Нет, не лучше. Как показывает практика других языков со своими
полукривыми менеджерами зависимостей, `это приводит к проблемам
<https://snyk.io/blog/77-percent-of-sites-still-vulnerable/>`_. Причем,
ситуация не улучшается годами, из чего мы делаем вывод, что менеджер
зависимостей, специфичный для некоего языка, не может решить значительное
количество задач, которые давно решают пакетные менеджеры в
Linux-дистрибутивах. Справедливее языкоспецифичные менеджеры зависимостей
называть менеджерами зависимостей сборки, но там, все-таки, бывает по-разному.

Кстати, `Golang, Rust (и, разумеется, LLVM) также уже некоторое время доступны
в RHEL
<https://developers.redhat.com/blog/2017/10/04/red-hat-adds-go-clangllvm-rust-compiler-toolsets-updates-gcc/>`_.
Как `и Node.js
<https://developers.redhat.com/blog/2017/10/04/red-hat-updates-python-php-node-js-supports-new-arches/>`_,
само собой! Пробуйте.
