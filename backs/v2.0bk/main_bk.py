# pyinstaller -F  -w -i D:\Project\Python\Calculator1999\images\logo_yellow.ico -n "伤害计算器v2.1test" main.py
from PyQt5.QtWidgets import QMainWindow, QApplication

from calculatorUI import *

import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.setupUi(self)

    _startPos = None
    _endPos = None
    _isTracking = None

    # 鼠标移动事件
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        if self._startPos:
            self._endPos = a0.pos() - self._startPos
            # 移动窗口
            self.move(self.pos() + self._endPos)

    # 鼠标按下事件
    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        # 根据鼠标按下时的位置判断是否在QFrame范围内
        if self.childAt(a0.pos().x(), a0.pos().y()).objectName() == "top_frame":
            # 判断鼠标按下的是左键
            if a0.button() == QtCore.Qt.LeftButton:
                self._isTracking = True
                # 记录初始位置
                self._startPos = QtCore.QPoint(a0.x(), a0.y())

    # 鼠标松开事件
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        if a0.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None





if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()

    calculator.show()

    sys.exit(app.exec_())
