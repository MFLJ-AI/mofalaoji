# 学习日志：2025年6月30日
## 📌 今日学习内容总结
### 1. Pandas数据处理
- **CSV文件操作**：
  - 创建DataFrame并保存为CSV文件
  ```python
  df.to_csv('students.csv', index=False)
  ```
  - 读取CSV文件并查看数据
  ```python
  students_df = pd.read_csv('students.csv')
  print(students_df.head(3))
  ```
  
- **缺失值处理**：
  - 计算列平均值填充数值缺失
  ```python
  score_mean = students_df['Score'].mean()
  students_df['Score'].fillna(score_mean, inplace=True)
  ```
  - 使用固定值填充文本缺失
  ```python
  students_df['Name'].fillna('Unknown', inplace=True)
  ```
  
- **数据保存**：
  - 将处理后的数据保存为新CSV文件
  ```python
  students_df.to_csv('students_cleaned.csv', index=False)
  ```
### 2. Matplotlib数据可视化
- **折线图绘制**：
  - 准备时间序列数据
  ```python
  dates = [datetime.strptime(month, '%Y-%m-%d') for month in months]
  ```
  
  - 创建基础图表
  ```python
  plt.figure(figsize=(12, 6))
  plt.plot(dates, sales, marker='o', linestyle='-')
  ```
  
  - 图表定制化：
    - 添加数据标签
    ```python
    for i, value in enumerate(sales):
        plt.text(dates[i], value + 3, f'{value}万', ha='center')
    ```
    
    - 设置日期格式
    ```python
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ```
    
    - 添加标注和网格
    ```python
    plt.annotate('年度最高', xy=(dates[-1], sales[-1]), ...)
    plt.grid(True, linestyle='--', alpha=0.7)
    ```
### 3. 解决Matplotlib后端问题
- **后端配置错误处理**：
  ```python
  import matplotlib
  matplotlib.use('TkAgg')  # 显式设置后端
  ```
  
- **备选解决方案**：
  - 尝试不同后端：`'Qt5Agg'`, `'WXAgg'`, `'Agg'`
  - 直接保存图像代替显示
  ```python
  plt.savefig('sales_trend.png', bbox_inches='tight')
  ```
## 💡 关键知识点
1. **Pandas核心操作**：
   - `to_csv()`/`read_csv()` 文件读写
   - `fillna()` 缺失值处理
   - `mean()` 列平均值计算
2. **时间序列可视化**：
   - 使用`datetime`转换日期格式
   - `mdates.DateFormatter` 日期格式化
   - `autofmt_xdate()` 自动旋转日期标签
3. **图表增强技巧**：
   - 数据点标注（`plt.text()`）
   - 特殊点标注（`plt.annotate()`）
   - 网格线定制（`linestyle`, `alpha`参数）
## 🚧 遇到的问题及解决
| 问题 | 解决方案 | 学习要点 |
|------|----------|----------|
| Matplotlib后端错误 | 显式设置`matplotlib.use('TkAgg')` | 1. 理解后端概念<br>2. 掌握常用后端选项<br>3. 环境配置重要性 |
| 日期格式显示异常 | 使用`DateFormatter('%Y-%m')` | 时间序列可视化的格式化技巧 |
| 缺失值处理逻辑混淆 | 区分数值列和文本列处理方式 | 数据类型决定处理策略 |
## 📚 明日学习计划
1. **深入Pandas**：
   - 数据分组与聚合（`groupby`）
   - 数据合并操作（`merge`, `concat`）
   - 时间序列处理（`resample`）
2. **高级可视化**：
   - 多子图绘制（`subplots`）
   - 双Y轴图表
   - 交互式可视化（Plotly初步）
3. **项目实践**：
   - 完整数据分析流程：从数据清洗到可视化报告
   - 销售数据分析小项目