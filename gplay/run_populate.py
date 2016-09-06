#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

<<<<<<< HEAD
cmd = "../../store-listing-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 1f8JS4pz6xhCTWdnqNUmpbYyvvt95dBUqmf6xj_rG2a0 -customized-metadata-path ../src/gplay/metadata"
=======
cmd = "../../../app-stores-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 1f8JS4pz6xhCTWdnqNUmpbYyvvt95dBUqmf6xj_rG2a0 -customized-metadata-path ../src/gplay/metadata"

>>>>>>> 14b89d4889234cb9deae4cc02fa9309d0206d4a6
print cmd
os.system(cmd)
