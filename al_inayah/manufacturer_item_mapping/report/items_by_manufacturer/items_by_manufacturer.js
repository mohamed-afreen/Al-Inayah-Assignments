// Copyright (c) 2026, afreen jasim and contributors
// For license information, please see license.txt

frappe.query_reports["Items by Manufacturer"] = {
    "filters": [
        {
            "fieldname": "manufacturers",
            "label": "Manufacturer",
            "fieldtype": "Link",
            "options": "Manufacturers"
        },
        {
            "fieldname": "item_code",
            "label": "Item",
            "fieldtype": "Link",
            "options": "Item"
        },
        {
            "fieldname": "gtin",
            "label": "GTIN",
            "fieldtype": "Data"
        }
    ]
};
