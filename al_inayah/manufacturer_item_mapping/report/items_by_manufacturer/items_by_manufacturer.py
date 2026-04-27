# Copyright (c) 2026, afreen jasim and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    filters = filters or {}

    columns = [
        {
            "label": "Manufacturer",
            "fieldname": "manufacturers",
            "fieldtype": "Link",
            "options": "Manufacturers",
            "width": 180
        },
        {
            "label": "Manufacturer Name",
            "fieldname": "manufacturer_name",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "Item Code",
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 150
        },
        {
            "label": "Part Number",
            "fieldname": "part_number",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "GTIN",
            "fieldname": "gtin",
            "fieldtype": "Data",
            "width": 150
        }
    ]

    conditions = "WHERE 1=1"
    values = {}

    if filters.get("manufacturers"):
        conditions += " AND mi.manufacturers = %(manufacturers)s"
        values["manufacturers"] = filters.get("manufacturers")

    if filters.get("item_code"):
        conditions += " AND mi.item_code = %(item_code)s"
        values["item_code"] = filters.get("item_code")

    if filters.get("gtin"):
        conditions += " AND mi.gtin = %(gtin)s"
        values["gtin"] = filters.get("gtin")

    query = f"""
        SELECT
            mi.manufacturers,
            m.manufacturer_name,
            mi.item_code,
            mi.part_number,
            mi.gtin
        FROM
            `tabManufacturers Item` mi
        JOIN
            `tabManufacturers` m ON m.name = mi.manufacturers
        {conditions}
        ORDER BY
            mi.manufacturers, mi.item_code
    """

    data = frappe.db.sql(query, values, as_dict=True)
    return columns, data
