import random

class VehicleBattery:
    def __init__(self):
        self.voltage = random.uniform(11.8, 12.6)
        self.current = random.uniform(-10, 10)
        self.soc = random.uniform(20, 100)

    def get_voltage(self):
        return self.voltage

    def get_current(self):
        return self.current

    def get_soc(self):
        return self.soc

class VehicleEngine:
    def __init__(self):
        self.rpm = random.randint(800, 3000)
        self.temperature = random.uniform(70, 110)

    def get_rpm(self):
        return self.rpm

    def get_temperature(self):
        return self.temperature


import unittest
from test_vehicle import VehicleBattery, VehicleEngine  # Replace 'your_module_name' with the actual module name containing the classes

class TestVehicleBattery(unittest.TestCase):
    def setUp(self):
        self.vehicle_battery = VehicleBattery()

    def test_voltage(self):
        self.assertGreaterEqual(self.vehicle_battery.get_voltage(), 11.8)
        self.assertLessEqual(self.vehicle_battery.get_voltage(), 12.6)

    def test_current(self):
        self.assertGreaterEqual(self.vehicle_battery.get_current(), -10)
        self.assertLessEqual(self.vehicle_battery.get_current(), 10)

    def test_soc(self):
        self.assertGreaterEqual(self.vehicle_battery.get_soc(), 20)
        self.assertLessEqual(self.vehicle_battery.get_soc(), 100)

class TestVehicleEngine(unittest.TestCase):
    def setUp(self):
        self.vehicle_engine = VehicleEngine()

    def test_rpm(self):
        self.assertGreaterEqual(self.vehicle_engine.get_rpm(), 800)
        self.assertLessEqual(self.vehicle_engine.get_rpm(), 3000)

    def test_temperature(self):
        self.assertGreaterEqual(self.vehicle_engine.get_temperature(), 70)
        self.assertLessEqual(self.vehicle_engine.get_temperature(), 110)

if __name__ == "__main__":
    unittest.main()
