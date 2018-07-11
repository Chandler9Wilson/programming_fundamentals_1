# Name: Chandler Wilson
# Date: 07/10/2018
# COSC1336, Exam 2, 3 parts:
#   part 1: Generate random number file
#   part 2: Improve part 1
#   part 3: Even Odd added to output
from random import randint


def call_show_data():
    file_name = input(
        'What file would you like to see? (exclude .txt): ')

    file_name += '.txt'

    shown = showData(file_name)

    if shown:
        return
    else:
        call_show_data()


# TODO bad funciton name improve
def call_create_data():
    file_name = input(
        'What file should hold the random numbers (exclude .txt): ')
    random_count = input(
        'How many random numbers do you want in file random.txt?: ')

    completed = createData(file_name, random_count)

    if completed:
        return
    else:
        call_create_data()


def createData(file_name, randCount):

    def open_file(file_name):
        file_opened = None

        try:
            file_object = open(file_name, 'w')
        except:
            print('ERROR:', file_name, 'could not be created')
            file_object = None
        else:
            file_opened = True

        return file_object, file_opened

    def convert_random_count(randCount):
        count_converted = False

        try:
            randCount = int(randCount)
        except:
            print('ERROR: Please enter a valid integer')
        else:
            count_converted = True

        return randCount, count_converted

    file_name += '.txt'

    file_object, file_opened = open_file(file_name)

    randCount, count_converted = convert_random_count(randCount)

    if file_opened and count_converted:
        random_list = []

        for i in range(0, randCount):
            random_list.append(randint(1, 1000))

        # Can't use writelines easily need to add \n back in
        for number in random_list:
            file_object.write(str(number) + '\n')

        file_object.close()

        print('File', file_name, 'written successfully.')

        return True
    else:
        return False


def showData(file_name):
    try:
        file_object = open(file_name)
    except:
        print('ERROR:', file_name, 'could not be opened')

        return False
    else:
        file_list = file_object.read().splitlines()

        for line in file_list:
            if evenodd(int(line)):
                print(line, 'is even')
            else:
                print(line, 'is odd')

        file_object.close()

        return True

    # This should never be hit but just in case read fails
    return False


def evenodd(number):
    if number % 2:
        return False
    else:
        return True


def main():
    print('Hello. This is COSC1336 Exam 2')
    print('This program allows you to generate a file with a given number' +
          ' of random numbers or print a file line by line in the console')

    while True:
        option = input(
            'Enter choice: c)reate file with random numbers; s)how file; ' +
            'q)uit: ')
        option = option.lower()

        if option == 'c':
            call_create_data()
        elif option == 's':
            call_show_data()
        elif option == 'q':
            break
        else:
            print('  Invalid option, please try again.')

    print('\nGoodbye')


if __name__ == "__main__":
    main()

# Test output
# (env) chandler@chandler-G551JM:~/ACC/programming_fundamentals_1/exams/second_exam$ python TT18_X2p3_Wilson.py
# Hello. This is COSC1336 Exam 2
# This program allows you to generate a file with a given number of random numbers or print a file line by line in the console
# Enter choice: c)reate file with random numbers; s)how file; q)uit: c
# What file should hold the random numbers (exclude .txt): /
# How many random numbers do you want in file random.txt?: 3
# ERROR: /.txt could not be created
# What file should hold the random numbers (exclude .txt): random
# How many random numbers do you want in file random.txt?: 3
# File random.txt written successfully.
# Enter choice: c)reate file with random numbers; s)how file; q)uit: s
# What file would you like to see? (exclude .txt): random
# 66 is even
# 285 is odd
# 125 is odd
# Enter choice: c)reate file with random numbers; s)how file; q)uit: q

# Goodbye