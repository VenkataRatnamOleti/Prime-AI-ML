class Vehile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehile):
    def __init__(self, brand, model, seats):
         super().__init__(brand, model)
         self.seats = seats

    
class Bike(Vehile):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc

vehicle = Vehile("BMW","X")
car = Car("BMW","X",6)
bike = Bike("BMW","X",125)