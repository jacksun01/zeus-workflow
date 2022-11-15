---
## 分析架构
https://note.youdao.com/s/byE8XhnT

## 后端代码
后端：*******************************************************************************************
--backend
-----extra_apps				#完整第三方系统或者模块  例如xadmin-django后台
-----logs						#后台程序日志存储目录
-----media					#静态日志
-----project   					#后台总体 配置，启动，url 路由，以及wsgi启动 配置
-----utils						#后台所有系统 共用 验证，抽象 目录
----------util.py  				#公共工具方法集合  例如 远程连接，加密解密，短信发送，表结构解析
----------base_mixin.py		#抽象中间件								基础类 
----------base_model.py		#抽象 ORM模型 中对象  					基础类 BaseModel
----------base_resource.py	#抽象  导入导出功能 自定义字段 				基础类 BaseResource
----------base_view.py		#抽象 逻辑 控制类 							基础类  BaseModelViewSet.BaseGenericViewSet
-----manage.py				#python启动文件
-----requirements.txt			# 项目启动需要插件包文件
-----uwsgi.ini					#wusgi.ini 使用uwsgi启动配置
-----apps    					#模块或者子系统包
----cmdb					#资产管理
----modellog				#日志管理
----users					#用户管理
================================大部分模块都拥有这些文件=======================================================
------management						# 模块管理目录  一般存放 初始化，定时任务 操作的脚本等
------migrations						# ORM模型 django 操作数据库表结构脚步记录目录
------models.py						#ORM模型中的 对象 类
------serializers.py						# 序列化文件
------views.py							# view 层   (接收 request参数，短业务逻辑(10行以内)/service业务逻辑引用，返回数据) 
------service/							# service 层(根据资源定义文件，对idc资源 长业务逻辑处理)						
  user.py						#用户资源 业务逻辑文件
  role.py
------resources.py						#导入导出自定义字段文件
------filters.py							#查询过滤条件文件  
------urls.py							#url 映射文件
------adminx.py						#django后台管理操作文件
------apps.py							#模块或者app基础信息类 添加到 总项目中 INSTALLED_APPS才会被使用
------util.py							# 模块 工具类
------config/							# 配置文件目录 所有这个app的配置文件都要放到这个目录下
xxxx1.yaml
xxx2.ini
=========================================================================================================
------middleware.py						#中间件 文件
------auth.py							# 去掉 csrf检查
------ldap_tool.py						#ldap操作相关
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


