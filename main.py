# calculator, discount, order 合併版

# ---------- 基本計算 ----------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ---------- 折扣 ----------
class Discount:
    def __init__(self, rate=0.1):
        self.rate = rate  # 預設 10%

    def apply(self, amount):
        discount_value = multiply(amount, self.rate)
        return subtract(amount, discount_value)


# ---------- 訂單 ----------
class Order:
    def __init__(self):
        self.items = []  # [(price, quantity)]

    def add_item(self, price, quantity):
        self.items.append((price, quantity))

    def total(self):
        total_price = 0
        for price, qty in self.items:
            total_price = add(total_price, multiply(price, qty))
        return total_price


# ---------- 測試 ----------
if __name__ == "__main__":
    order = Order()
    order.add_item(100, 2)  # 100元 * 2
    order.add_item(50, 3)   # 50元 * 3
    print("原始總額:", order.total())

    discount = Discount(0.2)  # 20% 折扣
    print("折扣後總額:", discount.apply(order.total()))
