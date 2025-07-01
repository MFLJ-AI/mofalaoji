# 此设备：魔法老姬
# 开发时间：2025/7/1 9:26

import matplotlib
matplotlib.use('Agg')  # 必须在导入pyplot之前设置
import matplotlib.pyplot as plt
import numpy as np

# 示例数据
cities = ['北京', '上海', '广州', '深圳', '杭州']
gdp_2015 = [2300, 2500, 1800, 1750, 1100]

# 创建图形
plt.figure(figsize=(12, 6))
plt.bar(cities, gdp_2015, color='skyblue')

# 添加数据标签
for i in range(len(cities)):
    plt.text(i, gdp_2015[i], str(gdp_2015[i]),
             ha='center', va='bottom', fontsize=9)

plt.title('2015年各城市GDP', fontsize=14)
plt.xlabel('城市', fontsize=12)
plt.ylabel('GDP (亿元)', fontsize=12)
plt.tight_layout()

# 保存图像而不是显示
plt.savefig('gdp_bar.png')
print("图形已保存为 gdp_bar.png")

# 设置中文字体（如果显示中文有问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
plt.rcParams['axes.unicode_minus'] = False

# 突出显示最大的部分
explode = (0.1, 0, 0, 0, 0)  # 突出北京

plt.figure(figsize=(8, 8))
plt.pie(gdp_2015, labels=cities, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('2015年各城市GDP占比', fontsize=14)
plt.axis('equal')  # 保证饼图是圆形
plt.tight_layout()
plt.show()