# Name: Chandler Wilson
# Date: 07/18/2018
# COSC1336, Lab 9, 3 parts:
#   part 1: Find state by abbreviation
#   part 2: Set manipulation
#   part 3: Using Pickle
import string


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
            pass
        elif option in ['4', 'q', 'Q', 'quit']:
            break
        else:
            print('  Invalid option, please try again.')
    print('\nGoodbye')


if __name__ == "__main__":
    main()
