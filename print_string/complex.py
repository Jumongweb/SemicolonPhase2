class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return self.left + other.left, self.right + other.right

    def __sub__(self, other):
        return self.left - other.left, self.right - other.right

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __gt__(self, other):
        return self.left > other.left and self.right > other.right

    def __iadd__(self, other):
        self.left += other.left
        self.right += other.right
        return complex(self.left, self.right)

    def __isub__(self, other):
        self.left -= other.left
        self.right -= other.right
        return complex(self.left, self.right)

    def __imul__(self, other):
        self.left *= other.left
        self.right *= other.right
        return complex(self.left, self.right)

    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'


c1 = Complex(2, 3)
c2 = Complex(5, 5)
c3 = Complex(2, 3)
m1 = Complex(5, 4)
m2 = Complex(3, 2)

print(c1)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c1 == c3)
print(c2 > c1)
print("I_add")
c1 += c2
print(c1)

c3 -= c2
print(c3)
m1 *= m2
print(m1)