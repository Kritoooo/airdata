import sys
from 数据分析 import 预处理
from PyQt5.QtGui import QPixmap
from 数据分析 import cityDict
from 数据分析.数据可视化 import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from 界面 import picshow, showpanel


class query_window(showpanel.Ui_showwid, QWidget):
    def __init__(self):
        super(query_window, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    query_window = query_window()


    query_window.show()

    sys.exit(app.exec_())