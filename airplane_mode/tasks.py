import frappe
from frappe.utils.background_jobs import enqueue
import random
import string


def cron():
    sample_txt = "Hello, Test Cron"
    print(sample_txt)
    random_str = ''.join(random.choices(string.ascii_letters, k=5))
    a = frappe.get_doc({"doctype":"TestSchedular", "text_data":random_str})
    a.insert()
    frappe.db.commit()


    # email_args = {
    #     "recipients": ["rangubhamakwana@gmail.com"],
    #     "message": ("Please see attachment"),
    #     "subject": 'Test EMAIL send',
    #     # "attachments": [frappe.attach_print(self.doctype, self.name, file_name=self.name)],
    #     # "reference_doctype": self.doctype,
    #     # "reference_name": self.name
    #     }


    todays_contract = frappe.get_all("Contract", filters={"contract_status":"On Going","date_of_expiry":[">",frappe.utils.getdate()],"date_of_contract":["=",frappe.utils.getdate()]}, fields=["tenant", "rent_amount", "date_of_expiry", "date_of_contract", "shop"])
    for contract in todays_contract:
        print(contract, "<----------Contract")
        tenant_obj = frappe.get_doc("Tenant", contract.tenant)
        # rent_data = {'tenant': contract.tenant, "shop": contract.shop, "payment_date": frappe.utils.getdate(), "amount":int((frappe.utils.get_last_day(frappe.utils.getdate()).day-frappe.utils.getdate().day)*self.rent_amount/30)}
        previous_month_payment = frappe.get_all("Rent Payment", filters={"tenant": contract.tenant, "issue_date":["=",frappe.utils.add_months(frappe.utils.getdate(),-1)]})
        if previous_month_payment:
           previous_month_rent_payment_obj = frappe.get_doc("Rent Payment", previous_month_payment[0]["name"])
           if previous_month_rent_payment_obj.status == "Unpaid":
            jinja_data = {"tenant_name":contract.tenant, "month": previous_month_rent_payment_obj.issue_date.strftime("%B %Y"), "last_date":frappe.utils.add_days(frappe.utils.getdate(),7)}
            email_args_unpaid = {
            "recipients": [tenant_obj.email],
            "message": ("Please see attachment"),
            "subject": 'Unpaid Rent Payment',
            "template":"rent_due",
            "args":{**jinja_data}
            }
            enqueue(method=frappe.sendmail, queue='long', timeout=4000, is_async=True,**email_args_unpaid)
        current_month_unpaid = frappe.get_all("Rent Payment", filters={"status":"Unpaid", "tenant": contract.tenant})
        print(current_month_unpaid, "<---------un paid contract")
        if current_month_unpaid:
            rent_data = {'tenant': contract.tenant, "shop": contract.shop, "issue_date": frappe.utils.getdate(), "amount":contract.rent_amount, "issue_date": frappe.utils.getdate()}
            rent_doc = frappe.get_doc({"doctype":"Rent Payment", **rent_data})
            rent_doc.insert()
            frappe.db.commit()
            print("rent_doc====", rent_doc)
            print("rent_doc====", rent_doc.__dict__)
            shop = frappe.get_doc("Shop", contract.shop)
            airport = frappe.get_doc("Airport", shop.airport)
            jinja_obj = {"shop_name": shop.shop_name, "shop_number":shop.shop_number, "airport": airport.name, "tenant_name": contract.tenant, "contract_end_date": contract.date_of_expiry, "rent_amount": contract.rent_amount, "issue_date":rent_doc.issue_date}
            email_args = {
            "recipients": [tenant_obj.email],
            "message": ("Please see attachment"),
            "subject": 'Rent Payment Due',
            "template":"rent_due",
            "args":{**jinja_obj}
            }
            enqueue(method=frappe.sendmail, queue='long', timeout=4000, is_async=True,**email_args)



