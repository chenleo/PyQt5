#!/usr/bin/env python
# encoding: utf-8
# part1.py in PyQt5
# Created by maverick on 2018-12-06, 21:26
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: part1.py
@time: 2018-12-06 21:26
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class AddressBook(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(AddressBook, self).__init__(parent = parent)

        nameLabel: QtWidgets.QLabel = QtWidgets.QLabel("Name:")
        self.nameLine: QtWidgets.QLineEdit = QtWidgets.QLineEdit()

        addressLabel: QtWidgets.QLabel = QtWidgets.QLabel("Address:")
        self.addressText: QtWidgets.QTextEdit = QtWidgets.QTextEdit()

        mainLayout: QtWidgets.QGridLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Simple Address Book")




if __name__ == '__main__':
    app:QtWidgets.QApplication =  QtWidgets.QApplication(sys.argv)
    addressBook: AddressBook = AddressBook()
    addressBook.show()

    sys.exit(app.exec_())