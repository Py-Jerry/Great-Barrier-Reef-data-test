import matplotlib.pyplot as plt
import pandas as pd

# 读取Excel文件
data = pd.read_excel('temperatue.xlsx', header=None)

# 循环每个横向数据
for index, row in data.iterrows():
    # 获取当前横向数据
    horizontal_data = row.values

    # 创建折线图
    plt.plot(horizontal_data)

    # 添加标题和轴标签
    plt.title(f'Temperature Trend {index}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')

    # 显示图表
    plt.show()
