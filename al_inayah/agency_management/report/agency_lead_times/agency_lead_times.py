# Copyright (c) 2026, afreen jasim and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    filters = filters or {}

    columns = [
        {"label": "Agency", "fieldname": "agency", "fieldtype": "Link", "options": "Agency", "width": 150},
        {"label": "Agency Name", "fieldname": "agency_name", "fieldtype": "Data", "width": 150},
        {"label": "Item", "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 150},
        {"label": "Min Order Qty", "fieldname": "min_order_qty", "fieldtype": "Float", "width": 150},
        {"label": "Lead Time", "fieldname": "lead_time_days", "fieldtype": "Int", "width": 120},
    ]

    conditions = "WHERE a.docstatus < 2"
    values = {}

    if filters.get("agency"):
        conditions += " AND a.name = %(agency)s"
        values["agency"] = filters.get("agency")

    if filters.get("item"):
        conditions += " AND ai.item_code = %(item)s"
        values["item"] = filters.get("item")

    if filters.get("status") == "Active":
        conditions += " AND a.is_active = 1"
    elif filters.get("status") == "Inactive":
        conditions += " AND a.is_active = 0"

    query = f"""
        SELECT
            a.name AS agency,
            a.agency_name,
            ai.item_code,
            ai.min_order_qty,
            ai.lead_time_days
        FROM
            `tabAgency` a
        LEFT JOIN
            `tabAgency Item` ai ON ai.parent = a.name
        {conditions}
        ORDER BY
            a.name, ai.item_code
    """

    data = frappe.db.sql(query, values, as_dict=True)
    return columns, data