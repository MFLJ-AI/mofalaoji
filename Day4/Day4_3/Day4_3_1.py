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



# 读取数据
file_path = r'D:\huaqing\Day4\Day4_3\train.csv'
data = pd.read_csv(file_path)

# 处理年龄数据：删除缺失值并创建年龄分组
data = data.dropna(subset=['Age'])  # 删除年龄缺失的行

# 创建年龄分组
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
age_labels = ['0-10岁', '10-20岁', '20-30岁', '30-40岁', '40-50岁', '50-60岁', '60-70岁', '70-80岁']
data['AgeGroup'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels, right=False)

# 计算各年龄组的生还率
age_survival = data.groupby('AgeGroup')['Survived'].agg(['mean', 'count']).reset_index()
age_survival.columns = ['AgeGroup', 'SurvivalRate', 'Count']

# 创建直方图
plt.figure(figsize=(14, 8))

# 设置柱状图位置和宽度
x = np.arange(len(age_survival['AgeGroup']))
width = 0.7

# 绘制柱状图
bars = plt.bar(x, age_survival['SurvivalRate'], width, color='skyblue')

# 添加标题和标签
plt.title('泰坦尼克号乘客年龄与生还率关系', fontsize=16)
plt.xlabel('年龄组', fontsize=14)
plt.ylabel('生还率', fontsize=14)
plt.xticks(x, age_labels, rotation=45, ha='right')
plt.ylim(0, 1)  # 设置Y轴范围为0-1

# 在每个柱子上方添加生还率数值
for bar, rate, count in zip(bars, age_survival['SurvivalRate'], age_survival['Count']):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
             f'{height:.2%}\n({count}人)',  # 显示百分比和样本数
             ha='center', va='bottom', fontsize=10)

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加参考线
plt.axhline(y=age_survival['SurvivalRate'].mean(), color='r', linestyle='--',
            label=f'平均生还率: {age_survival["SurvivalRate"].mean():.2%}')
plt.legend()

# 保存图像
output_path = r'D:\huaqing\Day4\Day4_3\titanic_survival_by_age.png'
plt.tight_layout()
plt.savefig(output_path)
print(f"图表已保存至: {output_path}")

# 打印生还率数据
print("\n各年龄组乘客生还率:")
print(age_survival)

# 显示分析结论
print("\n分析结论:")
print(f"1. 儿童(0-10岁)生还率最高: {age_survival.iloc[0]['SurvivalRate']:.2%}")
print(f"2. 老年人(60岁以上)生还率较低: {age_survival.iloc[6]['SurvivalRate']:.2%}")
print(f"3. 20-30岁年轻人组生还率: {age_survival.iloc[2]['SurvivalRate']:.2%}")
print(f"4. 整体平均生还率: {age_survival['SurvivalRate'].mean():.2%}")