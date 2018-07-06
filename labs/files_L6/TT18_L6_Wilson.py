# Name: Chandler Wilson
# Date: 07/05/2018
# COSC1336, Lab 6, 4 parts:
#   part 1: Write prime numbers to table
#   part 2: Census stat generator
#   part 3: Sum of file
#   part 4: Accept textual numbers for file sum


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
        primes_list = primes_to_nth_prime(number_of_primes)
        file_name = 'TT18_L6_Wilson_' + str(number_of_primes) + 'Primes.txt'
        outfile = open(file_name, 'w')

        for prime in primes_list:
            outfile.write(str(prime))

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


if __name__ == "__main__":
    choice_list()
