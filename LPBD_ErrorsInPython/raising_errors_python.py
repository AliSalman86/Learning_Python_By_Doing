class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}>"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    
    def add_car(self, car):     # method still under development
        # print("This method is a work in progress...")  #not so good idea
        # raise NotImplementedError("The car add feature is coming soon, cars can't be added to the garage yet!")
        # raising a TypeError when trying to append a car that is not an instance of Car class
        if not isinstance(car, Car):
            raise TypeError(f'An attemp to add a `{car.__class__.__name__}` to the garage, only `Car` objects can be added')
        self.cars.append(car)

ford = Garage()
car = Car('Ford', 'Fusion')  # if this line commented out and line 27 uncommented, then TypeError will be raised 
# ford.add_car('Fusion') # NotImplementedError: The car add feature is coming soon, cars can't be added to the garage yet!
                       # TypeError: An attemp to add a `str` to the garage, only `Car` objects can be added
ford.add_car(car)
print(ford.cars)
print(len(ford))

