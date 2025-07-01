# 此设备：魔法老姬
# 开发时间：2025/7/1 10:27
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 设置使用非交互式后端
matplotlib.use('Agg')  # 必须在导入pyplot之前设置

# 读取数据
file_path = r'D:\huaqing\Day4\Day4_3\train.csv'
data = pd.read_csv(file_path)

# 计算各乘客等级的生还率
survival_rates = data.groupby('Pclass')['Survived'].mean().reset_index()

# 创建直方图
plt.figure(figsize=(10, 6))

# 设置柱状图位置和宽度
x = np.arange(len(survival_rates['Pclass']))
width = 0.6

# 绘制柱状图
bars = plt.bar(x, survival_rates['Survived'], width, color=['#1f77b4', '#ff7f0e', '#2ca02c'])

# 添加标题和标签
plt.title('泰坦尼克号乘客等级与生还率关系', fontsize=14)
plt.xlabel('乘客等级', fontsize=12)
plt.ylabel('生还率', fontsize=12)
plt.xticks(x, ['上层(1)', '中层(2)', '下层(3)'])
plt.ylim(0, 1)  # 设置Y轴范围为0-1

# 在每个柱子上方添加生还率数值
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2%}',  # 显示百分比格式
             ha='center', va='bottom', fontsize=12)

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 保存图像
output_path = r'D:\huaqing\Day4\Day4_3\titanic_survival_by_class.png'
plt.savefig(output_path)
print(f"图表已保存至: {output_path}")

# 打印生还率数据
print("\n各等级乘客生还率:")
print(survival_rates)

# 显示生还率结果
print("\n生还率分析:")
for i, row in survival_rates.iterrows():
    class_name = ['上层(1)', '中层(2)', '下层(3)'][i]
    print(f"{class_name}乘客的生还率: {row['Survived']:.2%}")