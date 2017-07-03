.. title: Rust в Fedora
.. slug: rust-в-fedora
.. date: 2016-07-28 14:16:37
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Ситуация с языком Rust сдвинулась с мертвой точки. Совсем недавно `Rust
официально одобрили для включения в
Fedora <https://bugzilla.redhat.com/1356907>`__. Как раз успеем - `наши
коллеги уже используют язык для системного
ПО </content/rust-для-системного-ПО>`__, и `отладка приложений на Rust
уже доступна в GBD </content/gdb-теперь-поддерживает-rust>`__. Включение
Rust и сопутствующей сборочной инфраструктуры, `пакета
Cargo <https://bugzilla.redhat.com/1357749>`__, объявлено `фичей Fedora
25 <https://fedoraproject.org//wiki/Changes/RustCompiler>`__.

`Firefox с версии 48 будет использовать компоненты, написанные на
Rust <https://hacks.mozilla.org/2016/07/shipping-rust-in-firefox/>`__, и
разработчики Mozilla Foundation всячески призывают следовать их примеру.

Так что инициатива нашего коллеги, `Andy
Grover <https://www.openhub.net/accounts/agrover>`__, по `использованию Rust
в системном ПО </content/rust-для-системного-ПО>`__ тоже получила
поддержку с их стороны. Недавно Andy выступил на ежемесячном митапе по
Rust, проводимом MoFo. Тема его выступления была - `"Froyo: Using Rust
to get fancy with
storage" <https://www.meetup.com/PDXRust/events/230723873/>`__. К
сожалению, доступно только видео на Archive.org:
Раз уж заговорили о Rust, то обратите внимание на это `спорное
предложение <http://notes.willcrichton.net/rust-the-new-llvm/>`__. Will
Crichton, бывший интерн Palantir Technologies и Jane Street Capital,
предлагает при разработке DSL и просто новых языков программирования
выбирать не LLVM, а Rust в качестве целевой платформы. `К 2035 году в РФ
планируют разработать суверенный национальный язык
программирования <http://kommersant.ru/doc/3018874>`__, безопасный к
взлому и уводу аккаунта во Вконтакте, так что самое время начать
обсуждение его архитектуры.

