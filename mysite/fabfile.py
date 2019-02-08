from fabric.api import env, run, cd

env.hosts = ['47.92.135.212']
env.user = 'root'
env.password = '!Yang151750'


def deploy():
    with cd('/home/Blogger'):
        run('ls')
        with cd('/home/mysite_uwsgi'):
            run('ls')
#            run('uwsgi --reload master.pid')
