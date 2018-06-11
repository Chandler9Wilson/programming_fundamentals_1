# Name:
# COSC1336, Lab 2, 4 parts:
#   part 1: Compute MPG
#   part 2: Convert temperature
#   part 3: Stock sale
#   part 4: Draw initials using turtle graphics
#
# Part 1: Compute the mileage for a car.
#   Ask the user for all values.
#   Format mileage amounts to appear like: xx.x
#   Run at least two test cases.

print("Lab 2: Part 1: compute MPG;     Part 2: convert temp;")
print("       Part 3: stock gain/loss; Part 4: draw initials.\n")

print("This part computes gas mileage.")
# Ask for and get the vehicle make and model. These are separate items.
# Ask for and get the amount of miles traveled.
# Ask for and get the number of gallons used.
# Calculate the gas mileage.
# Output the results.
# Include: vehicle make and model, miles traveled, gallons used, mileage.
print("Drive safely.\n")


# Part 2: Convert temperature units from celsius to fahrenheit
#   Ask the user for all values.
#   Format temperature amounts to appear like: xx.x
#   Run at least two test cases.
print("This part performs a temperature unit conversion from celsius to fahrenheit.")
# Ask for and get celsius temperature
# Convert celsius temperature to fahrenheit
# Display result
print("Enjoy the great outdoors.\n")


# Part 3: Compute gain (or loss) on security transaction
#   Ask the user for all values (see textbook)
#   Perform stock transaction, buy and sell, show profit/loss
#   Format dollar amounts to appear like: $1,234.56
#   Run test case with this data:
#     buy 2000 shares at $40 per share, commission is 3%
#     sell 2000 shares at $42.75, commission is 3%
print ("This part computes the result of a stock transaction.")
# put your new code here
print ("Buy high, sell higher, make money, spend wisely.\n")


if False: # Change False to True when ready to work on Part 4
  # Part 4: Write initials on screen using Python Turtle graphics
  #
  # Using python turtle graphics, draw initials on the screen
  # My initials are 'PT' <change this to your initials>
  #
  # Provided: Startup code that draws instructor's initials
  # Modify this startup code to draw your initials:
  #   Two letters is enough. Draw just one if it is taking too long.
  #   Use straight lines and circles
  #   Use penup to position pen, pendown to start drawing
  #   Subdivide each portion into "paragraphs"
  #   Drawing should complete within 5 seconds
  #   Drawing should be inside a box of 400 x 400 pixels
  #   Comment what you are doing

  print("This part draws my initials.")
  import turtle

  turtle.pencolor('blue')  # Use favorite color
  turtle.pensize(3)        # write with bold strokes!

  # circle for top portion of 'P'
  turtle.penup()         # don't draw anything while positioning pen
  turtle.goto(0, 200)    # move up from (0, 0) to bottom center of where circle will be
  turtle.pendown()       # ready to draw
  turtle.circle(50)      # draw a circle for top of 'P'
  turtle.penup()         # stop showing pen

  # tall vertical line for stem of 'P'
  turtle.goto(-50, 250)  # move pen to left, middle arc of circle
  turtle.pendown()       # ready to draw
  turtle.right(90)       # point pen downwards
  turtle.forward(200)    # draw stem of 'P'
  turtle.penup()         # stop showing pen

  # Top horizontal line of 'T'
  turtle.goto(60, 300)   # move pen to near top of 'P', but spaced to the right
  turtle.setheading(0)   # face rightward
  turtle.pendown()       # ready to draw
  turtle.forward(200)    # draw horizontal line, top of 'T' to the right
  turtle.penup()         # stop showing pen

  # Middle Vertical line of 'T'
  turtle.goto(160, 300)  # Move pen to middle of top of 'T'
  turtle.setheading(270) # point down
  turtle.pendown()       # ready to draw
  turtle.forward(250)    # draw vertical line, middle of 'T', going down
  turtle.penup()         # stop showing pen

  turtle.write('   PT is for Paul Thayer, Good-bye!')
  turtle.hideturtle()    # hide turtle to see initials clearly 

  print("End of turtle lab to draw my initials.")



# Paste your output for parts 1, 2, and 3 below:

