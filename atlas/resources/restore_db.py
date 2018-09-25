import os


# Change to the project's main directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(project_dir)

# Restore this environment's database back to the original demo state
print('[Running Data Refresh]')
print('creating web content..')
os.system('./manage.py loaddata atlas/resources/data/web.json')
print('creating accounts..')
os.system('./manage.py loaddata atlas/resources/data/accounts.json')
print('creating projects..')
os.system('./manage.py loaddata atlas/resources/data/projects.json')
print('creating users..')
os.system('./manage.py loaddata atlas/resources/data/users.json')
