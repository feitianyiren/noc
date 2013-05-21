#!/bin/sh
##----------------------------------------------------------------------
## Debian 7.0 bootstrap0.sh
## Initialize system and install all prerequisites to NOC
##----------------------------------------------------------------------
## Copyright (C) 2007-2013 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

##
## Helper functions definitions
##
PROGNAME=`basename $0`

error_exit ( ) {
    echo "$PROGNAME: ${1:-'Unknown error'}" 1>&2
    echo "Terminating" 1>&2
    exit 1
}

info ( ) {
    echo $1 1>&2
}

aptinstall ( ) {
    info "Installing $1"
    apt-get install -y $1 || error_exit "Failed to install $1"
}

##
## Update base system
##
info "Updating base system"
apt-get update || die "Failed to run: apt-get: update"
apt-get upgrade || die "Failed to run: apt-get upgrade"
apt-get dist-upgrade || die "Failed to run: apt-get dist-upgrade"
##
## Create NOC user and group
##
info "Create group 'noc'"
grep -e ^noc: /etc/group
if [ $? -ne 0 ]; then
    groupadd noc
fi
info "Create user 'noc'"
grep -e ^noc: /etc/passwd
if [ $? -ne 0 ]; then
    useradd -g noc -s /bin/bash -d /home/noc -m noc
    passwd noc << __EOF__
thenocproject
thenocproject
__EOF__
fi
##
## Install base packages
##
aptinstall less
aptinstall telnet
aptinstall tcpdump
aptinstall python
aptinstall python-dev
aptinstall python-virtualenv
aptinstall libgmp10
aptinstall libgmp-dev
aptinstall nginx
aptinstall postgresql
aptinstall libpq-dev
aptinstall postgresql-9.1-postgis
aptinstall postgis
aptinstall mongodb
aptinstall mercurial
aptinstall smitools
aptinstall sudo
##
## Set up Postgresql database
##
info "Create PostgreSQL 'noc' user and database"
su - postgres -c psql << __EOF__
CREATE USER noc SUPERUSER ENCRYPTED PASSWORD 'thenocproject';
CREATE DATABASE noc WITH OWNER=noc ENCODING='UTF8';
__EOF__
[ $? -eq 0 ] || error_exit "Failed to initialize PostgreSQL database and user"
##
## Set up mongodb user
##
info "Setting MongoDB authentication"
mongo noc << __EOF__
db.addUser("noc", "thenocproject")
__EOF__
##
## Set up daemon autostart
##
update-rc.d postgresql enable
update-rc.d mongodb enable
update-rc.d nginx enable
##
## Get NOC
##
cd /opt || error_exit "cd /opt failed"
info "Fetching NOC"
hg clone http://hg.nocproject.org/noc noc
if [ "$1" != "--no-bootstrap" ]; then
    info "Running bootstrap.sh"
    /opt/noc/share/vagrant/x86_64/Debian/7.0/bootstrap.sh
fi
