# Copyright (c) 2026, afreen jasim and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Manufacturer",
            "fieldname": "manufacturers",
            "fieldtype": "Link",
            "options": "Manufacturers",
            "width": 200
        },
        {
            "label": "Item Count",
            "fieldname": "item_count",
            "fieldtype": "Int",
            "width": 120
        }
    ]

    data = frappe.db.sql("""
        SELECT
            mi.manufacturers AS manufacturers,
            COUNT(mi.name) AS item_count
        FROM
            `tabManufacturers Item` mi
        GROUP BY
            mi.manufacturers
        ORDER BY
            item_count DESC
    """, as_dict=True)

    return columns, data
