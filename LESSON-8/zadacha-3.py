

class MyListCheck(Exception):
    def __str__(self):
        return 'Только числа!'

def mycheck(num):
    try:
        digit = int(num)
    except ValueError as err:
        raise MyListCheck(err)
    return digit

mylist = []

while True:
    pr = input("\nВведите число или \"stop\" для выхода: ")
    if pr == 'stop':
        break
    try:
        mylist.append(mycheck(pr))
    except MyListCheck as err:
        print(err)
print(mylist)
