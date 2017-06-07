from json import dumps
import os

from pip._vendor.distlib.compat import raw_input
from termcolor import colored
from .base import Base


class Initialise(Base):

    def run(self):
        current_path = os.getcwd()

        def make_dir(dir_name):
            os.makedirs(current_path+dir_name)
            os.chdir(current_path+dir_name)
            open("__init__.py","w")

        print (colored('Building your folder structure .... ', 'magenta'))

        make_dir("/Test")
        make_dir("/Client")
        make_dir("/Report")
        make_dir("/Client/models")
        make_dir("/Client/models/Request")
        make_dir("/Client/models/Response")

        print (colored('Framework is created!', 'green'))