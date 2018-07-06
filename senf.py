import argparse
import os, os.path

from config.senfconfig import SenfConfig

def change_directory(path=None):
    if path is None:
        return None

    print(path)

    if not os.path.exists(path):
        print("os path does not exist")
        return None


    print(os.getcwd())
    os.chdir(path)
    print(os.getcwd())
    return os.getcwd()


parser = argparse.ArgumentParser()
parser.add_argument("config_file")
args = parser.parse_args()


default_config = SenfConfig(args.config_file)
default_config.read_config_file()


default_config_name = default_config.get_default_study()
print(default_config_name)

default_path = default_config.get_path()
user_path = os.path.expanduser(default_path)
abs_default_path = os.path.abspath(user_path)


print(default_path)

if not change_directory(abs_default_path):
    print("dir does not exist")


