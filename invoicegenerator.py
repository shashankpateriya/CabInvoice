class CabInvoice:
    def __init__(self):
        self.cost_per_km = 10
        self.cost_per_min = 1
        self.minimum_fare = 5

    def calculate_fare(self, distance, time):
        total_fare = (distance * self.cost_per_km) + (time * self.cost_per_min)
        return max(total_fare, self.minimum_fare)
