% ===============================
% Get home folder
% ===============================
home = getenv('HOME');

% ===============================
% Get E200_data path
% ===============================
path = fullfile(home, 'testbed', 'E200_DRT', 'E200_data');

% ===============================
% Add E200_data to path
% ===============================
addpath(path);

% ===============================
% Load a data file
% ===============================
datapath = 'nas/nas-li20-pm00/E200/2015/20150605/E200_17902/E200_17902.mat'
data = E200_load_data(datapath);

% ===============================
% Call python analysis script
% (example.py)
% ===============================
data = OpenPython('example.py', datapath)
