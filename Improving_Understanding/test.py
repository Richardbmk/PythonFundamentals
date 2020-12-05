class Vehicle:
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4
    
    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print('The {} {} goes VROOMM'.format(self.color, self.manuf))
        else:
            print('The {} {} sputters out of gas'.format(self.color, self.manuf))

class Car(Vehicle):

    def radio(self):
        print('Rockin TUnes!')

    def windows(self):
        print('Ahhh.. fresh air!')

class MotorCycle(Vehicle):
    
    def helmet(self):
        print('Nice and safe')

class Ecar(Car):

    def drive(self):
            print('The {} {} goes shhh'.format(self.color, self.manuf))

my_ecar = Ecar('Red', 'Opel')


my_ecar.windows()
my_ecar.radio()
my_ecar.drive()
print(my_ecar.gas)