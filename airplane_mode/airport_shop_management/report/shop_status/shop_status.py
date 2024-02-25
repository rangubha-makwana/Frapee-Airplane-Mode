# Copyright (c) 2024, Rangubha and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
# 	columns =[
# 		{"fieldtype":"Link","label":"Airline", "fieldname":"airline","width":300},
# 		{"fieldtype":"Currency","label":"Revenue", "fieldname":"revenue","width":300}
# 	]
# 	query = frappe.db.sql("""SELECT
#     a.name AS airport_name,
#     SUM(CASE WHEN s.status = 'Occupied' THEN 1 ELSE 0 END) AS occupied_count,
#     SUM(CASE WHEN s.status = 'Available' THEN 1 ELSE 0 END) AS available_count
# FROM
#     `tabAirport` a
# LEFT JOIN
#     `tabShop` s ON a.name = s.airport
# GROUP BY
#     a.name;
# """, as_dict=1)
# 	data = query
# 	chart = {
# 		"type":"donut",
# 		"data":{
# 			"labels":[row.airport_name for row in data],
# 			"datasets":[
# 				{
# 					"values":[row.revenue for row in data]
# 				}
# 			]
# 		}
# 	}
	columns, data = [], []
	return columns, data
