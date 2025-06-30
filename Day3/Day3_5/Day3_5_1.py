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