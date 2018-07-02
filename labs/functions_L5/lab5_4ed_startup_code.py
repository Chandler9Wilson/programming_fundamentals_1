# Name:
# COSC1336, Lab 5, startup structure for menu-driven loop
# Currently, these functions don't do anything. They all pass, which is a placeholder.
# Where a pass appears, remove the pass, replace with code.

def intro(): # Part 0. Write intro code. See written instructions for details.
    # The intro part is to practice with 10 function "design patterns"
    #  1) define and call 1 function f1 with: no parameters, no return
    pass

    #  2) define and call 1 function f2 with: 1 parameter, no return.
    pass

    #  3) define and call 1 function f3 with: 2 parameters, no return.
    pass

    #  4) define and call 1 function f4 with: 2 parameters, 1 return.
    pass

    #  5) define and call 1 function f5 with: 2 parameters, 2 returns.
    pass

    #  6) define and call 1 function f6 with: no parameters, 1 return.
    pass

    #  7) define and call 1 function f7 with: no parameters, 2 returns.
    pass

    #  8) define and call 1 function f8 with: 3 keyword parameters, 1 return.
    pass

    #  9) define and call 3 functions: f9, f9a, f9b. f9 calls f9a and f9b. All 0 parameters, 0 return.
    pass

    # 10) define and call 4 function f10, f10a, f10b, f10c. f10 calls f10a, f10a, f10b, f10c. All 0 parameters, 0 return.
    pass

# For the remaining parts, 
def launch(): # Part 1. Get startup code from launch.py (provided)
    pass

def tip_table(): # Part 2. Get startup code from tip_table.py (provided)
    pass

def scope(): # Part 3. Get startup code from scope.py (provided)
    pass

def sort(): # Part 4. No startup code provided. See instructions.
    pass

def ACC(): # Part 5. Extra Credit: no startup code provided. See instructions.
    pass

def main():
    print('Hello. This is cosc1336 lab 5 on functions.')
    while True:
        option =  input('Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? ')
        option=option.lower()
        if option == '0':
            intro()    
        elif option == '1':
            launch()
        elif option == '2':
            tip_table()
        elif option == '3':
            scope()
        elif option == '4':
            sort()
        elif option == '5':
            ACC()           
        elif option == '6' or option == 'q':
            break
        else:
            print('  Invalid option, please try again.')
    print('\nGoodbye')

main()    

# Test all options in one, last test run, and paste your output below:

