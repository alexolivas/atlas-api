import os

os.system('../.././manage.py dumpdata accounts > accounts.json')
os.system('../.././manage.py dumpdata projects > projects.json')
os.system('../.././manage.py dumpdata web > web.json')

os.system('mv accounts.json data/accounts.json')
os.system('mv projects.json data/projects.json')
os.system('mv web.json data/web.json')
