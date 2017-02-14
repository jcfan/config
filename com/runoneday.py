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
    cmd='doy %d %d %d>tmp '%(year,month,day)
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



def gweek(year,doy):
    cmd='doy %d %d >tmp '%(year,doy)
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

p = ArgumentParser(usage='python runoneday.py -year 2016 -doy 305', description='')  
p.add_argument('-doy',  type=int, help='input link day of year')  
p.add_argument('-year',  type=int, help='input link  year')  
  
args = p.parse_args()  
  

if not args.doy or not args.year:
    print 'input year doy error'
    sys.exit(1)


doy=args.doy
year=args.year
week,dow=gweek(year,doy)

flag=1

cmd='python ../com/linkrfile.py -year %04d -doy %03d -r -n  -sp3'%(year,doy)
exe(cmd,flag)
cmd='links.day %04d %03d orbd'%(year,doy)
exe(cmd,flag)
cmd='sh_upd_stnfo -files *.%02do'%(year%100)
exe(cmd,flag)
cmd='sh_makexp -expt orbd -orbt igsf -yr %04d -doy %03d -sess 99 -srin -nav brdc%03d0.%02dn -sinfo 30 00 00 2880'%(year,doy,doy,year%100)
exe(cmd,flag)
cmd='sh_sp3fit -f igs%04d%1d.sp3 -o igsf'%(week,dow)
exe(cmd,flag)
cmd='sh_check_sess -sess %03d -type gfile -file gigsf%1d.%03d'%(doy,year%10,doy)
exe(cmd,flag)
cmd='makej brdc%03d0.%02dn jbrdc%1d.%03d'%(doy,year%100,year%10,doy)
exe(cmd,flag)
cmd='sh_check_sess -sess %03d -type jfile -file jbrdc%1d.%03d'%(doy,year%10,doy)
exe(cmd,flag)
cmd='makex orbd.makex.batch'
exe(cmd,flag)
cmd='fixdrv dorbd%1d.%03d'%(year%10,doy)
exe(cmd,flag)
cmd='csh borbd%1d.bat'%(year%10)
exe(cmd,flag)

