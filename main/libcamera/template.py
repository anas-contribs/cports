pkgname = "libcamera"
pkgver = "0.3.1"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dtest=true"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-jinja2",
    "python-ply",
    "python-pyyaml",
]
makedepends = [
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtest-devel",
    "libevent-devel",
    "libunwind-devel",
    "libyaml-devel",
    "openssl-devel",
    "udev-devel",
]
pkgdesc = "Open source camera stack and framework"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://libcamera.org"
source = f"https://github.com/libcamera-org/libcamera/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ef93fba5751f55299ee8d593eaefc1b9b2b34008be7db19d3d2c05588d855c4f"
nostrip_files = ["usr/lib/libcamera/ipa*.so"]


def post_install(self):
    from cbuild.util import strip

    for f in (self.destdir / "usr/lib/libcamera").glob("ipa*.so"):
        fr = f.relative_to(self.destdir)
        print(f"   Stripping and signing: {fr.name}")
        strip.strip_attach(self, [fr])
        self.do(
            "src/ipa/ipa-sign.sh",
            "build/src/ipa-priv-key.pem",
            self.chroot_destdir / fr,
            f"{self.chroot_destdir / fr}.sign",
        )


@subpackage("gstreamer-libcamera")
def _(self):
    self.subdesc = "GStreamer support"
    self.install_if = [self.parent, "gstreamer"]
    return ["usr/lib/gstreamer-1.0"]


@subpackage("libcamera-devel")
def _(self):
    return self.default_devel(extra=["usr/bin/lc-compliance"])
