#!/usr/bin/env python
# encoding: utf-8
# part2.py in PyQt5
# Created by maverick on 2018-12-06, 21:37
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: part2.py
@time: 2018-12-06 21:37
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Dict, List, Union

class SortedDict(Dict):
    class Iterator(object):
        def __init__(self, sorted_dict: Dict):
            self.__dict: Dict = sorted_dict
            self.__keys: List = sorted(self.__dict.keys())
            self.__nr_items: int = len(self.__keys)
            self.__idx: int = 0

        def __iter__(self):
            return self

        def next(self) -> Union:
            if self.__idx >= self.__nr_items:
                raise StopIteration

            key = self.__keys[self.__idx]
            value = self.__dict[key]
            self.__idx += 1

            return key, value

        __next__ = next

    def __iter__(self):
        return SortedDict.Iterator(self)

    iterkeys = __iter__

class Addressbook(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(Addressbook, self).__init__(parent=parent)

        self.contacts: SortedDict = SortedDict()
        self.oldName: str = ""
        self.oldAddress: str = ""

        nameLabel: QtWidgets.QLabel = QtWidgets.QLabel("Name:")
        self.nameLine: QtWidgets.QLineEdit = QtWidgets.QLineEdit()
        self.nameLine.setReadOnly(True)

        addressLabel: QtWidgets.QLabel = QtWidgets.QLabel("Address:")
        self.addressText: QtWidgets.QTextEdit = QtWidgets.QTextEdit()
        self.addressText.setReadOnly(True)

        self.addButton: QtWidgets.QPushButton = QtWidgets.QPushButton("&Add")
        self.addButton.show()  ## ??
        self.submitButton: QtWidgets.QPushButton = QtWidgets.QPushButton("&Submit")
        self.submitButton.hide()
        self.cancelButton: QtWidgets.QPushButton = QtWidgets.QPushButton("&Cancel")
        self.cancelButton.hide()

        self.addButton.clicked.connect(self.addContact)  # not implement, what type?
        self.submitButton.clicked.connect(self.submitContact)  # not implement
        self.cancelButton.clicked.connect(self.cancel)   # not implement

        buttonLayout1: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        buttonLayout1.addWidget(self.addButton, QtCore.Qt.AlignTop)
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addWidget(self.cancelButton)
        buttonLayout1.addStretch()

        mainLayout: QtWidgets.QGridLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(addressLabel, 1, 0, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 1, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)

        self.setLayout(mainLayout)
        self.setWindowTitle("Simple Address Book")

    def addContact(self):   # work like a slot
        self.oldName: str = self.nameLine.text()
        self.oldAddress: str = self.addressText.toPlainText()

        self.nameLine.clear()
        self.addressText.clear()

        self.nameLine.setReadOnly(False)
        self.nameLine.setFocus(QtCore.Qt.OtherFocusReason)
        self.addressText.setReadOnly(False)

        self.addButton.setEnabled(False)
        self.submitButton.show()
        self.cancelButton.show()

    def submitContact(self):
        name: str = self.nameLine.text()
        address: str = self.addressText.toPlainText()

        if name == "" or address == "":
            QtWidgets.QMessageBox.information(self, "Empty Field!",
                                              "Please enter a name and address.")
            return

        if name not in self.contacts:
            self.contacts[name] = address
            QtWidgets.QMessageBox.information(self, "Add Successful!",
                                              f"\"{name}\" has been added to your address book.")
        else:
            QtWidgets.QMessageBox.information(self, "Add Failed!",
                                              f"Sorry, \"{name}\" is already in your address book.")
            return

        if not self.contacts:
            self.nameLine.clear()
            self.addressText.clear()

        self.nameLine.setReadOnly(True)
        self.addressText.setReadOnly(True)
        self.addButton.setEnabled(True)
        self.submitButton.hide()
        self.submitButton.hide()

    def cancel(self):
        self.nameLine.setText(self.oldName)
        self.nameLine.setReadOnly(True)

        self.addressText.setText(self.oldAddress)
        self.addressText.setReadOnly(True)

        self.addButton.setEnabled(True)
        self.submitButton.hide()
        self.cancelButton.hide()


if __name__ == '__main__':
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)

    addressBook: Addressbook = Addressbook()
    addressBook.show()

    sys.exit(app.exec_())