// Copyright (c) 2026, afreen jasim and contributors
// For license information, please see license.txt

frappe.ui.form.on('Agency', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button('Create Supplier', function() {
                frappe.call({
                    method: 'al_inayah.agency_management.doctype.agency.agency.create_supplier',
                    args: {
                        docname: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message) {
                            frappe.msgprint('Supplier Created: ' + r.message);
                        }
                    }
                });
            }, 'Create');
        }
    }
});