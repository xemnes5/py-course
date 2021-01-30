

class Data:
    def __init__(self, dates):
        self.dates = dates
        
    @classmethod
    def meth_1(cls, dates):
        day, month, year = [int(i) for i in dates.split('-')]
        return day, month, year
    
    @staticmethod    
    def meth_2(day, month, year):
        if day not in range(1,32):
            return  'Day is incorrect!'
        elif month not in range(1,13):
            return 'Month is incorrect!'
        elif year not in range(1,2022):
            return 'Year is incorrect!'
        else: return 'Date is OK!'

DATES = ['1-2-2010', '50-10-2020', '20-35-2015', '15-12-2050']

for date in DATES:
    print(f'raw date: {date}')
    print('Meth_1 : ', Data.meth_1(date))
    print('Meth_2 : ', Data.meth_2(*Data.meth_1(date)))
