
class Garage:
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)
    def show_all(self):
        for vehicle in self.vehicles:
            print(vehicle)
    def find_by_brand(self, brand):
        return [x for x in self.vehicles if x.brand == brand]
    