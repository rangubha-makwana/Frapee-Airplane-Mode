// Copyright (c) 2024, Rangubha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rent Payment", {
	refresh(frm) {
        frm.set_value('issue_date', frappe.datetime.nowdate())
	},
});
