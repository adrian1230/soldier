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

@task
def inspect(ctx):
	with conn(
		"172.105.4.75",
		user="root",
		connect_kwargs={
			"key_filename": ""
		}
		) as c:
		with c.cd("/var/www/html/icharbeitezuhaus.com/public_html/"):
			c.run("ls -la")
