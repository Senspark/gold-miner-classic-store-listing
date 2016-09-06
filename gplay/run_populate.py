#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../store-listing-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 1f8JS4pz6xhCTWdnqNUmpbYyvvt95dBUqmf6xj_rG2a0 -customized-metadata-path ../src/gplay/metadata"
print cmd
os.system(cmd)
