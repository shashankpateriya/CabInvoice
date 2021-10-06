class Ride:
    def __init__(self, total_time, total_kilometer, ride_type):
        """

        :param total_time: instance of total time
        :param total_kilometer: instance of total km
        :param ride_type: instance of ride type
        """
        self.total_time = total_time
        self.total_kilometer = total_kilometer
        self.ride_type = ride_type
        self.total_fare = self.calculate_fare()

    def calculate_fare(self):
        """
        Method to calculate fare
        :return: total fare
        """

        try:
            if self.ride_type == "normal":
                cost_per_km = 10
                cost_per_min = 1
                minimum_fare = 5
                fare = (self.total_kilometer * cost_per_km) + (self.total_time * cost_per_min)
                self.total_fare = max(fare, minimum_fare)
                return self.total_fare
            elif self.ride_type == "premium":
                cost_per_km = 15
                cost_per_min = 2
                minimum_fare = 20
                fare = (self.total_kilometer * cost_per_km) + (self.total_time * cost_per_min)
                self.total_fare = max(fare, minimum_fare)
                return self.total_fare
        except TypeError:
            print("Enter a valid input")


class User:
    def __init__(self, user_id):
        """

        :param user_id: instance for user id
        """
        self.user_id = user_id
        self.ride_list = []

    @staticmethod
    def get_user_id():
        """
        getting input for user id
        :return: appending the user in user list
        """
        user_id = int(input("Enter new user id:"))
        user = User(user_id)
        invoice_generator.user_list.append(user)
        print("User added successfully")

    def add_ride(self, ride):
        self.ride_list.append(ride)


class InvoiceGenerator:
    def __init__(self):
        self.user_list = []

    def addride(self):
        user_found = False
        check_user_id = int(input("Enter user id to add ride: "))
        for user in self.user_list:
            if user.user_id == check_user_id:
                user_found = True
                total_km = int(input("Enter distance: "))
                total_time = int(input("Enter time: "))
                ride = input("Enter the ride type: ")
                if ride == "normal":
                    user.add_ride(Ride(total_km, total_time, "normal"))
                    print("Added normal ride success")
                elif ride == "premium":
                    user.add_ride(Ride(total_km, total_time, "premium"))
                    print("Added premium ride success")
                else:
                    print("Invalid ride")
        if not user_found:
            print("No user found")

    @staticmethod
    def invoice_generate():
        """
        checking the user in user list
        :return: total fare, number of rides, average fare
        """
        check_user_id = int(input("Enter user id to generate invoice : "))
        for user in invoice_generator.user_list:
            if user.user_id == check_user_id:
                total_fare_of_user = 0
                number_of_rides = len(user.ride_list)
                for ride in user.ride_list:
                    total_fare_of_user += ride.total_fare
                print(f"Total fare of user: {total_fare_of_user}")
                print(f"Number of rides: {number_of_rides}")
                print(f"Average fare: {total_fare_of_user / number_of_rides}")


if __name__ == '__main__':
    invoice_generator = InvoiceGenerator()
    while True:
        print("\n1.Add a user\n"
              "2.Add a ride\n"
              "3.Generate invoice\n"
              "4.Quit\n")
        option = input("Choose option: ")
        if option == "1":
            User.get_user_id()
        elif option == "2":
            invoice_generator.addride()
        elif option == "3":
            invoice_generator.invoice_generate()
        elif option == "4":
            break
        else:
            print("Invalid input")
