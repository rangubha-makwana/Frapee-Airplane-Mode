// Copyright (c) 2023, Rangubha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button("Action",()=>{
            frappe.prompt({
                label: 'Seat Number',
                fieldname:"seat_number",
                fieldtype:"Data",
                reqd:1,
            },(data)=>{
                frm.set_value("seat", data.seat_number)
                frm.save()
            })
        })
	},
});
