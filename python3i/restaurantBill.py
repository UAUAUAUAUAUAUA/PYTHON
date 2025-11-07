# --- Main Menu Data ---
# All three lists must match in order and length.
# This data is now at the top-level (zero indentation)
# so all functions can see it.

menu_english = [
    "Borscht",
    "Pampushky (Garlic Bread)",
    "Varenyky (Dumplings)",
    "Deruny (Potato Pancakes)",
    "Holubtsi (Cabbage Rolls)",
    "Chicken Kyiv",
    "Syrnyky (Cheese Pancakes)",
    "Uzvar (Fruit Drink)",
    "Kvas (Fermented Bread Drink)"
    ]

menu_price = [
    8.99,
    4.99,
    12.99,
    10.99,
    14.99,
    18.99,
    9.99,
    3.99,
    3.99
]

def display_menu():
    """Display restaurant menu with prices."""
    print("═══════ MENU ═══════")
    for index in range(len(menu_english)):
        item = menu_english[index]
        price = menu_price[index]
        # I fixed the formatting to remove the extra colon
        print(f"{index + 1}. {item} - ${price:.2f}")
    print("--------------------")
    # I removed the extra 'index = 1' and 'number = index + 1' lines
    # as they weren't needed.

def get_order():
    """
    Let user order items. Return a list of items ordered
    and a list of their prices.
    """
    ordered_items = []
    ordered_prices = []
    while True:
        # ----> FIXED: Added the display_menu() call inside the loop
        display_menu() 
        
        choice = input("Enter the item number to order (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        try:
            item_index = int(choice) - 1
            if 0 <= item_index < len(menu_english):
                ordered_items.append(menu_english[item_index])
                ordered_prices.append(menu_price[item_index])
                print(f"Added {menu_english[item_index]} to your order.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Please enter a valid number or 'done'.")
    return ordered_items, ordered_prices
    
def calculate_subtotal(prices):
    """Calculate and return the subtotal of all prices."""
    # YOUR CODE HERE
    def sum_prices(prices):
        total = 0
        for price in prices:
            total += price
        return total
    return sum_prices(prices)
    

def calculate_tax(subtotal, tax_rate):
    """Calculate and return the tax amount."""
    # YOUR CODE HERE
    return subtotal * tax_rate


def calculate_tip(subtotal, tip_percent):
    """Calculate and return the tip amount."""
    # YOUR CODE HERE
    return subtotal * (tip_percent / 100)

def calculate_total(subtotal, tax, tip):
    """Calculate and return the final total."""
    # YOUR CODE HERE
    return subtotal + tax + tip

def split_bill(total, num_people):
    """Calculate how much each person pays. Return amount per person."""
    # YOUR CODE HERE
    return total / num_people

def display_receipt(items, prices, subtotal, tax, tip, total, per_person=None):
    """Display a formatted receipt."""
    # YOUR CODE HERE
    print("\n════════ RECEIPT ════════")

# Main program
print("════════════════════════════")
print("Ukrainian Resturant Bill ")
print("════════════════════════════")

TAX_RATE = 0.08  # 8% tax

# YOUR CODE HERE - Write the main program

# 1. & 2. Display menu and Take order
display_menu()
# We call get_order() which returns two lists
print("Taking your order...")
ordered_items_list, ordered_prices_list = get_order()

# --- FOR TESTING ---
# Let's print the results to see if it worked!
print("\n--- Order Summary ---")
print(f"Items ordered: {ordered_items_list}")
print(f"Prices: {ordered_prices_list}")
# --- END TESTING ---


# 3. Calculate all amounts
calculate_subtotal(ordered_prices_list)
tax_amount = calculate_tax(calculate_subtotal(ordered_prices_list), TAX_RATE)
tip_amount = calculate_tip(calculate_subtotal(ordered_prices_list), tip_percentage)
total_amount = calculate_total(calculate_subtotal(ordered_prices_list), tax_amount, tip_amount)
# (Your next step is to call calculate_subtotal here)
subtotal_amount = calculate_subtotal(ordered_prices_list)

# 4. Ask for tip percentage
tip_percentage = float(input("Enter tip percentage...")) 
# 5. Ask if splitting bill
tip_percentage = float(input("Enter tip percentage (e.g., 15 for 15%): "))
# 6. Display receipt
num_people = int(input("Enter number of people to split the bill (1 for no split): "))