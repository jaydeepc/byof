from json import dumps
import os

from pip._vendor.distlib.compat import raw_input
from termcolor import colored
from .base import Base


class Initialise(Base):

    def run(self):
        current_path = os.getcwd()
        try:
            def make_dir(dir_name):
                os.makedirs(current_path+dir_name)
                os.chdir(current_path+dir_name)
                open("__init__.py","w")
            make_dir("/Test")
            make_dir("/Client")
            make_dir("/Report")
            make_dir("/Client/models")
            make_dir("/Client/models/Request")
            make_dir("/Client/models/Response")
            print (colored('Building your folder structure .... ', 'magenta'))
            print (colored('Framework is created!', 'green'))

        except OSError, e:
            if (e.errno == 17):
                print(colored("fatal: Folders already exists and is not an empty directory.",'red'))


