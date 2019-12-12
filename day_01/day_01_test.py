import unittest
from got_fuel_01 import fuel_required_for_module, compute_total_fuel_required
from got_fuel_02 import added_fuel_required_for_module, is_further_fuel_required, compute_total_additional_fuel_required

class ModuleFuelRequiredTestCase(unittest.TestCase):
    def test_for_one_module(self):
        required_fuel = fuel_required_for_module(12)
        self.assertEqual(required_fuel, 2)

    def test_for_modules(self):
        sampleInput = [83326,84939,135378]
        required_fuel = compute_total_fuel_required(sampleInput)
        self.assertEqual(required_fuel, 101208)

    def test_for_one_module_additional_fuel_is_not_req(self):
        required_fuel = added_fuel_required_for_module(14)
        is_more_required = is_further_fuel_required(required_fuel)
        self.assertFalse(is_more_required)
        self.assertEqual(required_fuel, 2)

    def test_for_one_module_additional_fuel_is_req(self):
        required_fuel = added_fuel_required_for_module(1969)
        is_more_required = is_further_fuel_required(required_fuel)
        self.assertTrue(is_more_required)
        self.assertEqual(required_fuel, 966)

    def test_for_modules_additional_fuel(self):
        sampleInput = [83326,84939,135378]
        required_fuel = compute_total_additional_fuel_required(sampleInput)
        self.assertEqual(required_fuel, 151725)

if __name__ == '__main__':
    unittest.main()
