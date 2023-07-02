from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.qwebengine = QWebEngineView()
        url = os.getcwd() + os.path.sep + "\map\全国.html"
        print(url)
        self.qwebengine.load(QUrl.fromLocalFile(url))
        # self.qwebengine.load(QUrl('https://www.baidu.com'))
        self.setCentralWidget(self.qwebengine)


app = QApplication(sys.argv)
screen = Window()
screen.showMaximized()
sys.exit(app.exec_())

# chart_ad4f869ce26944ee890178c574c70830.on('click', function (param){
#             var selected = param.name;
#                 if (selected) {
#                     switch(selected){
#                         case '北京市':
#                             location.href = "./北京市.html";
#                             break;
#                         case '上海市':
#                             location.href = "./上海市.html";
#                             break;
#                         case '天津市':
#                             location.href = "./天津市.html";
#                             break;
#                         case '四川省':
#                             location.href = "./四川省.html";
#                             break;
#                         case '安徽省':
#                             location.href = "./安徽省.html";
#                             break;
#                         case '山东省':
#                             location.href = "./山东省.html";
#                             break;
#                         case '江苏省':
#                             location.href = "./江苏省.html";
#                             break;
#                         case '江西省':
#                             location.href = "./江西省.html";
#                             break;
#                         case '河北省':
#                             location.href = "./河北省.html";
#                             break;
#                         case '浙江省':
#                             location.href = "./浙江省.html";
#                             break;
#                         case '海南省':
#                             location.href = "./海南省.html";
#                             break;
#                         case '湖北省':
#                             location.href = "./湖北省.html";
#                             break;
#                         case '湖南省':
#                             location.href = "./湖南省.html";
#                             break;
#                         case '广东省':
#                             location.href = "./广东省.html";
#                             break;
#                         case '福建省':
#                             location.href = "./福建省.html";
#                             break;
#                         case '甘肃省':
#                             location.href = "./甘肃省.html";
#                             break;
#                         case '广西壮族自治区':
#                             location.href = "./广西壮族自治区.html";
#                             break;
#                         case '贵州省':
#                             location.href = "./贵州省.html";
#                             break;
#                         case '河南省':
#                             location.href = "./河南省.html";
#                             break;
#                         case '黑龙江省':
#                             location.href = "./黑龙江省.html";
#                             break;
#                         case '内蒙古自治区':
#                             location.href = "./内蒙古自治区.html";
#                             break;
#                         case '吉林省':
#                             location.href = "./吉林省.html";
#                             break;
#                         case '辽宁省':
#                             location.href = "./辽宁省.html";
#                             break;
#                         case '宁夏回族自治区':
#                             location.href = "./宁夏回族自治区.html";
#                             break;
#                         case '青海省':
#                             location.href = "./青海省.html";
#                             break;
#                         case '山西省':
#                             location.href = "./山西省.html";
#                             break;
#                         case '陕西省':
#                             location.href = "./陕西省.html";
#                             break;
#                         case '台湾省':
#                             location.href = "./台湾省.html";
#                             break;
#                         case '西藏自治区':
#                             location.href = "./西藏自治区.html";
#                             break;
#                         case '新疆维吾尔自治区':
#                             location.href = "./新疆维吾尔自治区.html";
#                             break;
#                         case '云南省':
#                             location.href = "./云南省.html";
#                             break;
#                         case '重庆市':
#                             location.href = "./重庆市.html";
#                             break;
#                         default:
#                             break;
#                     }
#
#             }
#       });