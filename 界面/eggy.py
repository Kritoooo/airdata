# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QSplitter, QGridLayout, QLabel, QPushButton, QComboBox, \
#     QLineEdit
# from PyQt5.QtCore import Qt, QUrl, QFileInfo
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from pyecharts import options as opts
# from pyecharts.charts import Map
# from pyecharts.faker import Faker
#
#
# class Main_Window(QMainWindow):
#
#     def __init__(self):
#         self.desktop = QApplication.desktop()
#         self.screenRect = self.desktop.screenGeometry()
#         self.height = self.screenRect.height()
#         self.width = self.screenRect.width()
#
#         self.ditu1 = 'world'
#         self.ditu2 = ''
#
#         self.knowledge = {'world': '全世界共有七大洲和四大洋',
#                           'china': '中国共有56个民族，陆地面积960万平方千米，\n水域面积约470多万平方千米',
#                           '北京': '北京是中国的首都',
#                           '美国': ''
#                           }
#
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # 将整个窗口分割成3个模块
#         choice_frame = QFrame(self)  # 声明一个矩形框，放置设置用的按钮
#         choice_frame.setFrameShape(QFrame.StyledPanel)  # 在矩形框周围画上黑线
#         knowledge_frame = QFrame(self)  # 声明一个矩形框，写知识点
#         knowledge_frame.setFrameShape(QFrame.StyledPanel)
#         show_frame = QFrame(self)  # 声明一个矩形框，展示地图
#         show_frame.setFrameShape(QFrame.StyledPanel)
#
#         # 对三个矩形框进行位置的排列，左边上下各两个框，右边一个用来展示动画
#         splitter1 = QSplitter(Qt.Vertical)  # 纵向分割，每添加一个，会依次向下添加
#         splitter1.addWidget(choice_frame)  # 将选项矩形框添加到这个布局中
#         splitter1.addWidget(knowledge_frame)  # 将知识点矩形框添加到这个布局中
#
#         splitter2 = QSplitter(Qt.Horizontal)  # 横向分割
#         splitter2.addWidget(splitter1)  # 将第一个纵向分割添加到横向中
#         splitter2.addWidget(show_frame)  # 将展示矩形框添加到横向中
#
#         self.setCentralWidget(splitter2)  # 将横向分割放置在窗口
#
#         # 栅格布局放置按钮
#         choice_grid = QGridLayout()
#         choice_grid.setSpacing(10)
#
#         # 选择方式1
#         choice1_label = QLabel('地图显示选择')
#         choice1 = QComboBox(self)
#         choice1.addItem('world')
#         choice1.addItem('china')
#         choice1.addItem('美国')
#         choice1.addItem('日本')
#         choice1.addItem('加拿大')
#         choice1.addItem('北京')
#         choice1.addItem('上海')
#         choice1.addItem('天津')
#         choice1.addItem('重庆')
#         choice1.addItem('河北')
#         choice1.addItem('山西')
#         choice1.addItem('辽宁')
#         choice1.addItem('吉林')
#         choice1.addItem('黑龙江')
#         choice1.addItem('江苏')
#         choice1.addItem('浙江')
#         choice1.addItem('安徽')
#         choice1.addItem('福建')
#         choice1.addItem('江西')
#         choice1.addItem('山东')
#         choice1.addItem('河南')
#         choice1.addItem('湖北')
#         choice1.addItem('湖南')
#         choice1.addItem('广东')
#         choice1.addItem('海南')
#         choice1.addItem('四川')
#         choice1.addItem('贵州')
#         choice1.addItem('云南')
#         choice1.addItem('陕西')
#         choice1.addItem('甘肃')
#         choice1.addItem('青海')
#         choice1.addItem('台湾')
#         choice1.addItem('新疆')
#         choice1.addItem('西藏')
#         choice1.addItem('宁夏')
#         choice1.addItem('内蒙古')
#         choice1.addItem('广西')
#         choice1.activated[str].connect(self.ditu1_Changed)
#         button1 = QPushButton('显示', self)
#         button1.clicked.connect(self.button1_action)
#         choice_grid.addWidget(choice1_label, 0, 0)
#         choice_grid.addWidget(choice1, 0, 1)
#         choice_grid.addWidget(button1, 0, 2)
#         # 选择方式2
#         choice2_label = QLabel('地图输入')
#         choice2 = QLineEdit(self)
#         choice2.textChanged[str].connect(self.ditu2_Changed)
#         button2 = QPushButton('显示', self)
#         button2.clicked.connect(self.button2_action)
#         choice_grid.addWidget(choice2_label, 1, 0)
#         choice_grid.addWidget(choice2, 1, 1)
#         choice_grid.addWidget(button2, 1, 2)
#         choice_frame.setLayout(choice_grid)
#
#         # 知识点框架的设置
#         knowledge_grid = QGridLayout()
#         self.knowledge_label = QLabel('')
#         knowledge_grid.addWidget(self.knowledge_label)
#         knowledge_frame.setLayout(knowledge_grid)
#
#         # 地图放置框架的设置
#         self.map_grid = QGridLayout()
#         self.browser = QWebEngineView()
#         self.map_grid.addWidget(self.browser)
#         self.browser.load(QUrl(QFileInfo("./map.html").absoluteFilePath()))
#         show_frame.setLayout(self.map_grid)
#
#         self.setGeometry(self.width / 4, self.height / 4, self.width / 2, self.height / 2)
#         self.setWindowTitle('地理地图')
#
#     def ditu1_Changed(self, text):
#         self.ditu1 = text
#
#     def ditu2_Changed(self, text):
#         self.ditu2 = text
#
#     def button1_action(self):
#         print(self.ditu1)
#         self.get_ditu(self.ditu1)
#
#     def button2_action(self):
#         self.get_ditu(self.ditu2)
#
#     def get_ditu(self, text):
#         map = (Map().add(text, [list(z) for z in zip(Faker.provinces, Faker.values())], text)
#                .set_global_opts(title_opts=opts.TitleOpts(title="map")))
#         map.render('map.html')
#         self.browser.load(QUrl(QFileInfo("./map.html").absoluteFilePath()))
#         if text in self.knowledge:
#             self.knowledge_label.setText(self.knowledge[text])
#         else:
#             self.knowledge_label.setText('')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Main_Window()
#     window.show()
#     sys.exit(app.exec_())

