from frappe.model.document import Document

class RideInvoice(Document):
    def before_save(self):
        self.set_total_amount()

    def set_total_amount(self):
        total_distance = 0

        for item in self.items:
            total_distance += item.distance or 0

        self.total_amount = total_distance * (self.rate_per_km or 0)