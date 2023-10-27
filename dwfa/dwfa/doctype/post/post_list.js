frappe.listview_settings["Post"] = {
	add_fields: ["title", "published", "blogger", "category"],
	get_indicator: function (doc) {
		if (doc.published) {
			return [__("Published"), "green", "published,=,Yes"];
		} else {
			return [__("Not Published"), "gray", "published,=,Yes"];
		}
	},
};
