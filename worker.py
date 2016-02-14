#!/usr/bin/env python

import shlex,subprocess
import os.path

class worker:
    def __init__(self):
        self.jobs = []
        self.processes = []
        
    def add(self, command_line, outfile):
        self.jobs.append((shlex.split(command_line), outfile))

    def run(self):
        for arg, filename in self.jobs:
            directory = os.path.dirname(filename)
            if not os.path.exists(directory):
                os.makedirs(directory)
            f = open(filename, "w")
            p = subprocess.Popen( arg, stdout=f)
            self.processes.append((p, f))
            
        for p, f in self.processes:
            p.wait()
            f.close()    

