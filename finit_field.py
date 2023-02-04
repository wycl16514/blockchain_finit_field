class LimitFieldElement: #实现有限域的元素
    def __init__(self, num, order):
        """
        order 表示集合元素的个数，它必须是一个素数，不然有限域的性质不能满足
        num 对应元素的数值
        """

        if order <= num < 0:
            err = f"元素 {num} 数值必须在0到 {order - 1} 之间"
            raise ValueError(err)
        self.order = order
        self.num = num

    def __repr__(self):
        return f"LimitFieldElement_{self.order}({self.num})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.order == other.order

    def __ne__(self, other):
        if other is None:
            return True

        return self.num != other.num or self.order != other.order

    def __add__(self, other):
        """
        有限域元素的"+"操作，它是在普通加法操作的基础上，将结果对集合中元素个数求余
        """
        if self.order != other.order:
            raise TypeError("不能对两个不同有限域集合的元素执行+操作")
        #先做普通加法，然后在结果基础上相对于集合元素的个数做求余运算
        num = (self.num + other.num) % self.order
        """
        这里使用__class__而不是LimitFieldElemet是为了后面实现类的继承考虑，
        后面我们实现的对象需要继承与这个类
        """
        return self.__class__(num, self.order)

    def __mul__(self, other):
        """
        有限域元素进行"*"操作时，先执行普通的乘法操作，然后将结果针对集合元素的个数进行求余
        """
        if self.order != other.order:
            raise TypeError("不能对两个不同有限域集合的元素执行*操作")

        num = (self.num * other.num) % self.order
        return self.__class__(num, self.order)

    def __pow__(self, power, modulo=None):
        """
        指数操作是先执行普通四则运算下的指数操作，再将所得结果针对集合元素个数求余
        """
        while power < 0:
            power += self.order
        num = pow(self.num, power, self.order)
        return self.__class__(num, self.order)

    def __truediv__(self, other):
        if self.order != other.order:
            raise TypeError("不能对两个不同有限域集合的元素执行*操作")
        #通过费马小定理找到除数的对应元素
        negative = other ** (self.order - 2)
        num = (self.num * negative.num) % self.order
        return self.__class__(num, self.order)


"""
a = LimitFieldElement(3, 13)
b = LimitFieldElement(12, 13)
c = LimitFieldElement(10, 13)
print(a * b == c)

a = LimitFieldElement(3, 13)
b = LimitFieldElement(1, 13)
print(a ** 3 == b)
"""

a = LimitFieldElement(3, 13)
#由于(7 * 2) % 13 = 1，因此元素3 "/" 7 等价余 3 "*" 2, 因此 3 "/" 7 = 3 "*" 2 = 6
b = LimitFieldElement(7, 13)
c = LimitFieldElement(6, 13)

print(a / b == c)



