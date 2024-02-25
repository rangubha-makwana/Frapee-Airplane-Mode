// Copyright (c) 2023, Rangubha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        if(cur_frm.doc.website){
            let linkElement = $('<a>',{
                'href': cur_frm.doc.website,
                'text': 'Visit Website'
            });
            $('.form-sidebar').prepend(linkElement)
        }
        frm.add_custom_button("Action",()=>{

        })
	},
});
