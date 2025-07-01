# 此设备：魔法老姬
# 开发时间：2025/7/1 9:03
import matplotlib
matplotlib.use('Agg')  # 在导入pyplot之前设置后端
import matplotlib.pyplot as plt
import numpy as np

# 示例数据
countries = ['USA', 'China', 'Japan', 'Germany', 'UK']
gold_medal = [16, 14, 12, 10, 8]      # 金牌数
silver_medal = [9, 11, 10, 12, 7]     # 银牌数
bronze_medal = [12, 10, 9, 6, 5]      # 铜牌数

# 设置柱状图位置和宽度
x = np.arange(len(countries))  # 国家标签位置
width = 0.25  # 柱状图宽度

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制柱状图
plt.bar(x - width, gold_medal, width, label='金牌', color='gold')
plt.bar(x, silver_medal, width, label='银牌', color='silver')
plt.bar(x + width, bronze_medal, width, label='铜牌', color='#cd7f32')

# 添加文本标签
for i in range(len(x)):
    plt.text(x[i] - width, gold_medal[i], gold_medal[i],
             va='bottom', ha='center', fontsize=8)
    plt.text(x[i], silver_medal[i], silver_medal[i],
             va='bottom', ha='center', fontsize=8)
    plt.text(x[i] + width, bronze_medal[i], bronze_medal[i],
             va='bottom', ha='center', fontsize=8)

# 添加标题和标签
plt.title('各国奖牌数对比', fontsize=14)
plt.xlabel('国家', fontsize=12)
plt.ylabel('奖牌数', fontsize=12)
plt.xticks(x, countries)
plt.legend()

# 保存图形
plt.savefig('medal_comparison.png')
print("图形已保存为 medal_comparison.png")