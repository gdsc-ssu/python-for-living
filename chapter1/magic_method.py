class Fruit(object):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __add__(self, target):
        return self._price + target._price

    def __sub__(self, target):
        return self._price - target._price

    def __mul__(self, target):
        return self._price * target._price

    def __truediv__(self, target):
        return self._price / target._price

    def __str__(self):
        return self._name

apple = Fruit("사과", 100000)
durian = Fruit("두리안", 50000)

print(apple + durian)
print(apple - durian)
print(apple * durian)
print(apple / durian)
print(f"{apple}와 {durian}")