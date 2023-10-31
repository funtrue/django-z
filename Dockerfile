# django-z Dockerfile
# Version 1.0
# author funtrue

# Base images
FROM centos:centos7

WORKDIR /opt

# add packge
ADD . .
RUN yum clean all && yum makecache && yum -y update --nogpgcheck \
&& yum -y install python3 vim mysql-devel python3-devel postgresql-devel* gcc gcc-c++ automake pcre pcre-devel zlib zlib-devel openssl openssl-devel \ 
&& pip3 install  --no-cache-dir --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/ \
&& pip3 install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ && yum clean all

# start django
CMD ["/bin/bash", "start_project.sh"]
