// Copyright (c) 2024, Rangubha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contract", {
	refresh(frm) {
        frm.set_value('date_of_contract', frappe.datetime.nowdate())


        frm.set_query("shop", function() {
            return {"filters":{"status":"Available"}}
        })
        // frappe.call({
        //     method:"airplane_mode.airport_shop_management.airport_shop_management_utils.get_available_shop",
            
        
        //     callback:function(response){
        //         console.log("resp----", response.message)
        //         frm.set_df_property("shop", "options",response.message)
        //         // set_field_options("shop", response.message)
            
        // }});




	},
    duration_of_contract:function(frm){
        frm.set_value('date_of_expiry', frappe.datetime.add_months(frappe.datetime.nowdate(), frm.fields_dict.duration_of_contract.get_value()))
    },
    shop:function(frm){
        console.log("Form-------", frm.doc.shop)
        console.log(frappe.get_doc("Shop", frm.doc.shop))
        frappe.call({
            method:"airplane_mode.airport_shop_management.airport_shop_management_utils.get_shop_amount",
            args:{
                "shop_name": frm.doc.shop,
            },
            
        
            callback:function(response){
                console.log("resp----", response.message)
                frm.set_value("rent_amount", response.message)
                // set_field_options("shop", response.message)
            
        }});
    }
});
