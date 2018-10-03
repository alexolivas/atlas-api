import os

print('[Running Data Refresh]')

print('Flushing out the existing database..')
os.system('python manage.py flush --noinput')
os.system('python manage.py migrate --fake')

print('Creating demo web data..')
os.system('python manage.py loaddata resources/demo-data/web.json')

print('Creating demo accounts..')
os.system('python manage.py loaddata resources/demo-data/accounts.json')

print('Creating demo projects..')
os.system('python manage.py loaddata resources/demo-data/projects.json')

print('Creating demo users..')
os.system('python manage.py loaddata resources/demo-data/users.json')
