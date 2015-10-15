import os
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--new-project', type=str, dest='project_name')


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

def make_project_directory(directory):
    path = os.getcwd() + '/' + directory
    if not os.path.exists(path):
        print "Create project root folder -- OK"
        os.makedirs(path)
        return path
    else:
        raise Exception('Directory already exists')

if __name__ == '__main__':
    args = parser.parse_args()

    root = make_project_directory(args.project_name)
    get_requirements(root)
