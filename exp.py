#!/usr/bin/env python

import subprocess
from worker import worker

exp = worker()

for arg1 in [0,1]:
    for arg2 in [2,3]:
        cmd = 'python test_repeater.py %d %d'%(arg1,arg2)
        outfile = "results/%d-%d.txt"%(arg1,arg2)
        exp.add(cmd, outfile)
        exp.run()
