import os

# Change to the project's main directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(project_dir)

# Only refresh this environment if the data refresh flag is turned on.
# DO NOT RUN THIS IN PRODUCTION!!
if os.environ.get('DATA_REFRESH', False):
    # Drop the existing data
    # print('[Flushing Data]')
    # os.system('./manage.py flush --noinput')

    # Restore this environment's database back to the development/stage state
    print('[Running Data Refresh]')
    print('creating web content..')
    os.system('./manage.py loaddata atlas/resources/data/web.json')
    print('creating accounts..')
    os.system('./manage.py loaddata atlas/resources/data/accounts.json')
    print('creating projects..')
    os.system('./manage.py loaddata atlas/resources/data/projects.json')
