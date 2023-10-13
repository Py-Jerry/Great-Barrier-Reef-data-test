import matplotlib.pyplot as plt
import pandas as pd

# 读取Excel文件，指定跳过表头行
data = pd.read_excel('大堡礁降水数据.xlsx', skiprows=1, header=None)
year = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
# 循环每个横向数据
for index, row in data.iterrows():
    # 获取当前横向数据
    horizontal_data = row.values

    # 创建折线图
    plt.plot(horizontal_data)

    # 添加标题和轴标签
    plt.title(f'Precipitation Trend {index}')
    plt.xlabel('Time')
    plt.ylabel('Precipitation')

    # 显示图表
    plt.show()
