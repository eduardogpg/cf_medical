from fabric.api import run
from fabric.api import env, cd, prefix, sudo

env.hosts = ['104.236.4.54']
env.user = 'eduardo'
env.key_filename = '/home/eduardo/.ssh/id_ed25519.pub'

def deploy():
    print('>>> Nos contamos a nuestro servidor remoto.')

    with cd('project'):
        with cd('cf_medical'):
            run('git pull')

            with prefix('source env/bin/activate'):
                run('pip install -r requirements.txt')
                
                run('python manage.py migrate')
                run('python manage.py collectstatic --noinput')
    
    sudo('sudo systemctl restart django')
    sudo('sudo systemctl restart nginx')

          
