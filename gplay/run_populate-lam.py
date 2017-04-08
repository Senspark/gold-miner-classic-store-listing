#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../store-listing-toolkit/populate-v3.py metadata -platform android -prj-path . -sheet 1Jo1G8iCpBKBwXewY4V-8KFOBbkZtNSYn81RaTnNf2f8 -customized-metadata-path ../src/gplay/metadata"

print cmd
os.system(cmd)
