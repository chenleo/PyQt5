#!/usr/bin/env python
# encoding: utf-8
# t9.py in PyQt5
# Created by maverick on 2018-12-06, 10:39
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t9.py
@time: 2018-12-06 10:39
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class LCDRange(QtWidgets.QWidget):
    valueChanged = QtCore.pyqtSignal(int)

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        lcd: QtWidgets.QLCDNumber = QtWidgets.QLCDNumber(2)

        self.slider: QtWidgets.QSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(0, 99)
        self.slider.setValue(0)

        self.slider.valueChanged.connect(lcd.display)
        self.slider.valueChanged.connect(self.valueChanged)

        layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(self.slider)

        self.setLayout(layout)
        self.setFocusProxy(self.slider)

    def value(self):
        return self.slider.value()

    @QtCore.pyqtSlot(int)
    def setValue(self, value: int):
        self.slider.setValue(value)

    def setRange(self, minValue: int, maxValue: int):
        if minValue < 0 or maxValue > 99 or minValue > maxValue:
            QtCore.qWarning(f"LCDRange::setRange({minValue}, {maxValue})\n"
                    "\tRange must be 0 .. 99\n"
                    "\tand minValue must not be greater than maxValue.")
            return

        self.slider.setRange(minValue, maxValue)

class CannonField(QtWidgets.QWidget):
    angleChanged = QtCore.pyqtSignal(int)

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent = None)

        self.currentAngle = 45
        self.setPalette(QtGui.QPalette(QtGui.QColor(250, 250, 200)))
        self.setAutoFillBackground(True)

    def angle(self):
        return self.currentAngle

    @QtCore.pyqtSlot(int)
    def setAngle(self, angle: int):
        if angle < 5:
            angle = 5
        if angle > 70:
            angle = 70
        if self.currentAngle == angle:
            return
        self.currentAngle = angle
        self.update()
        self.angleChanged.emit(self.currentAngle)

    def paintEvent(self, event: QtGui.QPaintEvent):   # over write function
        painter: QtGui.QPainter = QtGui.QPainter(self)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.blue)

        painter.translate(0, self.rect().height())
        painter.drawPie(QtCore.QRect(-35, -35, 70, 70), 0, 90 * 16)
        painter.rotate(-self.currentAngle)
        painter.drawRect(QtCore.QRect(33, -4, 15, 8))

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent = parent)

        quit: QtWidgets.QPushButton = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18,
                                 QtGui.QFont.Bold))

        quit.clicked.connect(QtWidgets.qApp.quit)

        angle: LCDRange = LCDRange()
        angle.setRange(5, 70)

        cannonField: CannonField = CannonField()

        angle.valueChanged.connect(cannonField.setAngle)
        cannonField.angleChanged.connect(angle.setValue)

        gridLayout: QtWidgets.QGridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(angle, 0, 0)
        gridLayout.addWidget(quit, 1, 0)
        gridLayout.addWidget(cannonField, 0, 1, 2, 1)
        gridLayout.setColumnStretch(1, 10)
        self.setLayout(gridLayout)

        angle.setValue(60)
        angle.setFocus()

if __name__ == '__main__':
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    widget: MyWidget = MyWidget()
    widget.setGeometry(100, 100, 500, 355)
    widget.show()

    sys.exit(app.exec_())