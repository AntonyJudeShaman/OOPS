import streamlit as st

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
    
    def __str__(self):
        return f"{self.model} - {self.price}"
    
class Manager:
    def __init__(self):
        self.carsl = []
        self.usersl = []

m = Manager()

cars = [
    {'model': 'Ford', 'Price': '50'},
    {'model': 'BMW', 'Price': '500'},
    {'model': 'Audi', 'Price': '150'}
]

users = [
    {'name': 'Antony', 'age': 20},
    {'name': 'Jude', 'age': 21},
    {'name': 'Shaman', 'age': 22}
]

for user in users:
    m.usersl.append(User(user['name'], user['age']))

for car in cars:
    m.carsl.append(Car(car['model'], car['Price']))

print("Users:")
for user in m.usersl:
    print(user)
    if user.name=="Jude":
        print("He is jude")

print("Cars:")
for car in m.carsl:
    print(car)

