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
% addpath(path);

% ===============================
% Load a data file
% ===============================
datapath = 'nas/nas-li20-pm00/E217/2015/20150504/E217_16808/E217_16808.mat'
data = E200_load_data(datapath)

% ===============================
% Call python analysis script
% (example.py)
% ===============================
data = OpenPython('example.py', datapath)
