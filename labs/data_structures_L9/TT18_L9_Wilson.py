# Name: Chandler Wilson
# Date: 07/18/2018
# COSC1336, Lab 9, 3 parts:
#   part 1: Find state by abbreviation
#   part 2: Set manipulation
#   part 3: Using Pickle
import string
import pickle


class Abbreviations():

    def __init__(self, file_to_read=None):
        self.abbrev_dict = {}

        if file_to_read:
            self.load(file_to_read)

    def load(self, file_to_read):
        with open(file_to_read) as infile:
            while True:
                state = infile.readline().strip('\n')

                if state:
                    abbreviation = infile.readline().strip('\n')
                    # This is the population and is thrown away
                    infile.readline()

                    self.abbrev_dict[abbreviation] = state
                else:
                    break

    def lookup(self, lookup_key):
        lookup_key = lookup_key.upper()

        lookup_value = self.abbrev_dict.get(lookup_key)

        if lookup_value:
            return lookup_value
        else:
            return 'Not Found'

    def lookup_loop(self):
        while True:
            option = input(
                'Enter an abbreviation to lookup (q to quit): ')
            if option in ['q', 'Q', 'quit']:
                break
            else:
                result = self.lookup(option)

                print(result)


def sets():
    # Startup sets
    alpha = set(string.ascii_lowercase)
    digit = set(string.digits)
    even = set('02468')
    vowel = set('aeiou')
    punct = set(string.punctuation)
    match = set('{}[]()<>')
    advice = 'treat others kindly'
    address = '11928 stonehollow dr., austin, tx (us [of] a)'

    advice_set = set(advice)
    address_set = set(address)

    # Generated sets
    consonants = alpha.difference(vowel)
    odd = digit.difference(even)
    advice_consonant = advice_set.intersection(alpha).difference(vowel)
    odd_address = address_set.intersection(digit).difference(even)
    punct_address = address_set.intersection(punct)
    no_match = address_set.intersection(punct).difference(match)

    # Display generated sets
    print('Consonants:', consonants)
    print('Odd digits:', odd)
    print('Consonants in advice:', advice_consonant)
    print('Odd digits in address:', odd_address)
    print('Punctuation in address:', punct_address)
    print('Nonmatching punctuation in address:', no_match)


def read_pickle(file_to_read):
    end_of_file = False

    # This will break if given a nonexistant file
    infile = open(file_to_read, 'rb')

    while not end_of_file:
        try:
            data = pickle.load(infile)
            print(data)
        except EOFError:
            end_of_file = True


def main():
    print('Hello. This is COSC1336 lab 9 on data structures.')
    while True:
        option = input(
            'Enter choice: 1)State Abbreviation 2)Derived Sets 3)Pickle ' +
            '4,q)uit? ')
        if option is '1':
            state_abbrev = Abbreviations('StateCensus2010.txt')
            state_abbrev.lookup_loop()
        elif option is '2':
            sets()
        elif option is '3':
            read_pickle('secret.dat')
        elif option in ['4', 'q', 'Q', 'quit']:
            break
        else:
            print('  Invalid option, please try again.')
    print('\nGoodbye')


if __name__ == "__main__":
    main()

# Test output:
# (env) chandler@chandler-G551JM:~/ACC/programming_fundamentals_1/labs/data_structures_L9$ python TT18_L9_Wilson.py
# Hello. This is COSC1336 lab 9 on data structures.
# Enter choice: 1)State Abbreviation 2)Derived Sets 3)Pickle 4,q)uit? 1
# Enter an abbreviation to lookup (q to quit): t
# Not Found
# Enter an abbreviation to lookup (q to quit): tx
# Texas
# Enter an abbreviation to lookup (q to quit): Tx
# Texas
# Enter an abbreviation to lookup (q to quit): tX
# Texas
# Enter an abbreviation to lookup (q to quit): wh
# Not Found
# Enter an abbreviation to lookup (q to quit): wi
# Wisconsin
# Enter an abbreviation to lookup (q to quit): wy
# Wyoming
# Enter an abbreviation to lookup (q to quit): q
# Enter choice: 1)State Abbreviation 2)Derived Sets 3)Pickle 4,q)uit? 2
# Consonants: {'g', 'j', 'd', 'z', 'p', 'l', 'v', 'c', 'm', 'q', 'k', 'h', 'f', 'n', 'r', 's', 'w', 'y', 't', 'b', 'x'}
# Odd digits: {'9', '1', '7', '5', '3'}
# Consonants in advice: {'n', 'r', 's', 'd', 'y', 't', 'l', 'h', 'k'}
# Odd digits in address: {'9', '1'}
# Punctuation in address: {']', '(', ',', '[', ')', '.'}
# Nonmatching punctuation in address: {',', '.'}
# Enter choice: 1)State Abbreviation 2)Derived Sets 3)Pickle 4,q)uit? 3
# The mists of time run thick and thin.
# Enter choice: 1)State Abbreviation 2)Derived Sets 3)Pickle 4,q)uit? q

# Goodbye
