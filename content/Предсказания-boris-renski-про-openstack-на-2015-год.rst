.. title: Предсказания Boris Renski про OpenStack на 2015 год.
.. slug: Предсказания-boris-renski-про-openstack-на-2015-год
.. date: 2014-12-19 15:06:25
.. tags: openstack, clouds, mirantis, redhat, vmware, debian, патенты, legal
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


`Boris Renski <https://www.linkedin.com/in/borisrenski>`__ опубликовал свои
`предсказания про OpenStack на 2015 год
<https://www.informationweek.com/cloud/infrastructure-as-a-service/3-openstack-predictions-for-2015/a/d-id/1318104?print=yes>`__.

Некоторые наши друзья и коллеги не согласились и разочарованы тем, что они
называют "anti-RedHat" (например, `раз
<https://plus.google.com/+jwildeboer/posts/iUnCyRKugPj>`__, `два
<https://plus.google.com/+AndrewCathrow/posts/GC3SVhDNGAL>`__, `три
<https://plus.google.com/+DanielDumitriu/posts/gFHNEBRRDkN>`__), но те из них,
кто работает в Mirantis, наоборот ободрены похвалой начальства и говорят, что
они вполне могут пободаться с Red Hat на равных, особенно при поддержке
сильного вендора.

Итак, Борис предсказал, что в 2015 году

- VMware подпишет больше контрактов на OpenStack, чем Red Hat

- Основной платформой для OpenStack будет Debian

- Использование devel-ветки больше не будет популярно

Борис, между прочим, очень хорошо осведомлен, и не на пустом месте фантазирует,
как бы мы ни симпатизировали Red Hat.

По первому пункту напоминаем, что `у VMware скоро будет облачный продукт на
базе OpenStack </content/vmware-выпускает-свой-продукт-на-базе-openstack>`__, а
по виртуализационным решениям, по мнению экспертов, `они твердо держат
лидерство </content/Текущая-ситуация-на-рынке-виртуализации-x86-систем>`__ (это
не доля рынка, напомним, а экспертные оценки). С другой стороны, у VMware пока
продукта-то нет, да и в Mirantis моногамности по отношению к VMware `пока не
наблюдалось </content/Облачные-новости-1>`__.

По второму пункту, тут Борис скорее всего имеет в виду не Debian, а HP. У
Hewlett-Packard тоже `есть облачное решение </content/Облачные-новости-2>`__,
базирующееся на Debian, в котором они за последний год навели порядок,
постепенно устраняя выглядевшее безнадежным технологическое отставание, и
обезоружили сторонников дальнейшего загнивания. Сделать пришлось много -
невзирая на стоны луддитов от опенсорса, Debian постепенно переходит на
systemd, `начал отказываться от тянущей его на дно поддержки устаревших ядер
</content/debian-отказался-от-kfreebsd>`__, и это еще не конец.

Понятно, что Debian продвинулся далеко вперед, но вот `последний опрос
пользователей OpenStack </content/Итоги-openstack-user-survey>`__ вроде бы не
подтверждает предположения Бориса о грядущей популярности Debian. Тут, конечно,
нужно учесть разницу в восприятии. Дело в том, что лидирующий по опросам
дистрибутив традиционно убыточен. Не то, чтобы с местом из четвертой-пятой
десятки по вкладу в OpenStack у поддерживающей его компании у них совсем не
было заказчиков, но отсутствие разработчиков не дает им возможности громко
заявить о себе, как о надежном центре по поддержке решений. Многочисленные
бесплатные пользователи пока в деньги для компании не конвертируются, в отличие
от нескольких следующих за ними дистрибутивов. Ну, собственно, Борис об этом и
заявил - нет разработчиков, не будет и клиентов. Вероятно он рассматривал
вообще лишь коммерчески успешные варианты.

Но даже с коммерчески успешными вариантами, ситуация для простого наблюдателя
не выглядит радужной для Debian. Второе и третье место, это Red Hat, и тут-то
традиционно даже бесплатные пользователи рано или поздно конвертируются в
деньги. Debian идет далеко позади. Тут, конечно сказывается и технологическое
оставание от семейства Red Hat, и отсутствие графика релизов, и отсутствие
компании, оказывающей коммерческую поддержку. В коммьюнити хиппи от OpenSource
всегда твердили, что выпустим не к сроку, а когда будет готово - теперь
попланируй-ка, менеджер проектов, на такой базе. Они еще и всерьез гордились
отстутствием релизов, наивно полагая, что затягивая выход, из продукта
улетучатся баги (мнение, надо признать, как ошибочное, так и популярное).
Понятно, что с приходом Кровавого Энтерпрайза в коммьюнити Debian, с казацкой
вольницей будет покончено, но нагнать такое отставание за год будет непросто.
Вероятно Борис, как более осведомленный человек, знает чуть больше, чем
говорит, например количество и прибыльность клиентов для компаний, и их
настроения. Ну посмотрим.

Вообще у нас двойственное впечатление от ставки настолько крупного вендора, как
HP, на Debian, и его участие в активной модернизации как коммьюнити
дистрибутива, так и самой его пакетной базы и архитектуры.

С одной стороны, это здорово, что больше и больше дистрибутивов склоняются на
нашу сторону в спорах о постройке единообразного стандартного Linux. С другой -
тем самым компания Red Hat взращивает своих же прямых конкурентов. К счастью
количество разработчиков, и вытекающий из этого `уровень поддержки
</content/selinux-больше-не-будет-пугать-пользователей-запускающих-windows-программы-в-wine>`__,
однозначно решает вопрос положительно для компании. Ну и из нашего спортивного
опыта мы знаем, что без соперника подходящего уровня можно одряхлеть и
зачахнуть даже в очень выгодных условиях.

Насчет поддержки - есть еще юридический аспект. Раньше, из производителей
дистрибутивов Linux `лишь Red Hat могла всерьез зарубаться с патентными
троллями в защиту своих клиентов </content/Короткие-новости-4>`__, но понятно,
что у HP есть патентное портфолио несопоставимых размеров. Если (если!) они
будут покрывать им своих пользователей своего OpenStack и своего Debian, то
будет очень интересно посмотреть на развитие событий.

По третьему пункту тут интереснее. Понятно, что кровавый патчинг
продакшен-систем прямо из master, это не самая рациональная практика.

Но, к счастью/сожалению OpenStack настолько динамично развивается, что порой
просто глупо не использовать гораздо более функциональный master-бранч. Однако,
хотя OpenStack, это молодой и быстро изменяющийся проект, тут хочется
согласиться с Борисом - есть ощущение, что сейчас (в следующем году), когда
понимание того, что, зачем, и как нужно сделать, уже появилось, появится и
запрос на стабильную платформу. Вообще, быстрый бег вперед, без оглядки на
стабильность, уже начинает `вредить проекту, порождая сильно недовольных как
минимум отдельными компонентами пользователей
<http://juick.com/maxlapshin/2755849#unfoldall>`__. И тут есть очень
интересное, чего Борис, как кажется некоторым нашим участникам, не заметил -
есть компания, у которой огромный опыт бэкпортирования из мастера в stable и
поддержки стабильных версий, и она поддерживает совсем не Debian. Это может
серьезно усложнить задачу HP по стандартизации Debian, как *the platform of
choice* для OpenStack.

В общем год для OpenStack будет интересный, и мы с интересом смотрим в будущее.
