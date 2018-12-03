#!/usr/bin/env python
# encoding: utf-8
# t1.py in PyQt5
# Created by maverick on 2018/12/3, 2:45 PM
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t1.py
@time: 2018/12/3 2:45 PM
"""

# PyQt5 tutorial 1

import sys
from PyQt5 import QtWidgets

# Step 1: Init
app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)

# Step 3: Do the major job
hello: QtWidgets.QPushButton = QtWidgets.QPushButton("Hello World!")
hello.resize(100, 30)

# Step 1+: Shut Down Logic
hello.show()
sys.exit(app.exec_())