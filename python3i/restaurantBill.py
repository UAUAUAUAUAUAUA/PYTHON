# --- Main Menu Data ---
# All three lists must match in order and length.
# This data is now at the top-level (zero indentation)
# so all functions can see it.
#Jamelle,Ben,Yaroslav
menu_english = [
    "Borscht",
    "Pampushky (Garlic Bread)",
    "Varenyky (Dumplings)",
    "Deruny (Potato Pancakes)",
    "Holubtsi (Cabbage Rolls)",
    "Chicken Kyiv",
    "Syrnyky (Cheese Pancakes)",
    "Uzvar (Fruit Drink)",
    "Kvas (Fermented Bread Drink)",
    "Tea (Carpatians Herbal)"
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
    3.99,
    2.99
]

def display_menu():
    """Display restaurant menu with prices."""
    print("═══════ MENU ═══════")
    # This loop will now run 10 times (for index 0 to 9)
    for index in range(len(menu_english)):
        item = menu_english[index]
        price = menu_price[index]
        # This will print "1. Borscht..." up to "10. Tea..."
        print(f"{index + 1}. {item} - ${price:.2f}")
    
    # We add 1 to the length (10 + 1) to get 11
    done_number = len(menu_english) + 1
    # This will print "11. Done ordering"
    print(f"{done_number}. Done ordering")
    print("--------------------")

def get_order():
    """
    Let user order items. Return a list of items ordered
    and a list of their prices.
    """
    ordered_items = []
    ordered_prices = []
    
    # Get the "done" number one time (it will be 11)
    done_number = len(menu_english) + 1
    
    while True:
        display_menu() 
        
        # The prompt will correctly show "1-10" and "11 to finish"
        choice = input(f"Enter the item number to order (1-{done_number-1}) or {done_number} to finish: ")
        
        try:
            choice_num = int(choice)
            
            # This correctly checks for 11
            if choice_num == done_number:
                print("Finishing order...")
                break # Exit the loop
                
            item_index = choice_num - 1
            
            # This correctly checks if the choice is between 0-10
            if 0 <= item_index < len(menu_english):
                ordered_items.append(menu_english[item_index])
                ordered_prices.append(menu_price[item_index])
                print(f"Added {menu_english[item_index]} to your order.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            # This handles if they type 'abc'
            print("Please enter a valid number.")
    return ordered_items, ordered_prices
    
def calculate_subtotal(prices):
    """Calculate and return the subtotal of all prices."""
    return sum(prices)
    
def calculate_tax(subtotal, tax_rate):
    """Calculate and return the tax amount."""
    return subtotal * tax_rate

def calculate_tip(subtotal, tip_percent):
    """Calculate and return the tip amount."""
    # This converts the user's '15' into '0.15'
    return subtotal * (tip_percent / 100)

def calculate_total(subtotal, tax, tip):
    """Calculate and return the final total."""
    return subtotal + tax + tip

def split_bill(total, num_people):
    """Calculate how much each person pays. Return amount per person."""
    # We check if num_people is 0 to avoid a crash
    if num_people > 0:
        return total / num_people
    return total # Return the total if num_people is 0 or less

def display_receipt(items, prices, subtotal, tax, tip, total, num_people, per_person=None):
    """Display a formatted receipt."""
    print("\n════════ RECEIPT ════════")
    
    # 1. Loop through and print all ordered items
    for i in range(len(items)):
        print(f"{items[i]:<25} ${prices[i]:>6.2f}")
    print("-------------------------")

    # 2. Print all the calculated totals
    print(f"{'Subtotal:':<25} ${subtotal:>8.2f}")
    print(f"{'Tax:':<25} ${tax:>8.2f}")
    print(f"{'Tip:':<25} ${tip:>8.2f}")
    print("-------------------------")
    print(f"{'TOTAL:':<25} ${total:>8.2f}")

    # 3. Print the split-bill info, if it exists
    if per_person is not None:
        print(f"\nSplit by {num_people} people")
        print(f"{'Each person pays:':<25} ${per_person:>8.2f}")

# Main program
print("════════════════════════════")
print("Ukrainian Resturant Bill ")
print("════════════════════════════")

TAX_RATE = 0.08  # 8% tax

# 1. & 2. Display menu and Take order
print("Taking your order...")
# We call get_order() which returns two lists
ordered_items_list, ordered_prices_list = get_order()

# Check if the order is empty. If so, quit.
if not ordered_items_list:
    print("No items ordered. Goodbye!")
else:
    # 3. Calculate all amounts
    subtotal_amount = calculate_subtotal(ordered_prices_list)
    tax_amount = calculate_tax(subtotal_amount, TAX_RATE)

    # 4. Ask for tip percentage
    tip_percentage = float(input("Enter tip percentage (e.g., 15): "))
    
    # 5. Calculate tip
    tip_amount = calculate_tip(subtotal_amount, tip_percentage)

    # 6. Calculate total
    total_bill = calculate_total(subtotal_amount, tax_amount, tip_amount)

    # 7. Ask if splitting bill
    num_people = int(input("How many people are splitting? (Enter 1 for no split): "))

    # 8. Calculate split bill
    amount_per_person = None
    if num_people > 1:
        amount_per_person = split_bill(total_bill, num_people)

    # 9. Display receipt
    display_receipt(
        ordered_items_list,
        ordered_prices_list,
        subtotal_amount,
        tax_amount,
        tip_amount,
        total_bill,
        num_people, 
        amount_per_person
    )

    print("\nThank you for dining with us!")