#!/bin/bash
#before install check DB setting in
#	judge.conf
#	hustoj-read-only/web/include/db_info.inc.php
#	and down here
#and run this with root
#CENTOS/REDHAT/FEDORA WEBBASE=/var/www/html APACHEUSER=apache
sudo apt-get update
DBUSER=root
DBPASS=root
printf "Input Database(MySQL) Username:"
read tmp
if test -n "$tmp"
then
DBUSER="$tmp"
fi
printf "Input Database(MySQL) Password:"
read tmp
if test -n "$tmp"
then
DBPASS="$tmp"
fi
#try install tools
if uname -a|grep 'Ubuntu\|Debian'
then
sudo apt-get install make  g++ clang libmysql++-dev mysql-server mono-gmcs subversion python3 python3-pip
sudo apt-get install make  g++ clang libmysql++-dev mysql-server mono-gmcs subversion python3 python3-pip
sudo /etc/init.d/mysql start
else
sudo yum -y update
sudo yum -y install httpd mysql-server gcc-c++  mysql-devel php-mbstring glibc-static flex
sudo /etc/init.d/mysqld start
echo "/usr/bin/judged" > judged
fi
#create user and homedir
sudo  /usr/sbin/useradd -m -u 1536 judge
#compile and install the core
cd hust_oj_core/trunk/core
sudo ./make.sh
cd ../install
#install web and db
sudo mysql -h localhost -u$DBUSER -p$DBPASS < db.sql
#create work dir set default conf
sudo    mkdir /home/judge
sudo    mkdir /home/judge/etc
sudo    mkdir /home/judge/data
sudo    mkdir /home/judge/log
sudo    mkdir /home/judge/run0
sudo    mkdir /home/judge/run1
sudo    mkdir /home/judge/run2
sudo    mkdir /home/judge/run3
sudo cp java0.policy  judge.conf /home/judge/etc
sudo chown -R judge /home/judge
sudo chgrp -R $APACHEUSER /home/judge/data
sudo chgrp -R root /home/judge/etc /home/judge/run?
sudo chmod 775 /home/judge /home/judge/data /home/judge/etc /home/judge/run?
#update database account
SED_CMD="s/OJ_USER_NAME=root/OJ_USER_NAME=$DBUSER/g"
SED_CMD2="s/OJ_PASSWORD=root/OJ_PASSWORD=$DBPASS/g"
sed $SED_CMD judge.conf|sed $SED_CMD2 >/home/judge/etc/judge.conf
SED_CMD="s/DB_USER=\\\"root\\\"/DB_USER=\\\"$DBUSER\\\"/g"
SED_CMD2="s/DB_PASS=\\\"root\\\"/DB_PASS=\\\"$DBPASS\\\"/g"
#boot up judged
sudo cp judged /etc/init.d/judged
sudo chmod +x  /etc/init.d/judged
sudo ln -s /etc/init.d/judged /etc/rc3.d/S93judged
sudo ln -s /etc/init.d/judged /etc/rc2.d/S93judged
sudo /etc/init.d/judged start
#install web dependence
cd ../../../onlineTest
pwd
sudo pip3 install django==1.9.9 -i https://mirrors.njupt.edu.cn/nexus/repository/pypi/simple
sudo pip3 install pymysql -i  https://mirrors.njupt.edu.cn/nexus/repository/pypi/simple
sudo pkill -9 judged
sudo judged
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
sudo python3 manage.py loaddata init_data.json
echo "create a super user:"
sudo python3 manage.py createsuperuser
