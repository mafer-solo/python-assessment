import csv  # Import the CSV module (not used in this code but can be useful for reading/writing CSV files)

# Define the car data as a list of dictionaries
cars = [
    {"car": "Toyota", "price": "20000", "color": "Red", "best seller": "Yes"},
    {"car": "Honda", "price": "22000", "color": "Blue", "best seller": "No"},
    {"car": "Ford", "price": "18000", "color": "Black", "best seller": "Yes"},
    {"car": "BMW", "price": "35000", "color": "White", "best seller": "No"},
    {"car": "Kia", "price": "17000", "color": "Green", "best seller": "Yes"}
]

# Function to generate a sales report based on the car data
def generate_report(cars):
    total_price = 0  # To store the sum of car prices
    highest_price = 0  # To keep track of the highest price
    best_seller_count = 0  # To count how many cars are best sellers
    most_expensive_car = ""  # To store the name of the most expensive car
    valid_entries = 0  # To count valid price entries

    # Loop through each car dictionary in the list
    for car in cars:
        try:
            # Convert the price to a float (in case it's a string)
            price = float(car["price"])
            total_price += price  # Add price to total
            valid_entries += 1  # Count this as a valid price

            # Check if this car is the most expensive so far
            if price > highest_price:
                highest_price = price
                most_expensive_car = car["car"]

            # Count if the car is marked as a best seller
            if car["best seller"].strip().lower() == "yes":
                best_seller_count += 1

        except ValueError:
            # Handle cases where the price isn't a valid number
            print(f"Invalid price for {car['car']} — skipping this entry.")

    # Calculate the average price of all valid car entries
    average_price = round(total_price / valid_entries, 2) if valid_entries else 0

    # Prepare the report content as a list of strings
    report_lines = [
        "Car Sales Summary Report",
        "-------------------------",
        f"Average Price: ${average_price}",
        f"Most Expensive Car: {most_expensive_car} at ${highest_price}",
        f"Total Best Sellers: {best_seller_count}",
        "",
        "Car List:",
    ]

    # Add each car’s details to the report
    for car in cars:
        report_lines.append(
            f"- {car['car']} | ${car['price']} | {car['color']} | Best Seller: {car['best seller']}"
        )

    # Write the report to a text file
    with open("car_sales_report.txt", "w") as file:
        for line in report_lines:
            file.write(line + "\n")  # Write each line to the file

    print("Report saved to car_sales_report.txt")  # Confirm report creation

# Run the report generation function
generate_report(cars)
