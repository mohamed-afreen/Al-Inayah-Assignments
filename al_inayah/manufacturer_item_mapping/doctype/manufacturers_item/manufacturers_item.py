# Copyright (c) 2026, afreen jasim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ManufacturersItem(Document):
	def before_validate(self):
		if not self.part_number:
			self.part_number = self.item_code


	def validate(self):
		self.check_manufacturer_blocked()
		self.validate_unique_mapping()

# ======== Check manufacturer is blocked or not ================
	def check_manufacturer_blocked(self):
		is_blocked = frappe.db.get_value(
			"Manufacturers",
			self.manufacturers,
			"is_blocked"
		)
		if is_blocked:
			frappe.throw("Cannot add item. Manufacturer is blocked.")


# ======== Validate manufacturer and item code ================
	def validate_unique_mapping(self):
		exists = frappe.db.exists(
			"Manufacturers Item",
			{
				"manufacturers": self.manufacturers,
				"item_code": self.item_code,
				"name": ["!=", self.name]
			}
		)
		if exists:
			frappe.throw("This Manufacturer and Item combination already exists.")