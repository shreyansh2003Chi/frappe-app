from frappe.model.document import Document
import frappe

class Driver(Document):
    pass

    # def before_save(self):
    #     self.full_name = f"{self.first_name} {self.last_name}"

    # def on_trash(self):
    #     frappe.throw("Can't delete")
