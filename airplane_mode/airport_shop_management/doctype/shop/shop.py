# Copyright (c) 2024, Rangubha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Shop(Document):
	# pass
    def before_save(self):
        self.area = self.height*self.width
        # self.route = f'shop/{self.name.lower().replace(" ","-")}'
		# return super().save(*args, **kwarg)
"""
SELECT
    a.name AS airport_name,
    SUM(CASE WHEN s.status = 'Occupied' THEN 1 ELSE 0 END) AS occupied_count,
    SUM(CASE WHEN s.status = 'Available' THEN 1 ELSE 0 END) AS available_count
FROM
    `tabAirport` a
LEFT JOIN
    `tabShop` s ON a.name = s.airport
GROUP BY
    a.name;

"""