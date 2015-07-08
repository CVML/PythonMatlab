import glob
import configparser as cg
import os
import platform


def matlabpath():
    # ======================================
    # Load configparser class
    # ======================================
    config = cg.ConfigParser()

    # ======================================
    # Default path for config file is:
    # $HOME/.PythonMatlabrc
    # ======================================
    home = os.environ['HOME']
    configfile = os.path.join(home, '.PythonMatlabrc')

    # ======================================
    # Get default matlabpath
    # ======================================
    system = platform.system()

    if system == 'Darwin':
        matlab_dirs = glob.glob('/Applications/MATLAB_R*.app')
        matlab_dirs.sort(key=os.path.getmtime)
        matlabpath_default = os.path.join(matlab_dirs[0], 'bin/matlab')
    elif system == 'Linux':
        matlabpath_default = os.path.join(home, 'Matlab/bin/./matlab')

    # ======================================
    # Try to read config
    # ======================================
    config.read(configfile)
    matlabpath = config.get('paths', 'matlab', fallback=matlabpath_default)

    return matlabpath
