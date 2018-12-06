#!/usr/bin/env python
# encoding: utf-8
# t11.py in PyQt5
# Created by maverick on 2018-12-06, 16:42
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: t11.py
@time: 2018-12-06 16:42
"""

import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets


class LCDRange(QtWidgets.QWidget):
    valueChanged: QtCore.pyqtSlot = QtCore.pyqtSignal(int)

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

    def value(self) -> int:
        return self.slider.value()

    @QtCore.pyqtSlot(int)
    def setValue(self, value: int) -> None:
        self.slider.setValue(value)

    def setRange(self, minValue: int, maxValue: int) -> None:
        if minValue < 0 or maxValue > 99 or minValue > maxValue:
            QtCore.qWarning(f"LCDRange::setRange({minValue}, {maxValue})\n"
                    "\tRange must be 0..99\n"
                    "\tand minValue must not be greater than maxValue")
            return
        self.slider.setRange(minValue, maxValue)

class CannonField(QtWidgets.QWidget):
    angleChanged: QtCore.pyqtSignal = QtCore.pyqtSignal(int)
    forceChanged: QtCore.pyqtSignal = QtCore.pyqtSignal(int)

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)

        self.currentAngle: int = 45
        self.currentForce: int = 0
        self.timerCount: int = 0
        self.autoShootTimer: QtCore.QTimer = QtCore.QTimer(self)
        self.autoShootTimer.timeout.connect(self.moveShot)     # emit signal without information
        self.shootAngle: int = 0
        self.shootForce: int = 0

        self.setPalette(QtGui.QPalette(QtGui.QColor(250, 250, 200)))
        self.setAutoFillBackground(True)

    def angle(self) -> int:
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

    def force(self) -> int:
        return self.currentForce

    @QtCore.pyqtSlot(int)
    def setForce(self, force: int) -> None:
        if force < 0:
            force = 0
        if self.currentForce == force:
            return
        self.currentForce = force
        self.forceChanged.emit(self.currentForce)

    @QtCore.pyqtSlot()
    def shoot(self) -> None:
        if self.autoShootTimer.isActive():
            return
        self.timerCount: int = 0
        self.shootAngle = self.currentAngle
        self.shootForce = self.currentForce
        self.autoShootTimer.start(5)

    @QtCore.pyqtSlot()
    def moveShot(self) -> None:
        region: QtGui.QRegion = QtGui.QRegion(self.shotRect())  ## not implement
        self.timerCount += 1

        shotR: QtCore.QRect = self.shotRect()

        if shotR.x() > self.width() or shotR.y() > self.height():
            self.autoShootTimer.stop()
        else:
            region = region.united(QtGui.QRegion(shotR))

        self.update(region)             # only update region

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter: QtGui.QPainter = QtGui.QPainter(self)

        self.paintCannon(painter)               # not implement
        if self.autoShootTimer.isActive():
            self.paintShot(painter)           # not implement

    def paintShot(self, painter: QtGui.QPainter):
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.black)
        painter.drawRect(self.shotRect())

    barrelRect: QtCore.QRect = QtCore.QRect(33, -4, 15, 8)

    def paintCannon(self, painter: QtGui.QPainter) -> None:
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.blue)

        painter.save()
        painter.translate(0, self.height())
        painter.drawPie(QtCore.QRect(-35, -35, 70, 70), 0, 90 * 16)
        painter.rotate( -self.currentAngle)
        painter.drawRect(CannonField.barrelRect)  # global parameter?
        painter.restore()

    def cannonRect(self) -> QtCore.QRect:
        result: QtCore.QRect = QtCore.QRect(0, 0, 50, 50)
        result.moveBottomLeft(self.rect().bottomLeft())
        return result

    def shotRect(self) -> QtCore.QRect:
        gravity: float = 4.0

        time: float = self.timerCount / 40.0
        velocity: int = self.shootForce
        radians: float = self.shootAngle * math.pi / 180

        velx: float = velocity * math.cos(radians)
        vely: float = velocity * math.sin(radians)
        x0: float = (CannonField.barrelRect.right() + 5) * math.cos(radians)
        y0: float = (CannonField.barrelRect.right() + 5) * math.sin(radians)
        x: float = x0 + velx * time
        y: float = y0 + vely * time - 0.5 * gravity * time * time

        result: QtCore.QRect = QtCore.QRect(0, 0, 6, 6)
        result.moveCenter(QtCore.QPoint(round(x), self.height() - 1 - round(y)))
        return result

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        quit: QtWidgets.QPushButton = QtWidgets.QPushButton("&Quit")
        quit.setFont(QtGui.QFont("Times", 18,
                                 QtGui.QFont.Bold))
        quit.clicked.connect(QtWidgets.qApp.quit)

        angle: LCDRange = LCDRange()
        angle.setRange(5, 70)

        force: LCDRange = LCDRange()
        force.setRange(10, 50)

        cannonField: CannonField = CannonField()

        angle.valueChanged.connect(cannonField.setAngle)
        cannonField.angleChanged.connect(angle.setValue)

        force.valueChanged.connect(cannonField.setForce)
        cannonField.forceChanged.connect(force.setValue)

        shoot: QtWidgets.QPushButton = QtWidgets.QPushButton("&Shoot")
        shoot.setFont(QtGui.QFont("Tiomes", 18,
                                  QtGui.QFont.Bold))

        shoot.clicked.connect(cannonField.shoot)

        topLayout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        topLayout.addWidget(shoot)
        topLayout.addStretch(1)

        leftLayout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        leftLayout.addWidget(angle)
        leftLayout.addWidget(force)

        gridLayout: QtWidgets.QGridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(quit, 0, 0)
        gridLayout.addLayout(topLayout, 0, 1)
        gridLayout.addLayout(leftLayout, 1, 0)
        gridLayout.addWidget(cannonField, 1, 1, 2, 1)
        gridLayout.setColumnStretch(1, 10)
        self.setLayout(gridLayout)

        angle.setValue(60)
        force.setValue(25)
        angle.setFocus()


if __name__ == '__main__':
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    widget: MyWidget = MyWidget()
    widget.setGeometry(100, 100, 500, 355)
    widget.show()
    sys.exit(app.exec_())