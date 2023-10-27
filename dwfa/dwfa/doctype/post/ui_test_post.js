context("Post", () => {
	before(() => {
		cy.login();
		cy.visit("/app");
	});

	it("Category dropdown works as expected", () => {
		cy.create_records([
			{
				doctype: "Category",
				title: "Category 1",
				published: 1,
			},
			{
				doctype: "Blogger",
				short_name: "John",
				full_name: "John Doe",
			},
			{
				doctype: "Post",
				title: "Test Post",
				content: "Test Post Content",
				category: "category-1",
				blogger: "John",
				published: 1,
			},
		]);
		cy.set_value("Settings", "Settings", { browse_by_category: 1 });
		cy.visit("/blog");
		cy.findByLabelText("Browse by category").select("Category 1");
		cy.location("pathname").should("eq", "/blog/category-1");
		cy.set_value("Settings", "Settings", { browse_by_category: 0 });
		cy.visit("/blog");
		cy.findByLabelText("Browse by category").should("not.exist");
	});
});
