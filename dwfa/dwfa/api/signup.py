import frappe


@frappe.whitelist(allow_guest=True)
def request_signup(email_address):
	"""Called from signup page to create a new account request"""
	if frappe.db.exists("User", email_address):
		frappe.throw("User already exists")
	else:
		account_request = frappe.new_doc(
			"Account Request", username=email_address, key=frappe.generate_hash()
		)
		account_request.insert()
		frappe.msgprint("Please check your email address for verification.")


@frappe.whitelist(allow_guest=True)
def validate_signup(key, email, password, first_name):
	"""Called from email verification page, once user calls this API a user is created for them and they can now login."""
	if frappe.db.exists("Account Request", key):
		# valid key
		try:
			new_user = frappe.new_doc("User", email)
			new_user.first_name = first_name
			new_user.set_password(password)
			return new_user.insert()
		except Exception:
			frappe.logger("signups").error(
				f"Failed to create account for {email}, arguments {key=}, {password=}, {first_name=}"
			)
