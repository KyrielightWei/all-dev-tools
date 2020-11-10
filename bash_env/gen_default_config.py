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
              'TERM':'alacritty-direct',
              'RUSTUP_DIST_SERVER':'https://mirrors.tuna.tsinghua.edu.cn/rustup',
              'GOPROXY':'https://goproxy.cn'
        },
    'PATH' : {
            'git':'$ALL_DEV_ENV/git-install/bin/',
            'clang_llvm':'$ALL_DEV_ENV/clang+llvm/bin/',
            'clangd':'$ALL_DEV_ENV/clang+llvm/bin/',
            'nvim':'$ALL_DEV_ENV/',
            'gcc':'',
            'go':'$ALL_DEV_ENV/bin/',
            'nodejs':'$ALL_DEV_ENV/node_js/bin/',
            'ctags':'$ALL_DEV_ENV/ctags-install/bin/',
            'gtags':'$ALL_DEV_ENV/gtags-install/bin/'
        }

}

with open(config_path,'w') as fw:
    json.dump(dict,fw,indent=4)

