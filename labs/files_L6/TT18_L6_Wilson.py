# Name: Chandler Wilson
# Date: 07/05/2018
# COSC1336, Lab 6, 4 parts:
#   part 1: Write prime numbers to table
#   part 2: Census stat generator
#   part 3: Sum of file
#   part 4: Accept textual numbers for file sum


def how_many_primes():

    def prime_table(number_of_primes):
        """Generate a prime table

        Outputs to TT18_L6_Wilson_number_of_primesPrimes.txt.

        Args:
            number_of_primes (int): The number of primes to put into the table.
        """

    def collect_number():
        try:
            number = int(
                input('How many primes would you like in the table? ' +
                      '(default 1000): '))

            if 1 < number < 1000000:
                pass
            else:
                raise ValueError
        except ValueError:
            print('ERROR: Please enter an integer between 1 and 1,000,000')
            print('-' * 30)
            return collect_number()
        else:
            return number

    number_of_primes = input(
        'How many primes would you like in the table? (default 1000): ')

    return


def choice_list():
    print('Hello. This is COSC1336 lab 6 on files.')
    while True:
        option = input(
            'Enter choice: 1)Prime Table 2)launch 3)tip table 4,q)uit? ')
        if option is '1':
            how_many_primes()
        elif option is '2':
            launch()
        elif option is '3':
            tip_table()
        elif option in ['4', 'q', 'Q', 'quit']:
            break
        else:
            print('  Invalid option, please try again.')
    print('\nGoodbye')


choice_list()
