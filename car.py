import streamlit as st

class Car:
    def __init__(self, car_id, make, model, year, rent_per_day):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.rent_per_day = rent_per_day

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - ${self.rent_per_day}/day"

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class RentalManager:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

# Data initialization
car_data = [
    Car(1, "Toyota", "Camry", 2020, 50),
    Car(2, "Honda", "Accord", 2019, 60),
    Car(3, "Ford", "Mustang", 2022, 100),
]

members_data = [
    Person("John Doe", "john@example.com"),
    Person("Jane Smith", "jane@example.com"),
]

rental_manager = RentalManager()
for car in car_data:
    rental_manager.add_car(car)

for member in members_data:
    rental_manager.add_customer(member)

def main():
    st.title("Car Rental System")

    page = st.sidebar.selectbox("Select a page", ["View Available Cars", "Rent a Car", "Membership Details"])

    if page == "View Available Cars":
        view_available_cars()
    elif page == "Rent a Car":
        rent_a_car()
    elif page == "Membership Details":
        view_membership_details()

def view_available_cars():
    st.header("Available Cars")
    for car in rental_manager.cars:
        st.write(car)

def rent_a_car():
    st.header("Rent a Car")
    car_id = st.selectbox("Select a car", [car.car_id for car in rental_manager.cars])
    selected_car = next((car for car in rental_manager.cars if car.car_id == car_id), None)
    if not selected_car:
        st.error("Car not found.")
        return

    st.subheader(f"Car Details: {selected_car.make} {selected_car.model} ({selected_car.year})")
    st.write(f"Price per Day: ${selected_car.rent_per_day}")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    if start_date and end_date:
        rental_days = (end_date - start_date).days + 1
        if rental_days < 1:
            st.warning("End date should be after the start date.")
            return

        total_price = selected_car.rent_per_day * rental_days
        st.success(f"Total Price for {rental_days} days: ${total_price}")

        if st.button("Book Now"):
            st.success("Booking successful!")
            st.write("Please proceed to payment.")
            card_type = st.selectbox("Card Type", ['Debit card', 'Credit card'])
            card_number = st.text_input("Card Number")
            pay = st.button("pay now")
            if pay:
                payment_success()

def payment_success():
    st.success("Payment success!")
    container = st.empty()
    container.write("Thank you for your payment. Your booking is confirmed.")

def view_membership_details():
    st.header("Membership Details")
    for member in rental_manager.customers:
        st.write(f"Name: {member.name}, Email: {member.email}")

if __name__ == "__main__":
    main()
