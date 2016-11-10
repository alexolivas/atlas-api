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

# Only backup the following tables
print('backing up web...')
os.system('./manage.py dumpdata web > web_bkp.json')
os.system('mv web_bkp.json atlas/resources/data/backup/web_bkp.json')

print('backing up accounts...')
os.system('./manage.py dumpdata accounts > accounts_bkp.json')
os.system('mv accounts_bkp.json atlas/resources/data/backup/accounts_bkp.json')

print('backing up projects...')
os.system('./manage.py dumpdata projects > projects_bkp.json')
os.system('mv projects_bkp.json atlas/resources/data/backup/projects_bkp.json')

logfile.close()
os.system('mv backup.log atlas/resources/data/backup/backup.log')

# Commit the backup files into the repository
commit_message = 'Backing up database tables from ' + str(socket.gethostname())
os.system('git commit -m "' + commit_message + '" -- atlas/resources/data/backup')
os.system('git push origin')

# TODO: Create an endpoint to call this file and add a button to my project management UI so that backups can be
# TODO: created with the push of a button.
