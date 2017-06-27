.. title: Криптоалгоритм ГОСТ теперь считается патентно чистым
.. slug: kriptoalgoritm-gost-teper-schitaetsia-patentno-chistym
.. date: 2017-06-26 14:18:55 UTC+03:00
.. tags: ГОСТ, openssl, cryptography, импортозамещение, патенты, legal
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

Недавно, без особого шума, `в пакет OpenSSL включили криптоалгоритм ГОСТ
<https://src.fedoraproject.org/cgit/rpms/openssl.git/commit/?id=1ff978b>`_.
Нами теперь считается, что его реализация в OpenSSL не покрывается никакими
патентами США. Поддержка доступна `начиная с Fedora 26
<https://bugzilla.redhat.com/1303016#c3>`_. Не прошло и `четырех лет
</content/bitcoin-и-шифрование-по-ГОСТу-вскоре-появится-в-fedora/>`_!

К сожалению, для работы с ГОСТ этого недостаточно. Дополнительно требуется
собрать и установить `еще одну библиотеку
<https://github.com/gost-engine/engine>`_. Тем не менее, зеленый свет включен,
и будем ожидать, что это упростит использование данного перспективного
стандарта шифрования, к которому, `как сообщается
</content/warren-togami-присоединяется-к-blockstream-и-другие-криптоновости/>`_,
есть растущий интерес.

Кроме ГОСТ патентно чистым теперь считается алгоритм `SRP
<https://ru.wikipedia.org/wiki/SRP>`_.
