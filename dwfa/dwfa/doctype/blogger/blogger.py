# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

# License: MIT. See LICENSE

import frappe
from frappe import _
from frappe.model.document import Document

from dwfa.dwfa.doctype.post.post import clear_blog_cache


class Blogger(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		avatar: DF.AttachImage | None
		bio: DF.SmallText | None
		disabled: DF.Check
		full_name: DF.Data
		short_name: DF.Data
		user: DF.Data
	# end: auto-generated types

	def on_update(self):
		"if user is set, then update all older blogs"

		clear_blog_cache()

		if self.user:
			for blog in frappe.db.sql_list(
				f"""select name from `tabPost` where owner={self.user}
				and ifnull(blogger,'')=''""",
			):
				b = frappe.get_doc("Post", blog)
				b.blogger = self.name
				b.save()

	def validate(self):
		if self.user and not frappe.db.exists("User", self.user):
			# for data import
			frappe.get_doc(
				{"doctype": "User", "email": self.user, "first_name": self.user.split("@", 1)[0]}
			).insert()
