class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Garage:
    def __init__(self):
        self.cars = []
        self.non_cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        # asking for forgiveness first, not permission -> one of Python idiomatic practices (EAFP)
        if not isinstance(car, Car):
            self.non_cars.append(car)
            raise TypeError(f'An attemp to add a `{car.__class__.__name__}` to the garage, only `Car` objects can be added')
        self.cars.append({
            'make': car.make,
            'model': car.model
        })
    
    def print_inventory(self):
        for car in self.cars:
            print(f'{car["make"]} {car["model"]}')

ford = Garage()

car_12345 = Car('ford', 'fusion')
car_5323323 = Car('ford', 'explorer')
car_85467 = Car('ford', 'boronco')

try:
    ford.add_car(car_12345)
    ford.add_car(car_85467)
    ford.add_car('car_5323323')
    
except TypeError:
    print("one or more items identified as not a car")
finally:
    print(f"There are {len(ford)} in the garage, {len(ford.non_cars)} non cars objects rejected")
print(ford.cars)
print(ford.print_inventory())