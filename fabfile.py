from fabric import Connection as conn
from invoke import task, run, env, sudo
import numpy as np
import os, sys
import json

env.parentdirectory = '/var/www/html'
env.appdirectory = '{}/icharbeitezuhaus.com'.format(env.parentdirectory)
env.applogs = '{}/logs'.format(env.appdirectory)
env.appsrc = '{}/public_html'.format(env.appdirectory)

keyfileloc = "../../.ssh/id_rsa.pub"

@task
def update(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":keyfileloc}) as f:
		f.run("yum update -y")

@task
def hosttypelocal(ctx):
	run('uname -s')

@task
def hosttyperemote(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":keyfileloc}) as f:
		f.run('uname -s')

@task
def diskspaceremote(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":keyfileloc}) as f:
		f.run('df')

@task
def diskspacelocal(ctx):
	run('df')

@task(help={'text':'this is it ya'})
def test(ctx, text):
	'''
	testing
	'''
	print("{}".format(text))
	# fab test --text 'this is it'
	# fab test --text='this is it'
	# fab test 'this is it'

@task
def checkstatus(ctx):
	with conn(
		"172.105.4.75",
		user="root",
		connect_kwargs={"key_filename":keyfileloc}
	) as c:
		c.run("service httpd restart")
		c.run("systemctl status httpd.service")

@task
def installbasic(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":keyfileloc}) as f:
		f.run("yum install openssh-server -y")
		f.run("yum install php python3 node npm -y")

@task
def geterrorlogs(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":keyfileloc}) as f:
		with f.cd(env.applogs):
			f.run("cat error.log >> errors.txt")
			f.get("/var/www/html/icharbeitezuhaus.com/logs/errors.txt","./errors.txt")
                        
@task
def upload(ctx):
	run("echo this is not drilling > meme.txt")
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":keyfileloc}) as f:
		with f.cd(env.applogs):
			f.put("/Users/dexio/Desktop/soldier/meme.txt","/var/www/html/icharbeitezuhaus.com/logs/")

@task
def restart(ctx):
	reboot()

@task 
def main(ctx):
	pass
