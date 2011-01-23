#!/usr/bin/env python
# fichier principal

import subprocess, sys

if len(sys.argv) < 2:
    print 'Usage: python start.py [option] <directory>'
    sys.exit(1)

#Lancement de qjackctl
#qjackctl = subprocess.Popen("qjackctl")
#qjackctl.poll()

#Lancement de sooperlooper
sooperlooper = subprocess.Popen("sooperlooper")
sooperlooper.poll()

awesomix = subprocess.Popen([sys.executable, 'awesomix/test.py'] + sys.argv[1:])
awesomix.wait()
