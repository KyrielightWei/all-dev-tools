import os
import sys
import json
config_default_path = os.path.realpath(os.path.dirname(__file__))+"/ADT_default.json"
#  print(config_default_path)
config_user_path = os.getenv('HOME')+"/ADT_user.json"

config_dict={}

user_dict={}

def load(fpath):
    if(os.path.exists(fpath) == False):
        print("error! Not found " + fpath)
        return {}
    with open(fpath,'r') as f:
        data = json.load(f)
        return data

config_dict = load(config_default_path)
user_dict = load(config_user_path)
config_dict.update(user_dict)

com_str = ""

for (key,value) in config_dict.items():
    if(key == "PATH"):
        for ( k , v ) in value.items():
            if(len(v) > 0) :
                path_str = "export PATH=\"" + v + ":$PATH\"" 
                #  print(path_str)
                com_str += path_str + " && " 
    if(key == "ENV"):
        for ( k , v ) in value.items():
            if(len(v) > 0) :
                env_str = "export " + k + "=\"" + v +"\""
                #  print(env_str)
                com_str += env_str + " && "
    if(key == "Control"):
        for (k , v ) in value.items():
            if(k=="message" and len(v) > 0) :
                com_str += "echo " + v + " && "

print(com_str.rstrip(" && "))


