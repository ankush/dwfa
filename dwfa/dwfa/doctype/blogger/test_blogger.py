# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe

test_records = frappe.get_test_records("Blogger")


@frappe.whitelist(allow_guest=True)
def create_test_record(**kwargs):
	"""Create test fixtures for integration testin, do not use in production code."""
	frappe.get_doc(kwargs).insert(ignore_permissions=True)
