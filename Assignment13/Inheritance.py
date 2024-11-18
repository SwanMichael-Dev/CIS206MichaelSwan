import unittest

class Vehicle:
  
    def __init__(self, make, model, year):
 
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
     
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
 
    def __init__(self, make, model, year, num_doors):
   
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_num_doors(self):
    
        return self.num_doors

class SUV(Vehicle):
  
    def __init__(self, make, model, year, cargo_capacity):
 
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def get_cargo_capacity(self):
      
        return self.cargo_capacity

class Truck(Vehicle):
   
    def __init__(self, make, model, year, towing_capacity):

        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_towing_capacity(self):
       
        return self.towing_capacity

class TestVehicle(unittest.TestCase):
  
    def test_vehicle_init(self):
    
        vehicle = Vehicle("Toyota", "Camry", 2023)
        self.assertEqual(vehicle.make, "Toyota")
        self.assertEqual(vehicle.model, "Camry")
        self.assertEqual(vehicle.year, 2023)

    def test_vehicle_get_info(self):
      
        vehicle = Vehicle("Honda", "Civic", 2022)
        self.assertEqual(vehicle.get_info(), "Make: Honda, Model: Civic, Year: 2022")

    def test_car_init(self):
        
        car = Car("Ford", "Mustang", 2024, 4)
        self.assertEqual(car.make, "Ford")
        self.assertEqual(car.model, "Mustang")
        self.assertEqual(car.year, 2024)
        self.assertEqual(car.num_doors, 4)

    def test_car_get_num_doors(self):
      
        car = Car("Chevrolet", "Corvette", 2023, 2)
        self.assertEqual(car.get_num_doors(), 2)

    def test_suv_init(self):
      
        suv = SUV("Subaru", "Outback", 2022, 75.8)
        self.assertEqual(suv.make, "Subaru")
        self.assertEqual(suv.model, "Outback")
        self.assertEqual(suv.year, 2022)
        self.assertEqual(suv.cargo_capacity, 75.8)

    def test_suv_get_cargo_capacity(self):
      
        suv = SUV("Toyota", "RAV4", 2023, 69.8)
        self.assertEqual(suv.get_cargo_capacity(), 69.8)

    def test_truck_init(self):
        
        truck = Truck("Ford", "F-150", 2024, 7700)
        self.assertEqual(truck.make, "Ford")
        self.assertEqual(truck.model, "F-150")
        self.assertEqual(truck.year, 2024)
        self.assertEqual(truck.towing_capacity, 7700)

    def test_truck_get_towing_capacity(self):
        
        truck = Truck("Chevrolet", "Silverado", 2023, 8200)
        self.assertEqual(truck.get_towing_capacity(), 8200)

if __name__ == "__main__":
    unittest.main()