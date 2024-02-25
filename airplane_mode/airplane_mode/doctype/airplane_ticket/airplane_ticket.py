# Copyright (c) 2023, Rangubha and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):

	def validate(self):
		print("VaidATE-------------")
		print(self)
		print(self.__dict__)
		print(self.add_ons)
		print(set(self.add_ons))
		print('|||||||||||||||||||||||')
		seen_items = set()
		unique_list_of_item = []
		for add_on in self.add_ons:
			if add_on.item not in seen_items:
				seen_items.add(add_on.item)
				unique_list_of_item.append(add_on)
			
		self.set("add_ons", unique_list_of_item)

	def before_save(self):
		item_price = []
		for added_item in self.add_ons:
			item_price.append(added_item.amount)
		self.total_amount = self.flight_price + sum(item_price)
		self.gate_number = int(random.choice([1,2,3,4,5]))


	num_list = list(range(1,100))
	char_list  = "ABCDE"
	def before_insert(self):
		self.seat = str(random.choice(self.num_list))+random.choice(self.char_list)
		print("///////", self.__dict__)
		item_price = []
		for added_item in self.add_ons:
			item_price.append(added_item.amount)
		self.total_amount = int(self.flight_price) + sum(item_price)
		# return super().before_insert()
		
	def on_submit(self):
		print("status----")
		print(self.status)
		if self.status!="Boarded":
			frappe.throw(
				title='Error',
				msg='Status is Not Boared',
				exc=frappe.ValidationError
			)

