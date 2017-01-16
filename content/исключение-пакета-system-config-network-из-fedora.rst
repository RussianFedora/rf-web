.. title: Исключение пакета system-config-network из Fedora
.. slug: исключение-пакета-system-config-network-из-fedora
.. date: 2012-02-28 15:54:47
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. author: mama-sun

**Это архивная статья**


На прошлой неделе в одной из рассылок Fedora проскочил
`запрос <http://lists.fedoraproject.org/pipermail/rel-eng/2012-February/013517.html>`__
на исключение пакета
*`system-config-network <https://admin.fedoraproject.org/pkgdb/acls/name/system-config-network?_csrf_token=53e23684570e2266331501bb2111e28aa367db21>`__*
из Fedora Rawhide и будущих версий Fedora.

При ближайшем рассмотрении выяснилось, что
`это <https://bugzilla.redhat.com/show_bug.cgi?id=493606>`__ происходит
в рамках "`System Configuration Tools Cleanup
Project <https://bugzilla.redhat.com/show_bug.cgi?id=480902>`__", т.е.
проекта по приведению в приличный вид конфигурационных приложений. По
всей видимости под проект попадут и некоторые другие приложения. В
частности пакет
*`system-config-network <https://admin.fedoraproject.org/pkgdb/acls/name/system-config-network?_csrf_token=53e23684570e2266331501bb2111e28aa367db21>`__*
собираются исключить из-за схожести с
`NetworkManager <https://admin.fedoraproject.org/pkgdb/acls/name/NetworkManager>`__'ом.

