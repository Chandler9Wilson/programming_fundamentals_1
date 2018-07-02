# COSC1336, Lab 5, part 1: Rewrite launch sequence software with functions
#
# Launch a rocket into space.
#
# This program mostly works. It executes the steps required to launch a
# rocket into space. You will improve the program. The output will be the
# same after modification.

# BIG PROBLEM!!! It is written without any functions. It has lots and lots
# of redundant code. Identify common blocks of redundant code. Gather the
# redundant code into functions. Eliminate all unneeded extra code.
# Use parameters if useful. Call your functions from launch(). 

# Arrange your program so all output starts and ends in launch().
# See program 3-3 on pages 93, 94 (2ed), program 5-3 on pages 177, 178 (3ed),
# pages 221, 222 (4ed) to see an example of how your program
# can be organized into multiple functions.
#
# When this part is done and tested, copy / paste the code into the
# menu-driven loop shell program. This part will become the 1)launch option.

print("This program launches a rocket.")
print("start launch sequence")

print("Fill booster fuel tank 1.")
print("  open valve")
print("  pre-freeze tank")
print("  attach filler hose")
print("  pressurize fuel supply")
print("  fill tank")
print("  secure and seal shutoff valve")

print("Fill booster fuel tank 2.")
print("  open valve")
print("  pre-freeze tank")
print("  attach filler hose")
print("  pressurize fuel supply")
print("  fill tank")
print("  secure and seal shutoff valve")

print("Fill booster fuel tank 3.")
print("  open valve")
print("  pre-freeze tank")
print("  attach filler hose")
print("  pressurize fuel supply")
print("  fill tank")
print("  secure and seal shutoff valve")

print("Start engine 1")
print("  ignition sequence start")
print("  start ignition spark generator")
print("  open fuel valve")
print("  verify ignition temperature")
print("  stop ignition spark generator")
print("  engine 1 is started")

print("Start engine 2")
print("  ignition sequence start")
print("  start ignition spark generator")
print("  open fuel valve")
print("  verify ignition temperature")
print("  stop ignition spark generator")
print("  engine 2 is started")

print("3, 2, 1, 0, BLASTOFF!!!")
print("Thank you. Keep looking up!")

def launch() :
    input("Press enter to begin the launch sequence...")
    # locate your function calls (indented) here.
    # When you combine this into one menu-driven program,
    # it takes the place of function launch()

launch()
