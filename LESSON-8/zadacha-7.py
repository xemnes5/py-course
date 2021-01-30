

class ComplexNumber:
    #r - real part; i - imaginary part
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return ComplexNumber(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        # (a+bi) * (p+qi) = (ap-bq)+(aq+bp)i
        return ComplexNumber(self.r*other.r - self.i*other.i, self.r*other.i + self.i*other.r)

    def __truediv__(self, other):
        # (a+bi) / (p+qi) = ((ap+bq)+(bp-aq)i) / (pp + qq)
        return ComplexNumber((self.r*other.r + self.i*other.i) / (other.r**2 + other.i**2),
                             (self.i*other.r - self.r*other.i) / (other.r**2 + other.i**2))

    def __str__(self):
        return '{}{}{}i'.format(self.r,'+' if self.i >= 0 else '', self.i)


num1 = ComplexNumber(5,-2)
num2 = ComplexNumber(-4,3)
print(f'Косплексное число 1 : {num1}')
print(f'Косплексное число 2 : {num2}')
print(f'Их сумма : {num1+num2}')
print(f'Их разность : {num1-num2}')
print(f'Их произведение : {num1*num2}')
print(f'Их частное (деление) : {num1/num2}')
