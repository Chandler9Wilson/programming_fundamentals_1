# Name: Chandler Wilson
# Date: 07/18/2018
# COSC1336, Lab 8, 4 parts:
#   part 1: Play in the shell (seperate file)
#   part 2: Validate a password
#   part 3: Test part 2 on user input
#   part 4: Generate a valid password (extra credit)
import string
import random


class Password():

    def __init__(self, password=''):
        self.password = password
        self.attempts = 0

    def meets_requirements(self):
        # This IPO isn't precisly as instructed because it takes the
        # self obj instead of one str but the initialization of a Password
        # instance only accepts one string so sort of meets I guess?
        if self._meets_len_requirement() and self._has_no_whitespace() and \
                self._has_digit() and self._has_punctuation() and \
                self._has_two_upper() and self._has_two_lower():
            return True
        else:
            return False

    def input_loop(self):
        def entrance_message():
            print('Hello!\n')
            self.help()

        def exit_message():
            print('Your password passed validation.')
            print('You took a total of', self.attempts, 'attempts')
            print('\nGoodbye')

        counter = 0
        entrance_message()

        while not self.meets_requirements() and counter < 3:
            if counter > 0:
                self.help()

                print('-' * 30)
                print('Password did not pass validation please try again')
                print('-' * 30)

            # self._debug_meets_requirements()
            self.password = input('Please enter a password: ')

            counter += 1
            self.attempts += 1

        if counter >= 3 and not self.meets_requirements():
            self.password = self.generate_password()

            print('Generated a password for you it is', self.password)
            exit_message()
        else:
            exit_message()

    def help(self):
        print('To validate a password must meet all the following:')
        print('     * At least 8 characters long')
        print('     * No spaces or whitespace (No space, tab, newline)')
        print('     * At least 1 digit (0 to 9)')
        print('     * At least 1 punctuation character')
        print('     * At least 2 uppercase letters (A .. Z)')
        print('     * At least 2 lowercase letters (a .. z)')

    def generate_password(self):
        """This generates a pseudo random string for a password this is
        not secure at all...
        """
        unshuffled_list = []

        digits = string.digits
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        punctuation = string.punctuation

        # random.choices is a much better choice here but not
        # available till 3.6
        unshuffled_list += random.sample(digits, k=random.randint(1, 7))
        unshuffled_list += random.sample(lower, k=random.randint(5, 15))
        unshuffled_list += random.sample(upper, k=random.randint(2, 7))
        unshuffled_list += random.sample(punctuation, k=random.randint(1, 7))

        # This shuffles the list
        shuffled_password = random.sample(unshuffled_list,
                                          k=len(unshuffled_list))

        return ''.join(shuffled_password)

    def _meets_len_requirement(self):
        length_requirement = 8

        # TODO might want some more fault tolerance here
        if len(self.password) >= length_requirement:
            return True
        else:
            return False

    def _has_no_whitespace(self):
        # If the password is only a whitespace character this method
        # of checking doesn't work
        split_password = self.password.split()

        if not self._meets_len_requirement():
            # Should this be None to reflect that it was not evaluated?
            return False
        elif len(split_password) > 1:
            return False
        else:
            return True

    def _has_digit(self):
        for char in self.password:
            if char.isdigit():
                return True

        return False

    def _has_punctuation(self):
        # Used to get all to punctuation char
        for char in self.password:
            if char in string.punctuation:
                return True

        return False

    def _has_two_upper(self):
        counter = 0

        for char in self.password:
            if char.isupper():
                counter += 1

        if counter >= 2:
            return True
        else:
            return False

    def _has_two_lower(self):
        counter = 0

        for char in self.password:
            if char.islower():
                counter += 1

        if counter >= 2:
            return True
        else:
            return False

    def _debug_meets_requirements(self):
        print('len requiremnt =', self._meets_len_requirement())
        print('has whitespace =', self._has_no_whitespace())
        print('has digit =', self._has_digit())
        print('has punctuation =', self._has_punctuation())
        print('has two upper =', self._has_two_upper())
        print('has two lower =', self._has_two_lower())


blank_password = Password()
user_password = blank_password.input_loop()


# Test cases:
# test_password = Password(password='ab3456789?AA')
# has_whitespace_password = Password(password='hm howdoesthiswork123')
# no_digit_password = Password(password='abcdefghijkl')
# no_punct_password = Password(password='asdfsfasdf123445')
# no_upper_password = Password(password='asdfasdfalkfjalk12233**($@')
# no_lower_password = Password(password='HALEKFJALKSDFADF;SLKJ;LADSKJF')
