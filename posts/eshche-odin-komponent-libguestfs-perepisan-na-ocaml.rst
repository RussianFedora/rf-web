.. title: Еще один компонент libguestfs переписан на Ocaml
.. slug: eshche-odin-komponent-libguestfs-perepisan-na-ocaml
.. date: 2017-06-09 17:25:44 UTC+03:00
.. tags: libguestfs, ocaml
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Наш коллега, Rich W.M. Jones, объявил, что `переписал еще один компонент
libguestfs на Ocaml
<https://rwmj.wordpress.com/2017/06/04/new-in-libguestfs-rewriting-bits-of-the-daemon-in-ocaml/>`_.
Напомним, Ocaml, это мультипарадигмальный язык программирования, на судьбе
которого трагическим образом сказалась чудовищная близорукость основного
архитектора языка и системы, всерьез считавшего, что `многопроцессорные системы
не будут популярны
<http://mirror.ocamlcore.org/caml.inria.fr/pub/ml-archives/caml-list/2002/11/64c14acb90cb14bedb2cacb73338fb15.en.html>`_.
Тем не менее, язык довольно удобен, и широко популярен в узких кругах.

Благодаря переходу на Ocaml некоторые части libguestfs сократились в размере
(например, со 183 строк на Си до 56 на Ocaml).
