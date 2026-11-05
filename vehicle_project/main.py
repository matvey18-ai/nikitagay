from models.vehicle import Vehicle
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle 
from garage import Garage
from models.bus import Bus
def main():
    car = Car("Toyota", "Camry", 2024, 4)
    print(car.get_info())
    truck = Truck("mer", "A80", 2020, 400)
    print(truck.get_info())
    motorcycle = Motorcycle("BMW", "X1000", 2025, False)
    print(motorcycle.get_info())
    bus = Bus("MOSKVA", "2300", 2025, 35, 211)
    print(bus.get_info())
    car.accelerate(60); car.brake(20); print(car.get_info())
    try:
        car.speed = -10
    except ValueError as error:
        print("Ошибка:", error)
    print(car)
    vehicles = [car, truck, motorcycle, bus]
    for vehicle in vehicles:
        print(vehicle.move())
        print(vehicle.get_info())
    garage = Garage()
    for vehicle in vehicles:
        garage.add_vehicle(vehicle)
    garage.show_all()
    for vehicle in garage.find_by_brand("Toyota"):
        print(vehicle)
    try:
        Vehicle("Generic", "Base", 2020)
    except TypeError as error:
        print("Нельзя создать объект:", error)
if __name__ == "__main__":
    main()