from fabric import Connection as conn
from invoke import task, run, env, sudo

@task
def helloworld(ctx):
	print("Hello World")

@task
def listdirmain(ctx):
	with conn("172.105.4.75","root",connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}) as f:
		with f.cd("/var/www/html/"):
			f.run("ls -la")

@task
def createnewapp(ctx):
        with conn(
		"172.105.4.75",
		"root",
		connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}
		) as f:
		with f.cd("/var/www/html/"):
			f.run("npx create-react-app myapp")
			with f.cd("/myapp"):
				f.run("ls -la")

@task
def checkstatus(ctx):
	with conn(
		"172.105.4.75",
		user="root",
		connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}
	) as c:
		c.run("service httpd restart")
		c.run("systemctl status httpd.service")

@task
def createfile(ctx):
	run("echo This is it! >> test.txt")

@task
def inspect(ctx):
	with conn(
		"172.105.4.75",
		user="root",
		connect_kwargs={
			"key_filename": "../../.ssh/id_rsa.pub"
		}
		) as c:
		with c.cd("/var/www/html/icharbeitezuhaus.com/public_html/"):
			c.run("ls -la")
