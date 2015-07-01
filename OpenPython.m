function  [data_processed]= Data_Analysis()

% - A function that calls the python program data_analysis.py - 

% The input arguments will be the name of the files we want to analyse

% [filename,pathname] = uigetfile('*.m','Select the MATLAB code file');
%filename='nas/nas-li20-pm00/E217/2015/20150504/E217_16808/E217_16808.mat'

%data=E200_load_data(filename);

system('python');

import basic_data_analysis.py as bd

% needs to be in the PyMa directory to work...  

data_processed=load('struct_test2.mat') ;



end

