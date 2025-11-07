# Ask for item names and prices
item1 = input("Enter item 1: ")
price1 = float(input("Enter price 1: "))

item2 = input("Enter item 2: ")
price2 = float(input("Enter price 2: "))

item3 = input("Enter item 3: ")
price3 = float(input("Enter price 3: "))

# Calculate tax at 6%
tax1 = price1 * 0.06
tax2 = price2 * 0.06
tax3 = price3 * 0.06

# Display results
print(item1, "costs $", round(price1, 2), "with tax $", round(tax1, 2))
print(item2, "costs $", round(price2, 2), "with tax $", round(tax2, 2))
print(item3, "costs $", round(price3, 2), "with tax $", round(tax3, 2))
