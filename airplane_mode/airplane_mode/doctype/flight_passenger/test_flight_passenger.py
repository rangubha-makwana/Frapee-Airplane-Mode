# Copyright (c) 2023, Rangubha and Contributors
# See license.txt

from frappe.tests.utils import FrappeTestCase
import frappe

class TestFlightPassenger(FrappeTestCase):

    def create_passenger(self, first_name, last_name=None):
        passenger = frappe.get_doc({
            'doctype': 'Flight Passenger',
            'first_name': first_name,
            'last_name': last_name
        })
        return passenger

    def test_full_name_with_last_name(self):
        # Create a passenger with both first and last name
        passenger = self.create_passenger('John', 'Doe')
        passenger.before_save()
        self.assertEqual(passenger.full_name, 'John Doe')

    def test_full_name_without_last_name(self):
        # Create a passenger with only first name
        passenger = self.create_passenger('Alice')
        passenger.before_save()
        self.assertEqual(passenger.full_name, 'Alice')


# class TestFlightPassenger(FrappeTestCase):
# 	pass
