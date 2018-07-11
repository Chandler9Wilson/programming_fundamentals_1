# Name: Chandler Wilson
# Date: 07/10/2018
# COSC1336, Exam 2, 3 parts:
#   part 1: Generate random number file
#   part 2: Improve part 1
#   part 3: Even Odd added to output
from random import randint


def show_data():
    raise NotImplementedError


# TODO bad funciton name improve
def collect_data():
    file_name = input(
        'What file should hold the random numbers (exclude .txt): ')
    random_count = input(
        'How many random numbers do you want in file random.txt?: ')

    createData(file_name, random_count)


def createData(file_name, randCount):
    file_name = file_name + '.txt'
    file_opened = False
    count_converted = False

    try:
        file_object = open(file_name, 'w')
    except:
        print('ERROR:', file_name, 'could not be created')
    else:
        file_opened = True

    try:
        randCount = int(randCount)
    except:
        print('ERROR: Please enter a valid integer')
    else:
        count_converted = True

    if file_object and count_converted:
        random_list = []

        for i in range(0, randCount):
            random_list.append(randint(1, 1001))

        print(random_list)
    else:
        collect_data()


def main():
    print('Hello. This is COSC1336 lab 7 on lists and tuples.')

    while True:
        option = input(
            'Enter choice: c)reate file with random numbers; s)how file; ' +
            'q)uit: ')
        option = option.lower()

        if option == 'c':
            collect_data()
        elif option == 's':
            show_data()
        elif option == 'q':
            break
        else:
            print('  Invalid option, please try again.')

    print('\nGoodbye')


if __name__ == "__main__":
    main()
