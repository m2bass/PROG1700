# WXXXXXXX-PROG1700-Assignment_Order and Customer Management System_in_Python3.py

# Data Setup
customers = {}

# Function Definitions
def add_customer():
    name = input("Enter customer name: ")
    contact = input("Enter customer contact number: ")

    customer_id = len(customers) + 1
    orders = []

    customer_data = {'name': name, 'contact': contact, 'orders': orders}
    customers[customer_id] = customer_data

    print(f"Customer {name} added successfully!")

def place_order(customer_id, product_name, quantity, unit_price):
    order_id = len(customers[customer_id]['orders']) + 1
    total_cost = quantity * unit_price

    order_data = {'order_id': order_id, 'product_name': product_name, 'quantity': quantity, 'total_cost': total_cost}
    customers[customer_id]['orders'].append(order_data)

    print(f"Order placed successfully!")

def generate_customer_report(customer_id):
    customer_data = customers.get(customer_id)

    if customer_data:
        print(f"\nCustomer Report for {customer_data['name']}:")
        print(f"  Contact: {customer_data['contact']}")
        print(f"  Total Spending: ${sum(order['total_cost'] for order in customer_data['orders']):.2f}")
        print("  Orders:")
        for order in customer_data['orders']:
            print(f"    Order ID: {order['order_id']} | Product: {order['product_name']} | "
                  f"Quantity: {order['quantity']} | Total Cost: ${order['total_cost']:.2f}")
    else:
        print("Customer not found.")

def generate_all_reports():
    for customer_id in customers:
        generate_customer_report(customer_id)

# Menu Setup
def display_menu():
    print("\nOrder and Customer Management System Menu:")
    print("\n1. Add Customer\n2. Place Order\n3. Generate Customer Report\n4. Generate All Customer Reports\n5. Exit")

# Processing User Input
while True:
    display_menu()
    user_choice = input("\nEnter your choice (1-5): ")

    if user_choice == '1':
        add_customer()
    elif user_choice == '2':
        customer_id = int(input("Enter customer ID: "))
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        unit_price = float(input("Enter unit price: "))
        place_order(customer_id, product_name, quantity, unit_price)
    elif user_choice == '3':
        customer_id = int(input("Enter customer ID: "))
        generate_customer_report(customer_id)
    elif user_choice == '4':
        generate_all_reports()
    elif user_choice == '5':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
