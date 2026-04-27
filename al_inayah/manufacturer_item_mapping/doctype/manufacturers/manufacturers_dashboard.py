from frappe import _

def get_data():
    return {
        "fieldname": "manufacturers",
        "transactions": [
            {
                "label": _("Items"),
                "items": ["Manufacturers Item"]
            }
        ]
    }
