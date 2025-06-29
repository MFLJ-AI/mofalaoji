# 此设备：魔法老姬
# 开发时间：2025/6/29 15:32
#一
import numpy as np

# 创建3x4的二维数组，元素为1到12
arr = np.arange(1, 13).reshape(3, 4)

print("原始数组:")
print(arr)

# 任务1：打印数组属性
print("\n1. 数组属性:")
print("形状:", arr.shape)      # 输出 (3, 4)
print("维度:", arr.ndim)       # 输出 2
print("数据类型:", arr.dtype)  # 输出 int32/int64（取决于系统）

# 任务2：数组元素乘以2
arr_multiplied = arr * 2
print("\n2. 元素乘以2后的数组:")
print(arr_multiplied)

# 任务3：重塑为4x3
arr_reshaped = arr.reshape(4, 3)
print("\n3. 重塑为4x3的数组:")
print(arr_reshaped)

#二
import numpy as np

# 创建4x4数组
array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

print("原始数组:")
print(array)

# 任务1：提取第2行所有元素（注意：从0开始索引）
row_2 = array[1, :]
print("\n1. 第2行所有元素:")
print(row_2)  # 输出 [5 6 7 8]

# 任务2：提取第3列所有元素
col_3 = array[:, 2]
print("\n2. 第3列所有元素:")
print(col_3)  # 输出 [ 3  7 11 15]

# 任务3：提取子数组（第1、2行和第2、3列）
sub_array = array[0:2, 1:3]
print("\n3. 子数组（第1-2行，第2-3列）:")
print(sub_array)  # 输出 [[2 3]
                 #      [6 7]]

# 任务4：将大于10的元素替换为0
array[array > 10] = 0
print("\n4. 修改后的数组（>10的元素替换为0）:")
print(array)

#三
import numpy as np

# 创建数组A（3x2）
A = np.arange(1, 7).reshape(3, 2)
# 创建数组B（1x2）
B = np.array([10, 20])

print("数组A:")
print(A)
print("\n数组B:")
print(B)

# 任务1：逐元素相加（广播）
add_result = A + B
print("\n1. A + B（广播加法）:")
print(add_result)

# 任务2：逐元素相乘（广播）
mul_result = A * B
print("\n2. A * B（广播乘法）:")
print(mul_result)

# 任务3：每行与B的点积
dot_result = np.dot(A, B)
print("\n3. A每行与B的点积:")
print(dot_result)