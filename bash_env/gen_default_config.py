import os
import sys
from configparser import ConfigParser

# @param config_path
import json

if(len(sys.argv) < 2):
    config_path="./ADT_default.json"
else:
    config_path=sys.argv[1]

dict ={
    'Control' : {
            'message':'All Dev Tools Loaded'
        },
    'ENV' : {
              'CXX':'clang++',
              'CC':'clang',
              'RUSTUP_DIST_SERVER':'https://mirrors.tuna.tsinghua.edu.cn/rustup',
              'GOPROXY':'https://goproxy.cn',
	          'LANG' : 'C.UTF-8',
              'LC_ALL': 'C.UTF-8'
        },
    'PATH' : {

        }

}

with open(config_path,'w') as fw:
    json.dump(dict,fw,indent=4)

