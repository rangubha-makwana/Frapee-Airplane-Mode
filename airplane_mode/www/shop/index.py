import frappe

def get_context(context):
    context.list_of_airport = frappe.db.sql("""select a.name as airport, s.shop_name, s.shop_number from `tabAirport` a LEFT JOIN `tabShop` s on s.airport=a.name;""", as_dict=1)
    # context.shops = frappe.get_all("Shop", filters={"status":"Available"} fields=[""])
    # return