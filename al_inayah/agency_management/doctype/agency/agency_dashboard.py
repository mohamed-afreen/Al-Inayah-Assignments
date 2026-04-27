from frappe import _

def get_data():
    return {
        "fieldname": "agency",
        "transactions": [
            {
                "label": _("Related"),
                "items": ["Supplier"]
            }
        ]
    }
