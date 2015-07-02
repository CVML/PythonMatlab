function [data_processed]= Data_Analysis(pythonscript, filename)

% - A function that calls the python program data_analysis.py - 

% The input arguments will be the name of the files we want to analyse

command = ['python3 ' pythonscript ' ' filename]
system(command);

% needs to be in the PyMa directory to work...  

data_processed=load('struct_test2.mat');

end
