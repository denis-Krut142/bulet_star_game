class Car:
    wheels = 4
    rudder = 1
    horsepower = 100
    weight_kg = 1000

    def drive(self):
        speed = self.horsepower * 10 // self.weight_kg
        return speed


a = Car()
a.horsepower = 5000
a.weight_kg = 550

b = Car()
b.horsepower = 300
b.weight_kg = 250
print(a.drive())
print(b.drive())
