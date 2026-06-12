// Copyright (c) 2026, JSCA and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
    refresh(frm) {
        if (frm.doc.status === "Pending") {
            frm.add_custom_button("Accept", () => {
                //frm.set_value("status", "Accepted");
                frappe.new_doc("Ride Invoice",{
                    "booking": frm.doc.name
                });
                frm.save();
            }, "Actions");

            frm.add_custom_button("Reject", () => {
                frm.set_value("status", "Rejected");
                frm.save();
            }, "Actions");
        }
    },
});
