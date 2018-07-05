# Name:
# COSC1336, Lab 6, part 3, on fileIO and exceptions
# This is the startup program.
# It comes from Program 6-26 in the textbook on page 279 (3ed);
# or Program 7-26 on page 283 (2ed).
# See instructions for making improvements and extra credit.


def main() :
    total = 0.0  # Initialize accumulator to 0.0

    try:
        infile = open('sales_data.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(format(total, ',.2f'))

    except IOError:
        print("IO Error occurred trying to read the file.")
    except ValueError:
        print("Non-numeric data found in file:")
    except:
        print("An error occurred.")

main()

# Paste your output below:






