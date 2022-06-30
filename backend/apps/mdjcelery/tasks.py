#coding:utf-8
import os
from celery import task,shared_task,platforms
from django.conf import settings
from utils.util import local_cmd

platforms.C_FORCE_ROOT = True

@task()
def add(x, y):
    return x + y

@task()
def test_task():
    return 'test task done'

@task()
def local_command(**kwargs):
    ret = local_cmd(kwargs['cmd'])
    return ret.stdout.read()

@task()
def local_script(**kwargs):
    script_file = '{}/media/{}'.format(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),kwargs['script_name'])
    cmd = '{} {}'.format(script_file, kwargs['script_args'])
    ret = local_cmd(cmd)
    return ret.stdout.read()

@task()
def remote_command(**kwargs):
    cmd = '''salt --out=raw '%s' cmd.run "%s"''' % (kwargs['host'],kwargs['cmd'])
    ret = local_cmd(cmd)
    return ret.stdout.read()

@task()
def remote_script(**kwargs):
    cmd = """salt --out=raw '%s' cmd.script salt://%s '%s'""" % (kwargs['host'], kwargs['script_name'], kwargs['script_args'])
    ret = local_cmd(cmd)
    return ret.stdout.read()
