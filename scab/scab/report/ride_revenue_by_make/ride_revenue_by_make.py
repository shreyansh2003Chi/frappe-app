import frappe
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count, Sum


def execute(filters=None):
    columns = get_columns()
    data = get_data()
    note="This is a join table data of the Vehicle and Ride Invoice table and the Pie Chart is Generated..."
    chart_data=get_chart_data(data)
    return columns, data, note,chart_data


def get_columns():
    return [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "fieldname": "rides",
            "label": "Rides",
            "fieldtype": "Int",
            "width": 120,
        },
        {
            "fieldname": "revenue",
            "label": "Revenue",
            "fieldtype": "Currency",
            "width": 150,
        },
    ]


def get_data():
    invoice = DocType("Ride Invoice")
    vehicle = DocType("Vehicle")

    return (
        frappe.qb.from_(invoice)
        .join(vehicle)
        .on(invoice.vehicle == vehicle.name)
        .select(
            vehicle.make,
            Count(invoice.name).as_("rides"),
            Sum(invoice.total_amount).as_("revenue"),
        )
        .groupby(vehicle.make)
    ).run(as_dict=True)


def get_chart_data(data):
    labels = []
    values = []

    for row in data:
        labels.append(row["make"])
        values.append(float(row["revenue"] or 0))

    return {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "values": values
                }
            ],
        },
         "type": "pie",
         "colors": ["#7cd6fd", "#743ee2", "#5e64ff"],
         "height": 300
    }