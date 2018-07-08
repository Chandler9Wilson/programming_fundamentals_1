# Name: Chandler Wilson
# Date: 07/05/2018
# COSC1336, Lab 6, 4 parts:
#   part 1: Write prime numbers to table
#   part 2: Census stat generator
#   part 3: Sum of file
#   part 4: Accept textual numbers for file sum


# TODO This would make far more sense as a class
def how_many_primes():

    def prime_test(number):
        """Tests a number to see if it is prime returns True if it is"""
        is_prime = True
        # Create an odd number list
        list_to_test = [2] + list(range(3, (number - 1), 2))

        # Concatenate 2 to check if even
        for i in list_to_test:
            if (number % i) == 0:
                is_prime = False
                break

        return is_prime

    def primes_to_nth_prime(n):
        """Find the primes up to the nth prime and return them as a list."""
        range_to_test = range(1, 1000000000, 2)
        prime_list = []

        # TODO I should really cache the results just brute forcing rn
        for odd_number in range_to_test:
            if len(prime_list) >= n:
                break
            if prime_test(odd_number):
                prime_list.append(odd_number)

        return prime_list

    def prime_table(number_of_primes):
        """Generate a prime table

        Outputs to TT18_L6_Wilson_number_of_primesPrimes.txt.

        Args:
            number_of_primes (int): The number of primes to put into the table.
        """

        def table_heading(number_of_primes, last_prime, outfile):
            number_of_primes = format(number_of_primes, ',')
            last_prime = format(last_prime, ',')
            # Centers within given number of characters
            # see https://pyformat.info/#string_pad_align
            first_line = format(
                'The First ' + number_of_primes + ' Primes\n', '^79')

            outfile.write(first_line)
            outfile.write('(the ' + number_of_primes +
                          'th is ' + last_prime + ')\n')
            outfile.write('\n')

        def table_footer(outfile):
            centered_end = format('End.', '^79')

            outfile.write('\n')
            outfile.write(centered_end)

        primes_list = primes_to_nth_prime(number_of_primes)
        file_name = 'TT18_L6_Wilson_' + str(number_of_primes) + 'Primes.txt'
        outfile = open(file_name, 'w')
        counter = 1

        table_heading(number_of_primes, primes_list[-1], outfile)

        for prime in primes_list:
            if counter % 10 is 0 and counter is not 0:
                # This format forces seven digits of padding
                # see https://pyformat.info/#number
                outfile.write(format(prime, '7d') + '\n')
            else:
                outfile.write(format(prime, '7d') + ', ')

            counter += 1

        table_footer(outfile)

        outfile.close()

    def collect_number():
        try:
            number = int(
                input('How many primes would you like in the table?: '))

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

    number_of_primes = collect_number()
    prime_table(number_of_primes)


class Census():

    def __init__(self, infile_name):
        self.infile_name = infile_name
        self.state_info = {}

        self.encode_file()
        self.population_stats()

    def encode_file(self):
        infile = open(self.infile_name)

        with open(self.infile_name) as infile:
            while True:
                state = infile.readline().strip('\n')

                if state:
                    abbreviation = infile.readline().strip('\n')
                    population = infile.readline().strip('\n')

                    self.state_info[state] = {
                        'abbreviation': abbreviation,
                        'population': int(population)
                    }
                else:
                    break

        return self.state_info

    def population_stats(self):
        # TODO add explanatory comment for this monstrosity
        sorted_states_list = sorted(
            self.state_info,
            key=lambda state: self.state_info[state]['population'])
        total_population = 0

        for state in self.state_info:
            total_population += self.state_info[state]['population']

        highest_population = sorted_states_list[-1]
        lowest_population = sorted_states_list[1]
        average_population = format(
            (total_population / len(self.state_info)), ',.0f')
        texas_population = format(
            self.state_info['Texas']['population'], ',.0f')

        print(highest_population, 'has the highest population')
        print(lowest_population, 'has the lowest population')
        print("The average state's population is", average_population)
        print('The state of Texas has a population of', texas_population)


def choice_list():
    print('Hello. This is COSC1336 lab 6 on files.')
    while True:
        option = input(
            'Enter choice: 1)Prime Table 2)Census Stats 3)tip table 4,q)uit? ')
        if option is '1':
            how_many_primes()
        elif option is '2':
            state_census = Census('StateCensus2010.txt')
        elif option is '3':
            tip_table()
        elif option in ['4', 'q', 'Q', 'quit']:
            break
        else:
            print('  Invalid option, please try again.')
    print('\nGoodbye')


if __name__ == "__main__":
    choice_list()
