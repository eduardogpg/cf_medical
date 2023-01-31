from fabric.api import run
from fabric.api import env, cd, prefix

env.hosts =  ['104.236.4.54']
env.user = 'eduardo'
env.key_filename = '/home/eduardo/.ssh/id_ed25519.pub'


def deploy():
    with cd('project'):
        with cd('cf_medical'):
            with prefix('source env/bin/activate'):
                run('git pull')

                run('sudo systemctl restart django', )
                run('sudo systemctl restart nginx')