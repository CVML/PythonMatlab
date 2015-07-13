#################
ProgramDescription 
#################

This program is purposed to run python analysis of Matlab data easily. It allows the user not to have to write the same analysis program in Matlab.

This program takes as input data from Matlab, an analysing python script, and gives as output the processed data in Matlab.

The two main files are : OpenPython.m and basic_data_analysis.py.

============
OpenPython.m
============

This program calls python from Matlab.

It takes as input the name of the pythonscript that you want to use, the datapath of the files that you want to analyse and the files that you want to analyse.

Once the analysis has ended, it loads the result in the Matlab Workspace.

======================
basic_data_analysis.py
======================

This file coutains a python function called LoadinMatlab that takes as input a dictionary of data and transfers it to Matlab.

To use it : 
* import it in your analysing python script
* at the end of your program, create a dictionary which countains : 
    * the uids of your data, with "muuid" as the name of the key
    * the output, whose keys'names must begin with "my"
* calls the LoadinMatlab function with your dictionary of output(s)

Outputs can be of four different types : scalars, vectors, arrays or images. They will be automatically sorted by types. There will be an array of uids that goes along with every output.

Outputs must be of the same size than uids, which means that there must be an uid for every treated file.


