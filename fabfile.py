from fabric.api import env, sudo

env.use_ssh_config = True

tz = "Europe/Moscow"
ntp = "ru.pool.ntp.org"
repo = "mirror.yandex.ru"

yum_conf = "http://%s/scientificlinux/6x/x86_64/os/Packages/yum-conf-sl6x-1-2.noarch.rpm" % repo
sl_release = "http://%s/scientificlinux/6x/x86_64/os/Packages/sl-release-6.5-1.x86_64.rpm" % repo


def set_tz():
    sudo("rm -f /etc/localtime")
    sudo("ln -s /usr/share/zoneinfo/%s /etc/localtime" % tz)


def install(pkg):
    sudo("yum install -y %s" % pkg)


def sync_time():
    install("ntpdate")
    sudo("ntpdate %s" % ntp)


def scientifize():
    sudo("rpm -ivh %s" % yum_conf)
    sudo("rpm -ivh --force %s" % sl_release)
    sudo("sed -i 's#distroverpkg=centos-release#distroverpkg=sl-release#g' /etc/yum.conf")
    sudo("yum erase -y centos-release")
    sudo("yum clean all")
    sudo("yum distro-sync -y")
    sudo("yum reinstall -y `rpm -qa --qf '%{NAME} %{VENDOR}\n' | grep CentOS | awk '{print $1}'`")


def main():
    set_tz()
    sync_time()
    scientifize()
