import configparser as cg
import os

try:

config = configparser.ConfigParser()
home = os.environ['HOME']
configfile = os.path.join(home, '.PythonMatlabrc')
try:
    with open(configfile)
    config.read(configfile)
    matlabpath = config.get('paths', 'matlab')
except:
    with open(configfile)
    try:
        config.add_section('paths')
    except:
        pass

config.set('paths', 'matlab', matlabpath)



