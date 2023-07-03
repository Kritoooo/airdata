
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType

from 数据分析.cityProvince import get_province
from 数据分析.预处理 import calc_province, calc_city
from 界面.htmltest import append_html


def init_map(pieces, name):
    map = Map(init_opts=opts.InitOpts(width="1500px", height="800px", theme=ThemeType.VINTAGE))  # 添加主题
    map.set_global_opts(
        # 标题配置项
        title_opts=opts.TitleOpts(
            title=name + "空气污染分布图",
            pos_left="center"
        ),
        # 图例配置项
        legend_opts=opts.LegendOpts(
            is_show=True,
            pos_left="left",
        ),
        # 视觉影射配置项
        visualmap_opts=opts.VisualMapOpts(
            min_=0,  # 组件最小值
            max_=1000,
            range_text=['污染程度分布颜色区间:', ''],  # 两端文本名称
            is_piecewise=True,  # 定义图例为分段型，默认为连续的图例
            pos_top="middle",  # 组件离容器左侧的距离
            pos_left="left",
            orient="vertical",  # 布局方式为垂直布局，水平为horizon
            pieces=pieces
        )
    )
    return map

def get_pieces(type):
    if type == "绝对指标":
        pieces = [
                {"max":999, "min":301, "label" : ">300", "color": "#8b0000"},
                {"max": 300, "min": 201, "label": ">200", "color": "#800080"},
                {"max": 200, "min": 151, "label": ">150", "color": "#FF0000"},
                {"max": 150, "min": 101, "label": ">100", "color": "#FFA500"},
                {"max": 100, "min": 51, "label": ">50", "color": "#FFFF00"},
                {"max": 50, "min": 1, "label": "<51", "color": "#00FF00"}
            ]
    else:
        pieces = [
            {"max": 100, "min": 85, "label": ">=85", "color": "#8b0000"},
            {"max": 84, "min": 60, "label": ">=60", "color": "#800080"},
            {"max": 59, "min": 45, "label": ">=45", "color": "#FF0000"},
            {"max": 44, "min": 30, "label": ">=30", "color": "#FFA500"},
            {"max": 29, "min": 15, "label": ">=15", "color": "#FFFF00"},
            {"max": 14, "min": 1, "label": ">=1", "color": "#00FF00"}
        ]
    return pieces
def generate_map(target, type):
    pieces = get_pieces(type)
    provinces, values = calc_province(target, type)
    # maptype='china' 只显示全国直辖市和省级
    map = init_map(pieces, "全国")
    map.add("程度", [list(z) for z in zip(provinces, values)], maptype="china")
    map.render("../文件操作/map/全国.html")
    for i in provinces:
        map = init_map(pieces, i)
        city, values = calc_city(target, type, i)
        map.add("程度", [list(z) for z in zip(city, values)],maptype=get_province(i))
        map.render("../文件操作/map/" + i + ".html")
    append_html()


# generate_map("AQI指数", "绝对指标")
