# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals
import time
import datetime
import sys
import os
from msp2db.parse import LibraryData
from msp2db.db import create_db

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')

odir = sys.argv[1]  # Output directory
idir = sys.argv[2]  # Input directory, should contain MassBank's contributor sub-directories

db_pth = os.path.join(odir, 'massbank_{}.db'.format(st))

#############################################################
# Create database
#############################################################
create_db(file_pth=db_pth)

#############################################################
# Traverse through all sub-directories
#############################################################
_, dirs, _ = next(os.walk(idir))
for dirname in dirs:
    if dirname.startswith("."):
        continue

    print("#############################################################")
    print('# %s' % dirname)
    print("#############################################################")
    libdata = LibraryData(msp_pth=os.path.join(idir, dirname),
                          db_pth=db_pth,
                          db_type='sqlite',
                          schema='massbank',
                          source=dirname,
                          chunk=10000)
