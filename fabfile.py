from fabric import Connection as conn
from invoke import task, run, env, sudo

@task
def createnewapp(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}) as f:
		with f.cd("/var/www/html/"):
			f.run("npx create-react-app lol")
			with f.cd("/lol/"):
				f.run("cat README.md")

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
def installbasic(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}) as f:
		f.run("yum install openssh-server")
		f.run("yum install php python3 node npm")

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

@task
def geterrorlogs(ctx):
        with conn(
                        "172.105.4.75",
                        user="root",
                        connect_kwargs={
                                "key_filename": "../../.ssh/id_rsa.pub"
                        }
                ) as fd:
                with fd.cd("/var/www/html/icharbeitezuhaus.com/logs/"):
                        fd.run("ls")
                        
