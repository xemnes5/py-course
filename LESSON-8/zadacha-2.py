

class MyDivZero(Exception):
    def __str__(self):
        return '-----На ноль не делим!-----'

def mydiv():
    num1, num2 = (int(x) for x in input("\nВведите числа a и b через пробел : ").split())
    if num2 == 0:
        raise MyDivZero
    else:
        return num1/num2

while True:
    try:
        print(mydiv())
    except MyDivZero as err:
        print(err)
