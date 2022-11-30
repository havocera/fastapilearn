FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8
RUN sed -i 's@http://archive.ubuntu.com/ubuntu/@http://mirrors.aliyun.com/ubuntu/@g' /etc/apt/sources.list # 更换源

RUN apt-get update -qq
RUN mkdir -p /root/directory
WORKDIR /root/directory
COPY requirements.txt requirements.txt
COPY . /root/directory  


RUN  apt-get clean && \
     apt-get update && \
     apt-get install -y libmysqlclient-dev tzdata  \
                        python3 python3-dev python3-pip libpcre3 libpcre3-dev  uwsgi-plugin-python3\
    && apt-get clean \
    && apt-get autoclean \
   && ln -sf /usr/bin/pip3 /usr/bin/pip && ln -sf /usr/bin/python3 /usr/bin/python \
   && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 以上操作 apt-get 清理缓存,update,安装python3.8以及安装 python模块 的一系列操作

RUN apt-get update -q \
    && apt-get install -y wget curl vim  # apt-get 安装 wget curl vim


EXPOSE 48080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "48080"]
