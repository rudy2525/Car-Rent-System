class CarRental:
    def __init__(self):
        self.carfare = {"Hatchback": 50, "Sedan": 70, "Suv": 100}

    def display_fare_detail(self):
            print("cost per day: ")
            print("Hatchback: $", self.carfare["Hatchback"])
            print("Sedan: $", self.carfare["Sedan"])
            print("Suv: $", self.carfare["Suv"])
    def calculate_price(self, type_of_car, number_of_day):
            return self.carfare[type_of_car] * number_of_day
car = CarRental()

while True:
    print("""
    ===== Ru's Car Rental =====
    1. Display fare detail
    2. Request a car 
    3. Exit
    """)
    choice = int(input("Please select a option: "))
    if choice == 1:
        car.display_fare_detail()

    elif choice == 2:
        print("Enter the fare you would like to ride: ")
        type_of_car = input()
        print("Enter the amount of days you would like your ride: ")
        number_of_day = int(input())
        fare = car.calculate_price(type_of_car, number_of_day)
        print("Total amount is $ ", fare)
        print("Thank you for choosing Ru's Car Rental!")
    elif choice == 3:
        print("Thank you for choosing Ru's Car Rental!")
        quit()



