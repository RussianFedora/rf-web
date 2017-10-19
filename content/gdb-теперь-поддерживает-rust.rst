.. title: GDB теперь поддерживает Rust!
.. slug: gdb-теперь-поддерживает-rust
.. date: 2016-06-07 18:39:07
.. tags: gdb, rust, gstreamer
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

Помните `новость
</content/colaboratory-rust-первая-конференция-о-rust-в-Москве>`__, что наш
коллега, `Tom Tromey <https://www.openhub.net/accounts/tromey>`__, предложил на
рассмотрение поддержку Rust в GDB? Так вот, `включили
<https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=c44af4e>`__, и
поддержка Rust будет доступна в следующем большом релизе GDB. Как раз вовремя,
чтобы начинать `использовать Rust для разработки плугинов для GStreamer
<https://coaxion.net/blog/2016/05/writing-gstreamer-plugins-and-elements-in-rust/>`__.

К сожалению, язык пока не доступен в Fedora. `Что-то все застряло
<https://bugzilla.redhat.com/915043>`__.
