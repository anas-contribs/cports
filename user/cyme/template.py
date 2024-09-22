pkgname = "cyme"
pkgver = "1.8.3"
pkgrel = 0
build_style = "cargo"
# hostmakedepends = ["cargo-auditable", "pkgconf"]
# makedepends = [
#     "libgit2-devel",
#     "rust-std",
#     "zlib-ng-compat-devel",
# ]
pkgdesc = "System USB buses and devices listing utility"
maintainer = "Anas Elgarhy <anas.elgarhy.dav@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://eza.rocks"
source = f"https://github.com/tuna-f1sh/cyme/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = ""


def post_install(self):
    self.install_license("LICENCE")
    self.install_man("doc/cyme.1")
    self.install_completion("doc/cyme.bash", "bash")
    self.install_completion("doc/_cyme", "zsh")
    self.install_completion("doc/cyme.fish", "fish")
