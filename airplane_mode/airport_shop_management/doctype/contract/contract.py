# Copyright (c) 2024, Rangubha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Contract(Document):


	def save(self, *args, **kwargs):
		print("save----------------, ", self.__dict__)
		# a = frappe.get_doc({"doctype":"TestSchedular", "text_data":"random_str"})
		# a.insert()
		# frappe.db.commit()
		# total_amount = self.rent		
		rent_data = {'tenant': self.tenant, "shop": self.shop, "payment_date": frappe.utils.getdate(), "amount":int((frappe.utils.get_last_day(frappe.utils.getdate()).day-frappe.utils.getdate().day)*self.rent_amount/30)}
		rent_doc = frappe.get_doc({"doctype":"Rent Payment", **rent_data})
		rent_doc.insert()
		frappe.db.commit()
		# rent_doc = frappe.get({""})
		return super().save(*args, **kwargs)
	