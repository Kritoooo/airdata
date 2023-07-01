import picshow, showpanel
import sys
from PyQt5.QtWidgets import *

class query_window(showpanel.Ui_showwid, QWidget):
    def __init__(self):
        super(query_window, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    query_window = query_window()


    query_window.show()

    sys.exit(app.exec_())