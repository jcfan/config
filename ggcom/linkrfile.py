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

p = ArgumentParser(usage='linkrfile.py -year 2016 -doy 301 -r -n -sp3', description='link files from ../rinex ../brdc ../igs')  
p.add_argument('-year',  type=int, help='input link year')  
p.add_argument('-doy',  type=int, help='input link day of year')  
p.add_argument('-r', type=int,nargs='?',default=0,const=1, help='whether link rinex observation files')  
p.add_argument('-n', type=int,nargs='?', default=0, const=1,help='whether link navigation files')  
p.add_argument('-sp3', type=int,nargs='?', default=0,const=1, help='whether link sp3 orbit files')  
  
args = p.parse_args()  
  

if not args.doy or not args.year:
    print 'input year doy error'
    sys.exit(1)

if args.r+args.n+args.sp3 == 0:
    args.r=1
    args.n=1
    args.sp3=1
    

doy=args.doy
year=args.year
if args.r:
    cmd='ln -s ../rinex/*%03d0.%02do . '%(doy,year%100)
    print cmd
    os.system(cmd)
    

if args.n:
    cmd='ln -s ../brdc/brdc%03d0.%02dn . '%(doy,year%100)
    print cmd
    os.system(cmd)

if args.sp3:
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
    cmd='ln -s ../igs/*%04d%1d.sp3 . '%(week,dow)
    os.system(cmd)
    print cmd

