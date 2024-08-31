class Car:
    def __init__(self, make, model, year, mileage=0.0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        if distance > 0:
            self.mileage += distance
        else:
            print("Distance driven must be positive.")

    def get_description(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage:.1f} miles"

# Creating an instance of the Car class
car = Car("Toyota", "Corolla", 2020)

# Simulating a few drives
car.drive(150.5)
car.drive(85.3)
car.drive(200.0)

# Printing the updated description
print(car.get_description())



#   Output:
#   Make: Toyota, Model: Corolla, Year: 2020, Mileage: 435.8 miles