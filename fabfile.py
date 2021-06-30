from fabric import Connection as conn
from invoke import task, run, env, sudo
import numpy as np
import os, sys
import json

env.ip = "172.105.4.75"
env.user = "root"
env.parentdirectory = '/var/www/html'
env.appdirectory = '{}/icharbeitezuhaus.com'.format(env.parentdirectory)
env.applogs = '{}/logs'.format(env.appdirectory)
env.appsrc = '{}/public_html'.format(env.appdirectory)

keyfileloc = "../../.ssh/id_rsa.pub"

@task
def update(ctx):
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
		f.run("yum update -y")

@task
def hosttypelocal(ctx):
	run('uname -s')

@task
def hosttyperemote(ctx):
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
		f.run('uname -s')

@task
def diskspaceremote(ctx):
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
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
		env.ip,
		user=env.user,
		connect_kwargs={"key_filename":keyfileloc}
	) as c:
		c.run("service httpd restart")
		c.run("systemctl status httpd.service")

@task
def installbasic(ctx):
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
		f.run("yum install openssh-server git -y")
		f.run("yum install php python3 node npm -y")

@task
def geterrorlogs(ctx):
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
		with f.cd(env.applogs):
			f.run("cat error.log >> errors.txt")
			f.get("/var/www/html/icharbeitezuhaus.com/logs/errors.txt","./errors.txt")
                        
@task
def upload(ctx):
	run("echo this is not drilling > meme.txt")
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
		with f.cd(env.applogs):
			f.put("/Users/dexio/Desktop/soldier/meme.txt","/var/www/html/icharbeitezuhaus.com/logs/")

@task
def restart(ctx):
	reboot()

@task 
def main(ctx):
	pass

@task
def github(ctx):
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
		with f.cd(env.appsrc):
			if os.path.exists(".git") != True:
				f.run("git init; git config --global user.name 'adrian1230'; git config --global user.email 'yourgmail@gmail.com'")
			f.run("cat ~/.gitconfig")
			f.run("git add .; git commit -m 'adrian@dexio'; clear; ls")

@task
def removesrcd(ctx):
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
		with f.cd(env.appsrc):
			f.run("rm -rf * -y")

@task
def removeparentd(ctx):
	with conn(env.ip,user=env.user,connect_kwargs={"key_filename":keyfileloc}) as f:
		with f.cd(env.parentdirectory):
			f.run("rm -rf * -y")
