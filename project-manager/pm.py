import os
import requests

URLS = {}
URLS['requirements'] = 'https://raw.githubusercontent.com/Drieger/utils/master/project-manager/requirements.txt'


def get_requirements(directory):
    u""" Gets requirements from our directory in GitHub. """
    requirements = requests.get(URLS['requirements'])
    # Check if we obtained the file we need
    if requirements.status_code == 200:
        filename = 'requirements.txt'
        # If provided directory does not exists we create it
        directory = directory.rstrip('/')
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Create requirements.txt file
        rf = open(directory + '/' + filename, 'w')
        print "Get requirements.txt -- OK"
        rf.write(requirements.text)
        rf.close()
    # If no file was obtained, we can't proceed
    else:
        print "Error: Couldn't retrieve requirements.txt"


if __name__ == '__main__':
    get_requirements(os.getcwd())
