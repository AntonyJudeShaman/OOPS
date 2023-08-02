class Car:
    def __init__(self, car_id, make, model, year, rent_per_day):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.rent_per_day = rent_per_day

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - Rent per day: ${self.rent_per_day}"


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email