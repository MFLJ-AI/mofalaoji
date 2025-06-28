# 此设备：魔法老姬
# 开发时间：2025/6/28 16:23

#题一
def is_prime(n):
    """判断一个数是否为素数"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("1到100之间的素数有:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")

print("\n" + "="*50 + "\n")  # 分隔线

#题二
# 初始化前两项
fib = [0, 1]

# 计算后续18项
for i in range(2, 20):
    fib.append(fib[i-1] + fib[i-2])

print("斐波那契数列前20项:")
print(fib)

print("\n" + "="*50 + "\n")  # 分隔线

#题三
total = 0
num = 1

while num <= 10000:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1

print("1-10000之间满足条件的数的和为:", total)