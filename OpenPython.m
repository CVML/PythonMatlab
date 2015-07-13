function [data_processed]= OpenPython(pythonscript, filename)

%% This file calls python from Matlab. It takes as input : 
% 'pythonscript' : the name of the python script you want to use to make
% the analysis
% 'filename' : the name of the Matlab files you want to analyse
% 'data' : 

command = ['python3 ' pythonscript ' ' filename]
system(command);

data_processed=load('struct_test2.mat');
% This loads the processed data in the Workspace.




end
