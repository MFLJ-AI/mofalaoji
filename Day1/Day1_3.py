# 此设备：魔法老姬
# 开发时间：2025/6/28 17:07
#题一
# 列表推导式生成1-100的整数
numbers = [x for x in range(1, 101)]

# 输出所有偶数
even_numbers = [num for num in numbers if num % 2 == 0]
print("1-100之间的所有偶数:")
print(even_numbers)

print("\n" + "="*50 + "\n")  # 分隔线

#题二
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# 示例列表
original_list = [3, 5, 2, 3, 8, 5, 9, 2, 1]

# 删除重复元素
unique_list = remove_duplicates(original_list)
print("原始列表:", original_list)
print("去重后的列表:", unique_list)

print("\n" + "="*50 + "\n")  # 分隔线

#题三
keys = ["a", "b", "c"]
values = [1, 2, 3]

# 合并为字典
result_dict = dict(zip(keys, values))
print("合并后的字典:")
print(result_dict)

print("\n" + "="*50 + "\n")  # 分隔线

#题四
# 定义学生信息元组
student_info = ("张三", 20, 89.5)

# 解包元组
name, age, score = student_info

print("学生信息:")
print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"成绩: {score}")

print("\n" + "="*50 + "\n")  # 分隔线