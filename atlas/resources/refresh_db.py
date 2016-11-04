import os

os.system('../.././manage.py loaddata accounts > accounts.json')
os.system('../.././manage.py loaddata projects > projects.json')
os.system('../.././manage.py loaddata web > web.json')
