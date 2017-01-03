import datetime
import os
import socket


# Change to the project's main directory so we can use manage.py
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(project_dir)

# Create a backup log so we have a recording of when and from where the backup took place
logfile = open('backup.log', 'w')
logfile.write('Last backup: ')
logfile.write(str(datetime.datetime.now()))
logfile.write(' from ' + str(socket.gethostname()) + '\n')

# Only backup the following apps
print('backing up web...')
os.system('./manage.py dumpdata web > web.json')
os.system('mv web.json atlas/resources/data/web.json')

print('backing up accounts...')
os.system('./manage.py dumpdata accounts > accounts.json')
os.system('mv accounts.json atlas/resources/data/accounts.json')

print('backing up projects...')
os.system('./manage.py dumpdata projects > projects.json')
os.system('mv projects.json atlas/resources/data/projects.json')

logfile.close()
os.system('mv backup.log atlas/resources/data/backup.log')

# Commit the backup files into the repository
# commit_message = 'Backing up database tables from ' + str(socket.gethostname())
# os.system('git commit -m "' + commit_message + '" -- atlas/resources/data/backup')
# os.system('git push origin')

# TODO: Create an endpoint to call this file and add a button to my project management UI so that backups can be
# TODO: created with the push of a button.
