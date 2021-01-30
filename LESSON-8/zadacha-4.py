

class Sklad:
    pass

class Orgtech:
    def __init__(self, model, vendor, warranty):
        self.model = model
        self.vendor = vendor
        self.warranty = warranty
    
    def __str__(self):
        return f'\nМодель: {self.model} \nВендор: {self.vendor} \nГарантия: {self.warranty} года'


class Printer(Orgtech):
    def __init__(self, *attrs, powders):
        Orgtech.__init__(self, *attrs)
        self.powders = powders
    def __str__(self):
        return f'{super().__str__()} \nПорошка осталось: {self.powders}'

class Scaner(Orgtech):
    def __init__(self, *attrs, scans):
        Orgtech.__init__(self, *attrs)
        self.scans = scans
    def __str__(self):
        return f'{super().__str__()} \nСканов сделано: {self.scans}'

class Xerox(Orgtech):
    def __init__(self, *attrs, xers):
        Orgtech.__init__(self, *attrs)
        self.xers = xers
    def __str__(self):
        return f'{super().__str__()} \nКсерокопий сделано: {self.xers}'

a1 = Printer('NP-1', 'LaserJet', 4, powders=75)
b1 = Scaner('SC-55', 'ScaNNy', 2, scans=230)
c1 = Xerox('XR-2', 'Xerxos', 3, xers=500)
#print(a1.model, a1.vendor)
print(a1)
print(b1)
print(c1)
