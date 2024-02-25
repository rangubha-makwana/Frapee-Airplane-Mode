# Copyright (c) 2023, Rangubha and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestAirplaneTicket(FrappeTestCase):
	def create_airplane_ticket(self, passenger, flight, flight_price, departure_time):
		airplane_ticket = frappe.get_doc({'doctype': 'Airplane Ticket',
								'passenger': passenger,
								'flight':flight,
								'flight_price':flight_price,
								'departure_time':departure_time
								})
		return airplane_ticket
		pass
	# pass
	def test_add_airplane_ticket(self):
		passenger = frappe.get_all("Flight Passenger")[0]["name"]
		flight = frappe.get_all("Airplane Flight")[0]["name"]
		ticket = self.create_airplane_ticket(passenger, flight, 500000, frappe.utils.now_datetime().time())
		ticket.status = "Boarded" 
		ticket.before_save()
		self.assertEqual(ticket.status,"Boarded")
