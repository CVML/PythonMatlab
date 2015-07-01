# PythonMatlab

## Installation:

### Set up path

In order for matlab to find Python 3, we must add it to Matlab's path. This is done via startup.m. Startup.m is found in the userpath location which can be found by typing:

```
>> userpath

ans =

/Users/(user)/Documents/MATLAB:
```

In this case, edit `/Users/(user)/Documents/MATLAB/startup.m` by adding these lines:

oldpath = getenv('PATH');
newpath = ['(path to python3):' oldpath];
setenv('PATH', newpath);

### (Next)
