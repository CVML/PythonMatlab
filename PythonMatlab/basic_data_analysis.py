#!/usr/bin/env python3
# -*-coding:UTF-8 -*

# The goal of the program is to analyse data from matlab, and loads it back into matlab
# It should get an UID for every data it treats

import scipy.io as io
import numpy as np
# import sys
import ipdb  # noqa


def LoadinMatlab(data_imported):
    # -Part 1 - This is were we classify the data

    # Get the uuid

    theuuid = data_imported.pop('muuid')
    size = theuuid.size

    data_processed            = {}

    # The output can be of four different types : numbers, vectors, arrays or images

    for x in data_imported:
        if (x.startswith("my")):    # avoid bugs due do loaded variables from  the .py file that can not (and shall not) be stored
            if data_imported[x].shape == (size, ):    # scalars
                if 'scalars' not in data_processed.keys():
                    data_processed['scalars'] = {}
                data_processed['scalars'][x]         = {}
                data_processed['scalars'][x]['data'] = data_imported[x]
                data_processed['scalars'][x]['UID']  = theuuid

            elif data_imported[x].shape == (size, 2):        # vectors
                if 'vectors' not in data_processed.keys():
                    data_processed['vectors'] = {}
                data_processed['vectors'][x]         = {}
                data_processed['vectors'][x]['data'] = data_imported[x]
                data_processed['vectors'][x]['UID']  = theuuid

            elif data_imported[x].shape == (size, 4):        # matrices
                if 'arrays' not in data_processed.keys():
                    data_processed['arrays'] = {}
                data_processed['arrays'][x]         = {}
                data_processed['arrays'][x]['data'] = data_imported[x]
                data_processed['arrays'][x]['UID']  = theuuid

            elif data_imported[x].shape == (size, size):    # images
                if 'images' not in data_processed.keys():
                    data_processed['images'] = {}
                data_processed['images'][x]         = {}
                data_processed['images'][x]['data'] = data_imported[x]
                data_processed['images'][x]['UID']  = theuuid

    # WARNING ! THERE CAN BE NO EMPTY DICTIONARY IF SAVEMAT IS TO WORK
        
    print(data_processed)

    # -Part 3 - This is were we load the data into matlab

    io.savemat('struct_test2.mat', data_processed)
    # with open('struct_test2.mat', 'ab') as f:
    # io.savemat(f, {'newdata3': np.arange(12)})

    # -End of the program:
