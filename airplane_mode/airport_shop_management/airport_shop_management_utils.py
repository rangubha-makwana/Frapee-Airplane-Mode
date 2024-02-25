import frappe



@frappe.whitelist()
def get_available_shop():
    print("fucntion-calling".center(100,"-"))
    available_shop_list = frappe.get_all("Shop", filters={"status":"Available"}, pluck='name')
    return available_shop_list


@frappe.whitelist()
def get_shop_amount(shop_name):
    shop_doc = frappe.get_doc("Shop", shop_name)
    print("doc-----", shop_doc)

    total_area = shop_doc.height * shop_doc.width
    
    data = frappe.db.sql("""select * from `tabSingles` where doctype="Configurations" and field="rate_of_one_squre" """, as_dict=1)
    print("doc-----", shop_doc)
    return int(data[0].value)*total_area
    # pass