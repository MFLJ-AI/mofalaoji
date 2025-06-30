# 此设备：魔法老姬
# 开发时间：2025/6/30 15:25
import pandas as pd
import numpy as np

# 步骤1：创建包含指定数据的DataFrame并保存为CSV
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Score': [92, 78, np.nan, 85, 88],
    'Grade': ['A', 'C', 'B', 'B', 'A']
}
df = pd.DataFrame(data)

# 保存到指定路径（确保路径存在）
file_path = r'D:\huaqing\Day3\Day3_6\students.csv'
df.to_csv(file_path, index=False)

# 步骤2：读取CSV文件并打印前3行
students_df = pd.read_csv(file_path)
print("前3行数据：")
print(students_df.head(3))

# 步骤3：处理缺失值
# 计算Score列的平均值（跳过NaN）
score_mean = students_df['Score'].mean()
# 填充缺失值
students_df['Score'].fillna(score_mean, inplace=True)
students_df['Name'].fillna('Unknown', inplace=True)

# 步骤4：保存处理后的DataFrame到新CSV文件
cleaned_path = r'D:\huaqing\Day3\Day3_6\students_cleaned.csv'
students_df.to_csv(cleaned_path, index=False)

print(f"\n处理后的数据已保存至: {cleaned_path}")
print("\n处理后的数据预览：")
print(students_df)