# from pyecharts import options as opts
# from pyecharts.charts import Map
# city = ['贵阳市', '六盘水市', '遵义市', '安顺市', '毕节市', '铜仁市', '黔西南', '黔东南', '黔南布']
# values = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]
# c = (
#     Map()
#     .add("贵州地图", [list(z) for z in zip(city, values)], "贵州")
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="Map-贵州地图"), visualmap_opts=opts.VisualMapOpts(max_=10)
#     )
#     .render("map_GuiZhou.html")
# )

from pyecharts import options as opts
from pyecharts.charts import Map

province_distribution = {'河南省': 45.23, '北京市': 37.56, '河北省': 21, '辽宁省': 12, '江西省': 6, '上海省': 20,
                         '安徽省': 10, '江苏省': 16, '湖南省': 9, '浙江省': 13, '海南省': 2, '广东省': 22, '湖北省': 8,
                         '黑龙江省': 11, '陕西省': 11, '四川省': 7, '内蒙古': 3, '重庆市': 3, '云南省': 6, '贵州省': 2,
                         '吉林省': 3, '山西省': 12, '山东省': 11, '福建省': 4, '青海省': 1, '天津市': 1, '宁夏省':10}

provinces = list(province_distribution.keys())
values = list(province_distribution.values())
c = (
    Map()
    .add("中国地图", [list(z) for z in zip(provinces, values)], "china")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="中国地图"),
                     visualmap_opts=opts.VisualMapOpts(max_=200))
    .render("China_map.html")
)