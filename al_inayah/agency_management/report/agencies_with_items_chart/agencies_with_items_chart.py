# Copyright (c) 2026, afreen jasim and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Agency",
            "fieldname": "agency",
            "fieldtype": "Link",
            "options": "Agency",
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
            a.name AS agency,
            COUNT(ai.name) AS item_count
        FROM
            `tabAgency` a
        LEFT JOIN
            `tabAgency Item` ai ON ai.parent = a.name
        GROUP BY
            a.name
        ORDER BY
            item_count DESC
    """, as_dict=True)

    return columns, data