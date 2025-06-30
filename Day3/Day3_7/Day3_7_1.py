# 此设备：魔法老姬
# 开发时间：2025/6/30 16:22
import matplotlib
# 设置正确的后端（通常使用TkAgg或Agg）
matplotlib.use('TkAgg')  # 如果这不起作用，尝试 'Agg'

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

# 创建销售数据
months = ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01',
          '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01',
          '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01']

# 转换为datetime对象
dates = [datetime.strptime(month, '%Y-%m-%d') for month in months]

# 生成销售数据（单位：万元）- 模拟季节性波动
np.random.seed(42)
sales = np.array([85, 78, 92, 88, 105, 120, 115, 110, 95, 102, 130, 145])

# 创建图表
plt.figure(figsize=(12, 6))

# 绘制折线图
plt.plot(dates, sales, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5, markersize=8)

# 添加数据标签
for i, value in enumerate(sales):
    plt.text(dates[i], value + 3, f'{value}万', ha='center', fontsize=9)

# 设置标题和标签
plt.title('2023年月度销售数据', fontsize=15, pad=20)
plt.xlabel('月份', fontsize=12, labelpad=10)
plt.ylabel('销售额 (万元)', fontsize=12, labelpad=10)

# 设置x轴为月份格式
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gcf().autofmt_xdate()  # 自动旋转日期标签

# 设置网格
plt.grid(True, linestyle='--', alpha=0.7)

# 设置y轴范围
plt.ylim(60, 160)

# 添加注解
plt.annotate('年度最高', xy=(dates[-1], sales[-1]), xytext=(dates[-1], sales[-1] + 15),
             arrowprops=dict(facecolor='red', shrink=0.05),
             ha='center', fontsize=10, color='red')

# 显示图表
plt.tight_layout()
plt.show()