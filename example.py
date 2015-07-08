#!/usr/bin/env python3
import PythonMatlab.basic_data_analysis as bda
import ipdb                         # noqa
import argparse
import E200
import scisalt as pt                # noqa
import numpy as np

# ===============================
# Get file from command line
# ===============================
parser = argparse.ArgumentParser(description='This is an example script that thresholds images.')
parser.add_argument('datafile',
        help='Path to E200 data file to be loaded.')
arg = parser.parse_args()

# ===============================
# Open file
# ===============================
data = E200.E200_load_data(arg.datafile)

# ===============================
# Load AX_IMG2 images
# ===============================
ax_img2 = data.rdrill.data.raw.images.AX_IMG2
uids = ax_img2.UID[0:5]
# ipdb.set_trace()

# ===============================
# Find number of images
# ===============================
num_images = np.size(uids)

# ===============================
# Create output
# ===============================
output_260 = np.empty(shape=num_images, dtype=object)
output_300 = np.empty(shape=num_images, dtype=object)

# ===============================
# Threshold all of the images
# ===============================
for i, uid in enumerate(uids):
    image = E200.E200_load_images(ax_img2, uid)
    # ipdb.set_trace()
    output_260[i] = (image.images[0] > 260) * 1
    output_300[i] = (image.images[0] > 300) * 1

# ===============================
# Plot first image
# ===============================
# pt.imshow_batch(output, figsize=(32, 24), columns=4, rows=4)
# pt.imshow_slider(images.images[0])

# ===============================
# Transfer output to matlab
# ===============================
formatlab            = {}
formatlab["muuid"]   = uids
formatlab["myth260"] = output_260
formatlab["myth300"] = output_300

bda.LoadinMatlab(formatlab)
