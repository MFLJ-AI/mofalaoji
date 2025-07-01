# 泰坦尼克号数据分析学习日志

## 📅 日期  
2025年7月1日  

## 🎯 学习主题  
泰坦尼克号乘客生还率的多维度分析  

## 🛠 使用工具  
- Python 3.x  
- Pandas (数据清洗与分析)  
- Matplotlib/Seaborn (数据可视化)  

---

## 📊 分析内容总结

### 1. 乘客等级(Pclass)对生还率的影响

\`\`\`python
# 关键代码
survival_rates = data.groupby('Pclass')['Survived'].mean()
plt.bar(['上层(1)', '中层(2)', '下层(3)'], survival_rates)
\`\`\`

**发现**：  
✅ 上层乘客(1等舱)生还率最高(≈63%)  
✅ 中层乘客(2等舱)生还率次之(≈47%)  
✅ 下层乘客(3等舱)生还率最低(≈24%)  

**结论**：社会阶层显著影响生还机会  

---

### 2. 年龄(Age)对生还率的影响

\`\`\`python
# 关键代码
age_bins = [0,10,20,30,40,50,60,70,80]
data['AgeGroup'] = pd.cut(data['Age'], bins=age_bins)
age_survival = data.groupby('AgeGroup')['Survived'].mean()
\`\`\`

**发现**：  
👶 儿童(0-10岁)生还率最高(≈59%)  
👴 老年人(60岁以上)生还率较低(≈35%)  
📉 20-30岁组生还率接近平均水平(≈35%)  

**结论**："妇女儿童优先"原则得到体现  

---

### 3. 性别与年龄的联合分析

\`\`\`python
# 关键代码
sns.catplot(
    x='AgeGroup', 
    y='Survived', 
    hue='Sex', 
    data=data, 
    kind='bar',
    height=6,
    aspect=2
)
\`\`\`

**核心发现**：  
🚺 **女性生还率全面高于男性**  
- 女童(0-10岁)生还率：≈91%  
- 男童(0-10岁)生还率：≈61%  

🚹 **男性生存劣势明显**  
- 20-30岁男性生还率仅≈15%  
- 60岁以上男性生还率仅≈9%  

**结论**：性别是影响生还的最关键因素，且在各年龄组表现一致  

---

## ⚠ 遇到的问题与解决方案

| 问题类型 | 具体表现 | 解决方案 |
|---------|---------|---------|
| 后端错误 | \`AttributeError: module 'backend_interagg' has no attribute 'FigureCanvas'\` | 使用\`matplotlib.use('Agg')\` |
| 中文乱码 | 图表中文标签显示为方框 | 设置\`plt.rcParams['font.sans-serif'] = ['SimHei']\` |
| 数据缺失 | 约20%年龄数据缺失 | 使用\`data.dropna(subset=['Age'])\`过滤 |

---

## 💡 关键学习收获

1. **数据讲故事能力**  
   - 通过可视化将历史事件(妇女儿童优先)转化为数据洞察
   
2. **多维度分析技巧**  
   
\`\`\`python
# 多维交叉分析
data.groupby(['AgeGroup','Sex','Pclass'])['Survived'].mean()
\`\`\`

3. **灵活应变能力**  
   - 图形渲染失败时转为纯文本分析
   - 样本量不足时添加数据标注

---

## 📅 后续学习计划

1. **深入分析方向**  
   - 票价(Fare)与舱位(Cabin)对生还率的影响
   - 家庭成员数量(SibSp+Parch)与生还率关系

2. **技术优化**  
   
\`\`\`python
# 计划尝试的热力图
sns.heatmap(
    pd.crosstab(
        [data['Pclass'], data['AgeGroup']], 
        data['Survived']
    )
)
\`\`\`

3. **模型应用**  
   - 使用逻辑回归预测生还概率
   - 构建决策树模型可视化关键特征

---

## 💭 反思与心得

> "数据是历史的沉淀，分析是时光的解码器。泰坦尼克号不仅是一艘沉船，更是社会结构的缩影。通过今天的分析，我深刻感受到数据可视化在揭示人类行为模式和社会规则方面的强大力量。"

