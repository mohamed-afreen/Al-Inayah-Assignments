// Copyright (c) 2026, afreen jasim and contributors
// For license information, please see license.txt

frappe.query_reports["Agency Lead Times"] = {
    "filters": [
        {
            "fieldname": "agency",
            "label": "Agency",
            "fieldtype": "Link",
            "options": "Agency"
        },
        {
            "fieldname": "item",
            "label": "Item",
            "fieldtype": "Link",
            "options": "Item"
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "\nActive\nInactive"
        }
    ]
};