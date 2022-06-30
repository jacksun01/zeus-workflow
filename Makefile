init:
	cd frontend && cnpm install
	source env/bin/activate && pip install -r backend/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
	source env/bin/activate && python backend/manage.py makemigrations && python backend/manage.py migrate
	source env/bin/activate && python backend/manage.py init_users
	source env/bin/activate && python backend/manage.py init_mdjcelery
	source env/bin/activate && python backend/manage.py init_stree
	source env/bin/activate && python backend/manage.py init_cmdb
	source env/bin/activate && python backend/manage.py init_mdb
	source env/bin/activate && python backend/manage.py init_inception
	source env/bin/activate && python backend/manage.py init_workflow
	source env/bin/activate && python backend/manage.py init_cicd
	source env/bin/activate && python backend/manage.py init_mlog
	source env/bin/activate && python backend/manage.py init_mcloud
	source env/bin/activate && python backend/manage.py init_mfalcon
	source env/bin/activate && python backend/manage.py init_mk8s
	source env/bin/activate && python backend/manage.py init_msc
	source env/bin/activate && python backend/manage.py init_middleapp
	source env/bin/activate && python backend/manage.py collectstatic --noinput

migrate:
	source env/bin/activate && python backend/manage.py makemigrations && python backend/manage.py migrate

dev:
	npm run --prefix frontend dev & (source env/bin/activate && python backend/manage.py runserver)
	source env/bin/activate && python backend/manage.py celery worker -Q task_a --loglevel=info
	source env/bin/activate && python backend/manage.py celery worker -Q task_b --loglevel=info
	source env/bin/activate && python backend/manage.py celery beat --loglevel=info

start:
	test ! -f backend/logs/gunicorn.pid && source env/bin/activate && (nohup gunicorn -c backend/gunicorn.conf.py project.wsgi &) || echo 'gunicorn running'
	echo "`date` start" >> backend/logs/restart.log

stop:
	test -f backend/logs/gunicorn.pid && source env/bin/activate && kill -9 `cat backend/logs/gunicorn.pid`  || echo 'gunicorn closed'
	rm -f backend/logs/gunicorn.pid
	echo "`date` stop" >> backend/logs/restart.log

restart:
	test -f backend/logs/gunicorn.pid && source env/bin/activate && kill -9 `cat backend/logs/gunicorn.pid`  || echo 'gunicorn closed'
	rm -f backend/logs/gunicorn.pid
	test ! -f backend/logs/gunicorn.pid && source env/bin/activate && (nohup gunicorn -c backend/gunicorn.conf.py project.wsgi &)  || echo 'gunicorn running'
	echo "`date` restart" >> backend/logs/restart.log

build-prod:
	npm run --prefix frontend  build:prod
	source env/bin/activate && python backend/manage.py collectstatic --noinput

build-test:
	npm run --prefix frontend  build:test
	source env/bin/activate && python backend/manage.py collectstatic --noinput

start-asgi:
	nohup daphne -p 8005 backend.project.asgi:application --access-log=backend/logs/asgi.log &>/dev/null &

restart-celery:
	mkdir -p backend/logs/celery/
	test -f backend/logs/celery/celery_task_a.pid && cat backend/logs/celery/celery_task_a.pid|xargs kill || echo 'celery_task_a closed'
	test -f backend/logs/celery/celery_task_b.pid && cat backend/logs/celery/celery_task_b.pid|xargs kill || echo 'celery_task_b closed'
	test -f backend/logs/celery/celery_beat.pid && cat backend/logs/celery/celery_beat.pid|xargs kill || echo 'celery_beat closed'
	test -f backend/logs/celery/celery_flower.pid && cat backend/logs/celery/celery_flower.pid|xargs kill || echo 'celery_flower closed'
	source env/bin/activate && cd backend && nohup  celery worker -A project --loglevel=info -Q task_a,task_b -c 24 --loglevel=info --pidfile=logs/celery/celery_task_b.pid &>logs/celery/celery_task_b.log 2>&1 &
	source env/bin/activate && cd backend && nohup celery beat -A project --loglevel=info --pidfile=logs/celery/celery_beat.pid &>logs/celery/celery_beat.log 2>&1 &
	source env/bin/activate && cd backend && nohup  celery flower -A project --loglevel=info --pidfile=logs/celery/celery_flower.pid &>logs/celery/celery_flower.log 2>&1 &
