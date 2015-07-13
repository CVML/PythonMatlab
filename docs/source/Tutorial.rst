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

For each filed, we will first describe what is its general purpose, and what it does in our example.

-------------
run_matlab.py
-------------
This program runs matlab with the right library, according to your os, in order to avoid conflicts between the python and matlab standard libraries. Currently, the Linux and Darwin os are supported.

----------
example.m
----------
This file loads in the workspace a bunch of data that comes from the specified folder. In our case, it is E217_16808.mat files. Note that we use a specific way to load data, with "E200_load_data" which is required because of the nature of the files we load. (with ordinary files, you can just use "load).

Then we call the "OpenPython" script, giving to it as input "example.py", the "datapath" of the files we want to analyse and the "data".

----------
OpenPython
----------
This is where Matlab calls Python.

It calls the execution of the pythonscript passed as input, along with the data that must be analysed. It loads the created file in the Workspace of Matlab.

Note that the 
"data_processed=load('struct_test2.mat');" line, which loads directly the given file, namely struct_test2.mat in the Workspace, will only work if thisvery file is created or edited in the pythonscript.

----------
example.py
----------
This file runs the python analysis of the data passed as input.

It then loads the output to Matlab using the function LoadinMatlab from the basic_data_analysis python script.

Let us describe more specifically what this file does : 

It first gets the given file from command line, here E217_16828.mat (remember we loaded it in example.m ?). It loads it with the E200.E200.load_data command. 

It then gets the uids associated with each images, and creates the (still empty) output. It then threshold the images : here the two ouputs, output_260 and output_300 are arrays that indicate for each image if the value of the central pixel is above a certain threshold.

In order to transfer it to Matlab, it creates a dictionary : formatlab, and files it with : the uids and the output. This dictionary is then loaded in Matlab via bda.LoadinMatlab.

---------------------
basic_data_analysis.py
----------------------
This is the core of our program. Being given a dictionary of data coutaining an array of uids, and arrays of scalars, vectors or images, it stores them in a dictionary that separate them by types, associating the uid with every item.

Note that it is requested that the "keys" of the dictionary that is being processed, here formatlab, need to start with "my" for every data array", and that the uid array need to be called "muuid".
Note also that all these array needs to be of the same size (in order to associate an uid with every data).

The different parts of the dictionary are created dynamically.

In our example, since we only have two outputs that are arrays of scalars, only the scalar part will be created.

The io.savemat transfer this python dictionary to a matlab structure, called here 'struct_test2.mat'.


