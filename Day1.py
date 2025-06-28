# 此设备：魔法老姬
# 开发时间：2025/6/28 11:22

#题一
x = 10
y = "10"
z = True

print("x的数据类型是:", type(x))
print("y的数据类型是:", type(y))
print("z的数据类型是:", type(z))

#题二
radius = float(input("请输入圆的半径: "))
# 定义π的值
pi = 3.14
# 计算面积
area = pi * radius ** 2
# 输出结果
print("圆的面积是:", area)

#题三
# 原始字符串
num_str = "3.14"
# 转换为浮点数
num_float = float(num_str)
# 转换为整数
num_int = int(num_float)

print("字符串转浮点数:", num_float)
print("浮点数转整数:", num_int)
print("注意：浮点数转整数会直接截断小数部分")