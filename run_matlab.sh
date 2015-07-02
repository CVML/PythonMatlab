#!/usr/bin/env bash

export DYLD_INSERT_LIBRARIES=/opt/local/lib/libgcc/libgfortran.3.dylib:/opt/local/Library/Frameworks/QtGui.framework/Versions/4/QtGui:/opt/local/Library/Frameworks/QtCore.framework/Versions/4/QtCore:/opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/PIL/.dylibs/libtiff.5.dylib
/Applications/MATLAB_R2015a.app/bin/matlab
