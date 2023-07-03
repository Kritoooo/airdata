import sys
from 数据分析 import 预处理
from PyQt5.QtGui import QPixmap
from 数据分析 import cityDict
from 数据分析.数据可视化 import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
from 文件操作 import eggy
from 界面 import picshow, showpanel, mainwid



class main_window(mainwid.Ui_mainwid, QWidget):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = main_window()

    main_window.show()

    sys.exit(app.exec_())