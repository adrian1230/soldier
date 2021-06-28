from fabric import Connection as conn
from invoke import task, run, env, sudo

@task
def update(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}) as f:
		f.run("yum update -y")

@task
def hosttypelocal(ctx):
	run('uname -s')

@task
def hosttyperemote(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}) as f:
		f.run('uname -s')

@task
def diskspaceremote(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}) as f:
		f.run('df')

@task
def diskspacelocal(ctx):
	run('df')

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
		f.run("yum install openssh-server -y")
		f.run("yum install php python3 node npm -y")

@task
def geterrorlogs(ctx):
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}) as f:
		with f.cd("/var/www/html/icharbeitezuhaus.com/logs/"):
			f.run("cat error.log >> errors.txt")
			f.get("/var/www/html/icharbeitezuhaus.com/logs/errors.txt","./errors.txt")
                        
@task
def upload(ctx):
	run("echo this is not drilling > meme.txt")
	with conn("172.105.4.75",user="root",connect_kwargs={"key_filename":"../../.ssh/id_rsa.pub"}) as f:
		with f.cd("/var/www/html/icharbeitezuhaus.com/logs/"):
			f.put("/Users/dexio/Desktop/soldier/meme.txt","/var/www/html/icharbeitezuhaus.com/logs/")

@task
def restart(ctx):
	reboot()

@task 
def main(ctx):
	pass

# if __name__ == "__main__":
# 	pass