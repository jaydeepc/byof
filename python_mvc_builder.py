import os

current_path = raw_input("Please enter the current path(/user/...):")
if  os.path.exists(str(current_path)):
    current_path = current_path
else:
    current_path = os.getcwd() 
def make_dir(current_path, dir_name):
    os.makedirs(current_path+dir_name)
    os.chdir(current_path+dir_name)
    open("__init__.py","w")

make_dir(current_path,"/Test")
make_dir(current_path,"/Client")
make_dir(current_path,"/Report")
make_dir(current_path,"/Client/models")
make_dir(current_path,"/Client/models/Request")
make_dir(current_path,"/Client/models/Response")
