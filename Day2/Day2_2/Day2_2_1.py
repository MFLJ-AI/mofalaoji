# 此设备：魔法老姬
# 开发时间：2025/6/29 9:38
class Car:
    """汽车类"""

    def __init__(self, brand, speed=0):
        """初始化品牌和速度"""
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        """加速m次，每次速度增加10"""
        self.speed += 10 * m
        print(f"{self.brand} 加速{m}次，当前速度：{self.speed}")

    def brake(self, n):
        """刹车n次，每次速度减少10，不低于0"""
        self.speed = max(0, self.speed - 10 * n)
        print(f"{self.brand} 刹车{n}次，当前速度：{self.speed}")


class ElectricCar(Car):
    """电动汽车子类"""

    def __init__(self, brand, speed=0, battery=50):
        """新增电量属性"""
        super().__init__(brand, speed)
        self.battery = battery

    def charge(self):
        """充电，电量增加20，不超过100"""
        self.battery = min(100, self.battery + 20)
        print(f"{self.brand} 充电后电量：{self.battery}%")


# 测试Car类
print("=== 普通汽车测试 ===")
my_car = Car("Toyota")
my_car.accelerate(3)  # 加速3次
my_car.brake(1)       # 刹车1次
my_car.accelerate(2)  # 加速2次
my_car.brake(4)       # 刹车4次（会减到0）

# 测试ElectricCar子类
print("\n=== 电动汽车测试 ===")
my_ev = ElectricCar("Tesla", battery=75)
print(f"初始电量：{my_ev.battery}%")
my_ev.accelerate(2)   # 继承的加速方法
my_ev.charge()        # 充电
my_ev.charge()        # 再次充电（不会超过100）
my_ev.brake(1)        # 继承的刹车方法