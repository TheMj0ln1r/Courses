#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1],"r") as files:
    for file in files.readlines():
        oldname = file.strip()
        newname = file.strip().replace("jane","jdoe")
        subprocess.run(["mv",".."+oldname,".."+newname])

