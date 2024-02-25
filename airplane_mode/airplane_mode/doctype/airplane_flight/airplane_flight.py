# Copyright (c) 2023, Rangubha and contributors
# For license information, please see license.txt
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator):
	def before_save(self):
		modified_route = self.name.lower().replace(" ", "")
		self.route = f"flights/{modified_route}"

	def on_submit(self):
		print("Submit------------")
		self.status="Completed"
		print(self.name)

	# pass
