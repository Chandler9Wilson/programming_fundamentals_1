# COSC1336, Lab 5, part 3: Demonstrating parameter passing, local scope

# Create a function called add_one(). The function add_one() is simple. It has one input, a
# parameter called number. It defines one local variable called modified. It adds one to number and
# stores the result in modified. Then it prints:
# "  at top of add_one: number=xx, modified=yy"
# This is indented two spaces to show the nested calls.
# Display the value of the original number and it's modified value, not xx and yy.
# After add_one() prints this message, within add_one, call the function times_ten(),
# passing in the parameter modified. It will look like this: times_ten(modified)
# After the return from times_ten(), display the message:
# "  at bot of add_one: number=xx, modified=yy"

# Create another function called times_ten(). Function times_ten() is simple, too. It has one input, a
# parameter called number. It defines one local variable called modified. It multiplies number times 10
# and stores the result in modified. Then it prints:
# "    at top of times_ten: number=xx, modified=yy"
# This is indented four spaces to show the nested calls.
# After times_ten() prints this message, within times_ten, call the function less_100(),
# passing in the parameter modified. It will look like this: less_100(modified)
# After the return from less_100(), display the message:
# "    at bot of times_ten: number=xx, modified=yy"


# Create a third function called less_100(). Function less_100() is trivial. It has one input, a
# parameter called number. It defines one local variable called modified. It subtracts number minus 100
# and stores the result in modified. Then it prints:
# "      in less_100. number=xx, modified=yy"
# This is indented six spaces to show the nested calls.
# The function less_100() does not call anything. There is no further nesting.

    
# Almost done. Now create a function scope(). In scope(), input a number from the user. Store it in
# variable "number".
# Start by displaying the message:
# "at top of scope: number=xx"
# This message has no spaces of indenting, to show it is the initial call.
# Then call all three functions: add_one(number), times_ten(number), less_100(number)
# After calling all 3 functions, one after the other, at the end of scope, again print:
# "at bot of scope: number=xx"

# Run this program on the inputs: 10, 100, 1000.
# Notice how number and modified are changed and restored as the flow of control passes
# from the caller to the callee and the value is passed into the various functions.
 
# Call the scope function here.

# When you combine this into one menu-driven program, the function scope() here
# becomes the function scope() in the startup code. Copy / paste the code into the
# menu-driven loop shell program.
