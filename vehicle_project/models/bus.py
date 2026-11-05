from models.vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, brand, model, year, seats, mar):
        super().__init__(brand, model, year)
        self.seats = seats
        self.mar = mar

    def get_info(self):
        return f"{super().get_info()}, мест: {self.seats}, маршрут: {self.mar}"
    def move(self):
        return "Автобус едет по маршруту"
