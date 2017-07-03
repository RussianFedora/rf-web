.. title: Дыра в BASH
.. slug: Дыра-в-bash
.. date: 2014-09-25 09:58:22
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: Peter Lemenkov

**Это архивная статья**


Независимый разработчик, `Stephane
Chazelas <http://stephane.chazelas.free.fr/Stephane-CHAZELAS-2010.html>`__,
отловил прекрасную дыру в BASH, которую `подтвердили наши
коллеги <https://securityblog.redhat.com/2014/09/24/bash-specially-crafted-environment-variables-code-injection-attack/>`__.

Учитывая, что по религии юниксвэя, легко читаемыми баш-портянками
залепляются все возможные отверстия (OpenSSH, DHCP-клиенты и т.п.), то
дыра получилась массивная. `По десятибалльной системе ее оценивают в 10
баллов <https://www.theregister.co.uk/2014/09/24/bash_shell_vuln/>`__, и
для ее использования не нужно авторизации.

За подробностями предлагаем `сходить на
OpenNET.ru <https://www.opennet.ru/opennews/art.shtml?num=40667>`__, где
коллеги-аналитики уже обсуждают новость. Обновления уже доступны, так
что стоит поскорее обновиться.

