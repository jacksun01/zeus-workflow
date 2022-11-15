---
## 分析架构
https://note.youdao.com/s/byE8XhnT


## Description

Flexible work order system: The front end of the work order project is flexibly configured according to the needs, and the approval process is dynamically configured.
#Jacksun qq:774428957
#email:105163356@qq.com
#wechat:taiji158
## Environment

```
Centos 6/7
Python 3.6.1-6
mysql-server 5.6.21
node 9.4.0
Django==2.1.4
djangorestframework==3.9.0
```

## How to run

Clone the repository:

```zsh
➜ git clone git@gitlab.zeus.com:aiops/django-vue-demo.git
```

Create and activate virtualenv:

```zsh
➜  virtualenv -p python3 env
➜  source env/bin/activate
```

Run scripts from Makefile that install all dependencies, run migrations and start dev server.

```zsh
(env) ➜  mysql -uroot -p -e "create database demo default charset utf8;"
(env) ➜  cp backend/config.example.ini backend/config.ini #修改后端配置
(env) ➜  修改 backend/uwsgi.ini 配置中项目路径和服务端口
(env) ➜  修改frontend/config/dev.env.js、test.env.js和prod.env.js中后端接口地址
(env) ➜  make init
(env) ➜  make dev
(env) ➜  make build-prod
(env) ➜  make start
```

Nginx config

```
[root@app1 vhosts]# vim www.zeus.com.conf
upstream demo{
    server 127.0.0.1:8002;
}
server {
        listen 80;
        server_name www.zeus.com;

        location / {
            include uwsgi_params;
            uwsgi_connect_timeout 30;
            uwsgi_pass  demo;
        }

    access_log  /opt/logs/www.zeus.com.log;
}
```

We are done.

dev

- Frontend: http://localhost:9527/
- Backend: http://localhost:8002/

prod

- Frontend: http://www.zeus.com/
- Backend: http://www.zeus.com/api/
- Xadmin: http://www.zeus.com/xadmin/
- API Docs: http://www.zeus.com/docs/

默认管理员账号：admin   密码：abcccc


