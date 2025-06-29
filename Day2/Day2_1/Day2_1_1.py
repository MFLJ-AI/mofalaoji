# 此设备：魔法老姬
# 开发时间：2025/6/29 9:21
#一
def is_palindrome(number):
    """判断一个数是否为回文数"""
    num_str = str(number)
    return num_str == num_str[::-1]

# 测试示例
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False
print(is_palindrome(1221)) # True
print("\n" + "="*50 + "\n")

#二
def calculate_average(*args):
    """计算任意数量参数的平均值"""
    return sum(args) / len(args) if args else 0

# 测试示例
print(calculate_average(1, 2, 3))      # 2.0
print(calculate_average(10, 20, 30, 40)) # 25.0
print(calculate_average())              # 0
print("\n" + "="*50 + "\n")

#三
def find_longest_string(*strings):
    """返回任意多个字符串中最长的一个"""
    return max(strings, key=len, default=None)

# 测试示例
print(find_longest_string("apple", "banana", "cherry"))  # "banana"
print(find_longest_string("hello", "world"))             # "hello"
print(find_longest_string())                             # None
print("\n" + "="*50 + "\n")


