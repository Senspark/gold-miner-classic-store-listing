#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../app-stores-toolkit/populate.py metadata -platform ios -prj-path . -data-file-path ../src/goldminer-metadata-translate.xlsx -customized-metadata-path ../src/itunes/metadata"
print cmd
os.system(cmd)
