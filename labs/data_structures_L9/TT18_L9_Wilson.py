# Name: Chandler Wilson
# Date: 07/18/2018
# COSC1336, Lab 9, 3 parts:
#   part 1: Find state by abbreviation
#   part 2: Set manipulation
#   part 3: Using Pickle


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
        print(self.abbrev_dict)


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
            pass
        elif option is '3':
            pass
        elif option in ['4', 'q', 'Q', 'quit']:
            break
        else:
            print('  Invalid option, please try again.')
    print('\nGoodbye')


if __name__ == "__main__":
    main()
