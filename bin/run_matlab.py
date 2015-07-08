#!/usr/bin/env python3

import platform
import PythonMatlab as pm
import subprocess
import shlex
import os

system = platform.system()

if system == 'Linux':
    pass
elif system == 'Darwin':
    os.environ['DYLD_INSERT_LIBRARIES'] = '/opt/local/lib/libgcc/libgfortran.3.dylib:/opt/local/Library/Frameworks/QtGui.framework/Versions/4/QtGui:/opt/local/Library/Frameworks/QtCore.framework/Versions/4/QtCore:/opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/PIL/.dylibs/libtiff.5.dylib'

command = pm.matlabpath()
subprocess.call(shlex.split(command))
