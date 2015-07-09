########
Tutorial
########

In this tutorial, we will run the example file and try to understand step by step what has happened.

============
Instructions
============

First, go to the PythonMatlab directory. Inside it, you can find a bunch of files and directories. Go to the bin directory. You will find a run_matlab.py. Run it, using
$./run_matlab.py
This should open Matlab.
In Matlab, move up to the PythonMatlab directory with, for instance : 
$cd ..
Type "example", press Enter
You will see various instructions in the Command Window, and the creation of four variables in the Workspace : data, datapath, home, path.

============
Explanations
============

-------------
run_matlab.py
-------------
This program runs matlab with the right library, according to your os, in order to avoid conflicts between the python and matlab standard libraries. Currently, the Linux and Darwin os are supported.

----------
example.m
----------
This file loads in the workspace a bunch of data that comes from the specified folder. In our case, it is E217_16808.mat files. Note that we use a specific wat to load data, with "E200_load_data" which is required because of the nature of the very files we load.

Then we call the "OpenPython" script, giving to it as input "example.py, the datapath of the files we want to analyse and the data.

----------
OpenPython
----------
