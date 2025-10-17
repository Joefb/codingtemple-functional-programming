## Instructions
## A retail analytics team needs to process quarterly sales data to generate insights and reports.


sales_data = [
    {"product": "Laptop", "q1": 150, "q2": 180, "q3": 160, "q4": 200},
    {"product": "Mouse", "q1": 300, "q2": 280, "q3": 320, "q4": 350},
    {"product": "Keyboard", "q1": 200, "q2": 190, "q3": 210, "q4": 230},
    {"product": "Monitor", "q1": 80, "q2": 95, "q3": 85, "q4": 110},
    {"product": "Headphones", "q1": 120, "q2": 140, "q3": 130, "q4": 160},
]

# TODO: Use list comprehension to create a new list with annual totals
# Include product name and total_sales
# [{'product': <product name>, 'total_sales': q1 + q2 + q3 + q4}]

annual_sales = [
    {
        "product": item["product"],
        "total_sales": item["q1"] + item["q2"] + item["q3"] + item["q4"],
    }
    for item in sales_data
]

# Test your result
print("Annual Sales Totals:")
for item in annual_sales:
    print(f"  {item['product']}: {item['total_sales']} units")
