# Copyright (c) 2024, Rangubha and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns =[
		{"fieldtype":"Link","label":"Airline", "fieldname":"airline","width":300},
		{"fieldtype":"Currency","label":"Revenue", "fieldname":"revenue","width":300}
	]
	test = frappe.db.sql("""SELECT
         A.name AS airline,
         COALESCE(SUM(T.total_amount), 0) AS revenue
     FROM
         `tabAirline` A
     LEFT JOIN
         `tabAirplane` AP ON A.name = AP.airline
     LEFT JOIN
         `tabAirplane Flight` F ON AP.name = F.airplane
     LEFT JOIN
         `tabAirplane Ticket` T ON F.name = T.flight
     GROUP BY
         A.name;
     """, as_dict=1)
	# data = [
	# 	{"airline":"AirAsia","revenue":1000},
	# 	{"airline":"Indigo","revenue":10000},
	# 	{"airline":"Techno","revenue":100000}
	# ]
	data = test
	chart = {
		"type":"donut",
		"data":{
			"labels":[row.airline for row in data],
			"datasets":[
				{
					"values":[row.revenue for row in data]
				}
			]
		}
	}
	total_revenue = sum(row.revenue for row in data)
	report_summray = [
		{
			"value": total_revenue,
			"indicator":"green" if total_revenue > 0 else "red",
			"label":"Total Revenue",
			"datatype":"Currency"
		},
		# {
		# 	"value": len(data),
		# 	"indicator":"green" if total_revenue > 0 else "red",
		# 	"label":"Total Revenue",
		# 	"datatype":"Currency"
		# }
	]
	return columns, data, None, chart, report_summray
