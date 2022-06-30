#author Jack qq:774428957
import sys
import os
import multiprocessing

proc_name = 'open-galaxy'
bind = "0.0.0.0:8000"
worker_class = 'sync'

# 工作进程数
workers = multiprocessing.cpu_count()
# 指定每个工作进程开启的线程数
threads = multiprocessing.cpu_count() * 2

# 处理请求的工作线程数，使用指定数量的线程运行每个worker。为正整数，默认为1。
worker_connections = 2000

# 最大客户端并发数量防止内存泄漏的两个参数
max_requests = 1500
max_requests_jitter=512

# 监听队列
backlog = 512

# 设置超时时间120s，默认为30s。按自己的需求进行设置timeout = 120
timeout = 120
# # 超时重启
# graceful_timeout = 300

# 启动方式
daemon = False

BASE_DIR = '/opt/open-galaxy/backend'
sys.path.append(BASE_DIR)

LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
chdir = BASE_DIR

loglevel = 'debug'  # 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
#
# # 访问日志文件
accesslog = '%s/access.log' %  (LOG_DIR)
# # 错误日志文件
errorlog = '%s/gunicorn_startup_info.log' %  (LOG_DIR)

pidfile = '%s/gunicorn.pid' % (LOG_DIR)