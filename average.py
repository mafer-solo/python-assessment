import csv

# Define the car data
cars = [
    {"car": "Toyota", "price": "20000", "color": "Red", "best seller": "Yes"},
    {"car": "Honda", "price": "22000", "color": "Blue", "best seller": "No"},
    {"car": "Ford", "price": "18000", "color": "Black", "best seller": "Yes"},
    {"car": "BMW", "price": "35000", "color": "White", "best seller": "No"},
    {"car": "Kia", "price": "17000", "color": "Green", "best seller": "Yes"}
]

def generate_report(cars):
    total_price = 0
    highest_price = 0
    best_seller_count = 0
    most_expensive_car = ""
    valid_entries = 0

    for car in cars:
        try:
            price = float(car["price"])
            total_price += price
            valid_entries += 1

            if price > highest_price:
                highest_price = price
                most_expensive_car = car["car"]

            if car["best seller"].strip().lower() == "yes":
                best_seller_count += 1

        except ValueError:
            print(f"Invalid price for {car['car']} — skipping this entry.")

    average_price = round(total_price / valid_entries, 2) if valid_entries else 0

    # Prepare report content
    report_lines = [
        "Car Sales Summary Report",
        "-------------------------",
        f"Average Price: ${average_price}",
        f"Most Expensive Car: {most_expensive_car} at ${highest_price}",
        f"Total Best Sellers: {best_seller_count}",
        "",
        "Car List:",
    ]

    for car in cars:
        report_lines.append(
            f"- {car['car']} | ${car['price']} | {car['color']} | Best Seller: {car['best seller']}"
        )

    # Write to a .txt file
    with open("car_sales_report.txt", "w") as file:
        for line in report_lines:
            file.write(line + "\n")

    print("Report saved to car_sales_report.txt")

# Run the report
generate_report(cars)
