# Name: Chandler Wilson
# Date: 07/18/2018
# COSC1336, Lab 8, 4 parts:
#   part 1: Play in the shell (seperate file)
#   part 2: Validate a password
#   part 3: Test part 2 on user input
#   part 4: Generate a valid password (extra credit)


class Password():

    def __init__(self, password=''):
        self.password = password

        self.meets_requirements()

    def meets_requirements(self):
        if self._meets_len_requirement() and self._has_no_whitespace() and \
                self._has_digit() and self._has_punctuation() and \
                self._has_two_upper() and self._has_two_lower():
            return True
        else:
            return False

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
        import string

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


# Test cases:
# test_password = Password(password='ab3456789?AA')
# has_whitespace_password = Password(password='hm howdoesthiswork123')
# no_digit_password = Password(password='abcdefghijkl')
# no_punct_password = Password(password='asdfsfasdf123445')
# no_upper_password = Password(password='asdfasdfalkfjalk12233**($@')
# no_lower_password = Password(password='HALEKFJALKSDFADF;SLKJ;LADSKJF')
