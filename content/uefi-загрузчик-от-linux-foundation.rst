.. title: UEFI-загрузчик от Linux Foundation
.. slug: uefi-загрузчик-от-linux-foundation
.. date: 2013-02-09 16:47:36
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`James
Bottomley <https://plus.google.com/106426395028955095070/about>`__
`представил универсальный загрузчик
UEFI <http://blog.hansenpartnership.com/linux-foundation-secure-boot-system-released/>`__
для систем с включенным RestrictedBoot (т.н. "SecureBoot"), подписанный
ключом Microsoft. Он использует
`gummiboot <http://freedesktop.org/wiki/Software/gummiboot>`__
(загрузчик, написанный `Kay
Sievers <https://www.ohloh.net/accounts/kaysievers>`__), который уже
может запустить GRUB2. Похоже, что в случае SecureBoot без трех-четырех
загрузчиков не обойтись - такова цена безопасности.

