# 此设备：魔法老姬
# 开发时间：2025/6/30 14:07
import pandas as pd

# 读取CSV文件
file_path = r'D:\huaqing\Day3\Day3_4\exercise_data\drinks.csv'
df = pd.read_csv(file_path)

# 1. 哪个大陆平均消耗的啤酒更多？
beer_avg = df.groupby('continent')['beer_servings'].mean().sort_values(ascending=False)
top_continent = beer_avg.idxmax()
print(f"1. 平均啤酒消耗最多的大陆是: {top_continent} ({beer_avg[top_continent]:.1f}份)\n")

# 2. 每个大陆的红酒消耗描述性统计
wine_stats = df.groupby('continent')['wine_servings'].describe()
print("2. 每个大陆红酒消耗的描述性统计:")
print(wine_stats, "\n")

# 3. 每个大陆每种酒类别的消耗平均值
avg_drinks = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].mean()
print("3. 每个大陆各类酒的平均消耗:")
print(avg_drinks, "\n")

# 4. 每个大陆每种酒类别的消耗中位数
median_drinks = df.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].median()
print("4. 每个大陆各类酒消耗的中位数:")
print(median_drinks)