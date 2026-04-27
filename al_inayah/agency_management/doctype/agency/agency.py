# Copyright (c) 2026, afreen jasim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Agency(Document):
    def validate(self):
        self.prevent_deactivate_with_items()

    def prevent_deactivate_with_items(self):
        if not self.is_active:
            
            if self.agency_item and len(self.agency_item) > 0:
                frappe.throw("Cannot deactivate Agency because it has linked Agency Items.")


@frappe.whitelist()
def create_supplier(docname):
    agency = frappe.get_doc("Agency", docname)

    if agency.supplier:
        frappe.throw(f"Supplier already linked: {agency.supplier}")

    existing_supplier = frappe.db.exists("Supplier", {"supplier_name": agency.agency_name})

    if existing_supplier:
        agency.supplier = existing_supplier
        agency.save(ignore_permissions=True)
        return existing_supplier

    supplier = frappe.get_doc({
        "doctype": "Supplier",
        "supplier_name": agency.agency_name,
        "supplier_type": "Company",
        "agency": agency.name
    })

    supplier.insert(ignore_permissions=True)
    agency.supplier = supplier.name
    agency.save(ignore_permissions=True)

    return supplier.name