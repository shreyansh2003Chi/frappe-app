# Copyright (c) 2026, JSCA and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
    def get_context(self, context):
        context.add_breadcrumbs = True
        context.no_cache = True
