# 此设备：魔法老姬
# 开发时间：2025/6/30 14:58
import pandas as pd
import numpy as np
import os

# 设置文件路径
base_path = r'D:\huaqing\Day3\Day3_5'
file_names = ['2015年国内主要城市年度数据.csv', '2016年国内主要城市年度数据.csv', '2017年国内主要城市年度数据.csv']

# 1. 读取并合并数据（纵向连接）
dfs = []
for file in file_names:
    file_path = os.path.join(base_path, file)
    df = pd.read_csv(file_path, encoding='utf-8-sig')
    dfs.append(df)

# 合并所有数据
merged_df = pd.concat(dfs, ignore_index=True)

# 2. 按照年份聚合
# 由于数据已经是年度数据，这一步主要是按年份分组

# 3. 求每年的国内生产总值
gdp_by_year = merged_df.groupby('年份')['国内生产总值'].sum().reset_index()
gdp_by_year.columns = ['年份', '国内生产总值总和']

# 4. 处理缺省值，填充为0
# 特别处理'房地产开发投资额'列中的空字符串
merged_df['房地产开发投资额'] = pd.to_numeric(merged_df['房地产开发投资额'], errors='coerce')
merged_df.fillna(0, inplace=True)

# 输出结果
print("1. 合并后的数据概览:")
print(f"数据集形状: {merged_df.shape}")
print(f"包含年份: {merged_df['年份'].unique()}\n")

print("2. 按年份聚合后的国内生产总值总和:")
print(gdp_by_year.to_string(index=False))

print("\n3. 缺省值处理结果:")
print("各列缺失值数量:")
print(merged_df.isnull().sum())

# 5. 计算每个城市GDP年均增长率并找出最高/最低的五个城市
# 提取每个城市2015和2017年的GDP数据
gdp_growth = merged_df.pivot_table(index='地区', columns='年份', values='国内生产总值')
gdp_growth = gdp_growth[[2015, 2017]].dropna()

# 计算年均增长率（%）
gdp_growth['年均增长率(%)'] = ((gdp_growth[2017] / gdp_growth[2015])**(1/2) - 1) * 100

# 排序并选择最高和最低的五个城市
top_5 = gdp_growth.nlargest(5, '年均增长率(%)')
bottom_5 = gdp_growth.nsmallest(5, '年均增长率(%)')

print("\n5. GDP年均增长率分析:")
print("\n增长率最高的5个城市:")
print(top_5[['年均增长率(%)']])
print("\n增长率最低的5个城市:")
print(bottom_5[['年均增长率(%)']])

# 6. 医院、卫生院数的归一化处理（Min-Max标准化）
# 按年份分组进行归一化
def min_max_normalize(group):
    min_val = group.min()
    max_val = group.max()
    if max_val - min_val > 0:
        return (group - min_val) / (max_val - min_val)
    return group * 0  # 避免除以0

merged_df['医院、卫生院数_归一化'] = merged_df.groupby('年份')['医院、卫生院数'].transform(min_max_normalize)

# 按年份比较医疗资源变化
medical_resource = merged_df.pivot_table(index='地区', columns='年份',
                                        values='医院、卫生院数_归一化',
                                        aggfunc='mean')

print("\n6. 医疗资源归一化结果 (部分城市展示):")
print(medical_resource.head(10))  # 展示前10个城市

# 7. 提取四大城市数据并保存为新CSV
cities = ['北京', '上海', '广州', '深圳']
selected_cols = ['地区', '年份', '国内生产总值', '社会商品零售总额']
big4_df = merged_df[merged_df['地区'].isin(cities)][selected_cols]

# 按城市和年份排序
big4_df = big4_df.sort_values(by=['地区', '年份'])

# 保存为CSV
output_path = os.path.join(base_path, '四大城市GDP与消费数据.csv')
big4_df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"\n7. 四大城市数据已保存至: {output_path}")
print("数据预览:")
print(big4_df)