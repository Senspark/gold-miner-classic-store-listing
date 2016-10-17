#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = 'supply -j ../../../THANH-Google-Play-Android-Developer-b8ad63fc6d69.json -a beta -p com.senspark.goldminerclassic --skip_upload_apk true --skip_upload_images true --skip_upload_screenshots true'
print cmd
os.system(cmd)