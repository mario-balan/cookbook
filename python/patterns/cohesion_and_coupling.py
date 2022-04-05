import string
import random


class VehicleInformation:
    brand: str
    electric: bool
    catalogue_price: int

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def determine_tax_percentage(self):
        return 0.05 if self.electric == True else 0.02

    def calculate_tax(self):
        return self.determine_tax_percentage() * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable Tax: {self.calculate_tax()}")


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInformation

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License Plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    vehicleInformation = {}

    def __init__(self): # I'm just initializing the previous vehicles to simulate a database
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Volkswagen Fusca", False, 15000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicleInformation[brand] = VehicleInformation(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicleInformation[brand])


class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # create a vehicle
        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("Volkswagen Fusca")
vehicle.print()
