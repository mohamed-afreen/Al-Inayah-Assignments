import frappe

@frappe.whitelist(allow_guest=True)
def get_manufacturer_mappings(item_code):
    if not item_code:
        frappe.throw("item_code is required")

    data = frappe.db.get_all(
        "Manufacturers Item",
        filters={
            "item_code": item_code
        },
        fields=[
            "manufacturers",
            "item_code",
            "part_number",
            "gtin"
        ]
    )

    return {
        "item_code": item_code,
        "mappings": data
    }