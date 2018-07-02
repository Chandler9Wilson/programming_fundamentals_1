# COSC1336, Lab 5, part 2: Call a tip function multiple times to create a tip table

# Provided is a function that provides one possible payment option.
#
# First, modify the display total due function so that when it is called with the values
# 10.82, 0.15, and 0.0825, it displays the result formatted like this:
# Total due with 15% tip: $12.32
#
# You have to provide some formatting code in the display_total_due function.
# Look at the sections in Chapter 2 on the end and sep arguments to print (pp. 65-67) on
# formatting numbers (pp. 68-69) and on formatting numbers as a percentage (p. 72).
# These page numbers are valid for textbook editions 2, 3, 4.
#
# Second, complete the program so that it reads in the bill for a meal, and then displays
# the total due with a tip rate of 10%, 15%, 20%, and 25%, using the display total due function.
# Since the tax rate should be the same for all of the function calls, you should declare a constant
# variable called TAX_RATE to hold the tax rate of 8.25%. Here is a test interaction with the
# program:
# Enter the bill with tax: $16.24
# Total due with 10% tip: $17.74
# Total due with 15% tip: $18.49
# Total due with 20% tip: $19.24
# Total due with 25% tip: $19.99

# Your program should ask for and get a float in the amount due for a meal
# with tax), and then use the provided function to display the total due with 
# a tip rate of 10%, 15%, 20% and 25%.  The tax rate should be the same in
# each case (8.25%), so it should be stored in a constant called TAX_RATE.

# display_total_due function
#   inputs: the original bill (with tax), the tip rate, and the tax rate
#   output: displays the total due, with tip and tax
#   processing: calculates the total due by computing the tip
#               based on the pre-tax amount and then adding both
#               the tip and the tax to the original bill
def display_total_due(bill_with_tax, tip_rate, tax_rate):
    bill_without_tax = bill_with_tax / (1 + tax_rate)
    tip = bill_without_tax * tip_rate
    total_due = bill_with_tax + tip
    print("Total due with ", tax_rate, "% tip: ", total_due)

# Add a tip_table function here
# Your tip_table function will ask the user for total bill amount, including tax.
# Your tip_table function will then call the display_total_due function 4 times
# with 4 different tip rates.

# Call the tip_table function here.

# When you combine this into one menu-driven program, the function tip_table()
# becomes one of the menu options. After testing, copy / paste the code into the
# menu-driven loop startup program.
