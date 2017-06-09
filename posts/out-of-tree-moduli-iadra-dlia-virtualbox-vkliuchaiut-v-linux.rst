.. title: Out-of-tree guest-модули ядра для VirtualBox включают в Linux
.. slug: out-of-tree-moduli-iadra-dlia-virtualbox-vkliuchaiut-v-linux
.. date: 2017-06-09 17:38:58 UTC+03:00
.. tags: kernel, virtualbox
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Peter Lemenkov

VirtualBox продолжают использовать на десктопах, особенно на  Windows. Нас
беспокоит лишь одна деталь - работа Fedora, как гостевой системы в VirtualBox.
Для ее работы нужны т.н. гостевые модули, которые никогда не были включены в
ядро Linux, хотя и поставляются с открытым кодом. Это, разумеется, создавало
проблемы на ровном месте, т.к. для полноценного использования Fedora в
VirtualBox эти драйверы приходилось сначала собрать в Fedora, а потом
установить (и переустанавливать с каждой сменой ядра). Пользователям Windows
это постоянно создавало проблемы.

Наконец-то, наш коллега, `Hans de Goede <https://github.com/jwrdegoede>`_,
решил исправить ситуацию, для чего `начал процесс переделки этих гостевых
драйверов <http://hansdegoede.livejournal.com/17743.html>`_, планируя включить
результаты в ядро Linux. В процессе уже `удалось уменьшить размер видеодрайвера
с 52681 строк кода до 7275
<https://lists.freedesktop.org/archives/dri-devel/2017-June/143839.html>`_.

Нужно отметить, что работу VirtualBox в Linux это не улучшит. Там так и
придется (пере)собирать драйверы, чтобы она работала. А зачем вы используете
коробку в Linux?
