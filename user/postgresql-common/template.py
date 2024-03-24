pkgname = "postgresql-common"
pkgver = "1.0"
pkgrel = 0
build_style = "meta"
# technically a cycle, but we don't want this to be installable without having
# some postgresql provider around, so hack around it anyway
depends = ["virtual:postgresql-runtime!base-files"]
pkgdesc = "Common files for PostgreSQL"
maintainer = "mia <mia@mia.jetzt>"
license = "custom:none"
url = "https://chimera-linux.org"


def do_install(self):
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="postgresql.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="postgresql.conf",
    )
