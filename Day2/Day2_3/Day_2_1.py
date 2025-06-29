# 此设备：魔法老姬
# 开发时间：2025/6/29 10:34
import os
import re


def natural_sort_key(s):
    """
    生成自然排序键，使文件名按数字顺序排序
    例如：['1.png', '2.png', ..., '10.png'] 而不是 ['1.png', '10.png', '2.png']
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


# 设置路径
txt_path = r"D:\huaqing\Day2\Day2_3\text\zi.txt"
image_dir = r"D:\huaqing\Day2\Day2_3\text\tu"

# 读取名字列表
with open(txt_path, 'r', encoding='utf-8') as f:
    names = [line.strip() for line in f.readlines() if line.strip()]

# 获取图片文件列表并自然排序
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith('.png')]
image_files.sort(key=natural_sort_key)

# 检查数量是否匹配
if len(image_files) != len(names):
    print(f"警告: 图片数量({len(image_files)})与名字数量({len(names)})不匹配!")
    # 只处理数量匹配的部分
    min_count = min(len(image_files), len(names))
    image_files = image_files[:min_count]
    names = names[:min_count]

# 重命名文件
for i, (old_name, new_name) in enumerate(zip(image_files, names)):
    old_path = os.path.join(image_dir, old_name)
    new_path = os.path.join(image_dir, f"{new_name}.png")

    # 处理文件名冲突
    counter = 1
    while os.path.exists(new_path):
        new_path = os.path.join(image_dir, f"{new_name}_{counter}.png")
        counter += 1

    os.rename(old_path, new_path)
    print(f"重命名: {old_name} -> {os.path.basename(new_path)}")

print(f"\n成功重命名 {len(image_files)} 个文件!")