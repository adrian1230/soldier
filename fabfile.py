from fabric import Connection as conn
from invoke import task, run, env, sudo

@task
def helloworld(ctx):
	print("Hello World")

@task
def listdir(ctx):
	run('dir')

@task
def createfile(ctx):
	run("echo 'This is it!' >> test.txt")
