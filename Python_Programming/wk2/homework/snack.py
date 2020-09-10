# Michael Garcia, ET574
# Vending Machine, snack dispenser

# We initialize and define all values related to each item
chocolateBar = 2.75
potatoChip = 2.50
sugarCookie = 1.75
pretzel = 1.25

# This variable is constant therefore all letters are UPPERCASE
SALES_TAX = .0875

# foodList is defined, these are the food names we want to print out
# foodValues is defined, these are the amount each item costs
# subTotal simply sums the values inside foodValues
# spacer is defined to make the code look cleaner
foodList = ['Chocolate bar', 'Potato chip', 'Sugar cookie', 'Pretzel']
foodValues = [chocolateBar, potatoChip, sugarCookie, pretzel]
subTotal = sum(foodValues)
spacer = ":\t\t$"

# In order to reduce work, a loop is added to print each item until all values in the list are exhausted
# For every item printed, it is removed from the list using pop()
# Inside the loop, the foodValueString does multiple conversions in order to achieve consistent results
# foodValues are integers which are then converted into floats defined into f-strings
for foodValue in foodValues:
    foodValueString = f"{foodValue:.2f}"
    print(foodList.pop(0) + spacer + foodValueString)
print(f"Subtotal{spacer}{subTotal}")

# Tax is calculated, displayed, then added to the subtotal
taxCalculation = subTotal*SALES_TAX
totalDue = taxCalculation+subTotal
print(f"Tax:\t\t\t${taxCalculation:.2f}")
# print("--------------\t\t-----\n")
delimiter = '-'
print(f"{delimiter * 20}\t\t-----\n")
print(f"Total:\t\t\t${totalDue:.2f}")
