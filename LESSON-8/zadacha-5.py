

class Sklad:
    def __init__(self):
        self.skdict = {'printer': {'quant': 0, 'model': None},
                       'scaner': {'quant' : 0, 'model' : None},
                       'xerox': {'quant': 0, 'model': None}
                       }

    def techadd(self, tech):
        print(f'Добавляем на склад {tech.model} {tech.type}')
        self.skdict[tech.type]['quant'] += 1
        self.skdict[tech.type]['model'] = tech.model
        tech.depart = 'Склад'

    def techtrans(self, tech, dest):
        print(f'Перемещаем со склада {tech.model} {tech.vendor} в {dest}')
        self.skdict[tech.type]['quant'] -= 1
        tech.depart = dest

    def __str__(self):
        return f'{self.skdict}'

class Orgtech:
    def __init__(self, model, vendor, techtype):
        self.model = model
        self.vendor = vendor
        self.type = techtype
        self.depart = None

    def __str__(self):
        return f'\nМодель: {self.model} \nВендор: {self.vendor} \nType: {self.type} '
 
    def location(self):
        return f'{self.depart}'

class Printer(Orgtech):
    def __init__(self, *attrs):
        Orgtech.__init__(self,*attrs,techtype='printer')

class Scaner(Orgtech):
    def __init__(self, *attrs):
        Orgtech.__init__(self,*attrs,techtype='scaner')
        
class Xerox(Orgtech):
    def __init__(self, *attrs):
        Orgtech.__init__(self,*attrs,techtype='xerox')

a1 = Printer('NP-1', 'LaserJet')
b1 = Scaner('SC-55', 'ScaNNy')
c1 = Xerox('XR-2', 'Xerxos')
stor = Sklad()
stor.techadd(a1)
stor.techadd(b1)
stor.techadd(c1)
stor.techtrans(a1, 'Отдел печати')
print(f'На складе: \n{stor}')
print(f'Перенесенное устройство находится : {a1.location()}')
#print(b1.location())
