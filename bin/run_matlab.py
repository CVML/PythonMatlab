#!/usr/bin/env python3

import platform
import PythonMatlab as pm

Osname = platform.system()

if Osname == 'Linux':
    print('ok')
    
elif Osname == 'Darwin':
    print('ok2')
