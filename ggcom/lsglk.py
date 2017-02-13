#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 jcfan <cfan89@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import sys
import os
from argparse import ArgumentParser  

def exe(cmd,flag=1):
    print cmd
    if flag:
        os.system(cmd)

def ymd2gw(year,month,day):
    cmd='doy %d %d %d > tmp '%(year,month,day)
    os.system(cmd)
    fid=open('tmp','r')
    for i,line in enumerate(fid):
        if i == 1:
            week=int(line[8:14])
            dow=int(line[26:29])
    fid.close()
    cmd='rm tmp'
    os.system(cmd)
    return (week,dow)

def main():
    p = ArgumentParser(usage='python lsglk.py ', description='')  
    p.add_argument('-dir',   help='direction')  
    args = p.parse_args()  
    path=args.dir
    fnames=os.listdir(path)
    for fn in fnames:
        if fn[-3:]=='glx':
            #print os.path.join(path,fn)
            #print int(fn[1:3]),int(fn[3:5]),int(fn[5:7])
            week,sow=ymd2gw(int(fn[1:3]),int(fn[3:5]),int(fn[5:7]))
            nfn='gk%04d%1d.gld'%(week,sow)
            cmd='ls %s > %s' %(os.path.join(path,fn),nfn)
            exe(cmd)
            
if __name__ == "__main__":
    main()
