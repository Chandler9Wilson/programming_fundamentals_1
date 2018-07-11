# Name: Chandler Wilson
# Date: 07/10/2018
# COSC1336, Lab 7, 3 parts:
#   part 1: Read and Sort a file
#   part 2: File menu with all associated actions
#   part 3: Uppercase and lowercase options to menu


class Names_file():

    def __init__(self, file_name='people.txt'):
        self.file_name = 'people.txt'
        self.names_list = []

    def read(self, file_name=None):
        """Given a file_name attempts to read the file and return a list"""
        def collect_filename():
            self.file_name = input('Enter the name of the file to be read: ')

            # Compare the last 4 characters of input to see if .txt
            if self.file_name[-4:] == '.txt':
                pass
            else:
                self.file_name += '.txt'

            return self.file_name

        if file_name:
            self.file_name = file_name
        else:
            self.file_name = collect_filename()

        try:
            file_object = open(self.file_name)
        except:
            print('ERROR: there was an error opening', file_name, 'Try again')
            self.read()
        else:
            self.names_list = file_object.read().splitlines()
            file_object.close()

            print('Read the file')

        return self.names_list

    def sort(self):
        self.names_list = sorted(self.names_list)
        print('Sorted the list')

        return self.names_list

    def write(self):
        default_file_to_write = self.file_name[:-4] + '_out' + \
            self.file_name[-4:]

        file_to_write = input(
            'What file would you like to write to (default people_out.txt): ')

        if file_to_write:
            pass
        else:
            file_to_write = default_file_to_write

        try:
            file_object = open(file_to_write, 'w')
        except:
            print('Unable to open', file_to_write)
        else:
            # Can't use writelines easily need to add \n back in
            for name in self.names_list:
                file_object.write(name + '\n')

    def insert(self):

        def insertName(namelist, name):
            if name in namelist:
                print('ERROR: Name is already in list')
            else:
                namelist.append(name)
                print(name, 'added to the list')

            return namelist

        new_name = input('Enter a name to insert: ')

        self.names_list = insertName(self.names_list, new_name)

    def delete(self):

        def deleteName(namelist, target):
            if target in namelist:
                namelist.remove(target)
                print('Removed', target, 'from the list')
            else:
                print(target, 'is not in the list')

            return namelist

        name_to_delete = input('What name would you like to delete?: ')

        self.names_list = deleteName(self.names_list, name_to_delete)

    def find(self):

        def findName(namelist, target):
            if target in namelist:
                return True
            else:
                return False

        name_to_find = input('What name would you like to find?: ')

        found = findName(self.names_list, name_to_find)

        if found:
            print(name_to_find, 'is in the list')
        else:
            print(name_to_find, 'is NOT in the list')

    def view(self):
        counter = 1

        for name in self.names_list:
            if counter % 10 is 0:
                print(name)
            elif (counter) == len(self.names_list):
                print(name)
            else:
                print(name, end=', ')

            counter += 1

    def uppercase(self):
        new_list = []

        for name in self.names_list:
            new_name = name.upper()
            new_list.append(new_name)

        self.names_list = new_list

        print('All names are uppercase')

    def lowercase(self):
        new_list = []

        for name in self.names_list:
            new_name = name.lower()
            new_list.append(new_name)

        self.names_list = new_list

        print('All names are lowercase')

    def input_loop(self):
        print('Hello. This is COSC1336 lab 7 on lists and tuples.')

        while True:
            option = input(
                'Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, ' +
                's)ort, v)iew, u)ppercase, l)owercase, q)uit: ')
            option = option.lower()

            if option == 'r':
                self.read()
            elif option == 'w':
                self.write()
            elif option == 'i':
                self.insert()
            elif option == 'd':
                self.delete()
            elif option == 'f':
                self.find()
            elif option == 's':
                self.sort()
            elif option == 'v':
                self.view()
            elif option == 'u':
                self.uppercase()
            elif option == 'l':
                self.lowercase()
            elif option == 'q':
                break
            else:
                print('  Invalid option, please try again.')

        print('\nGoodbye')


def main():
    user_names = Names_file()
    user_names.input_loop()


if __name__ == "__main__":
    main()

# Test output:
# (env) chandler@chandler-G551JM:~/ACC/programming_fundamentals_1/labs/lists_L7$ python TT18_L7_Wilson.py
# Hello. This is COSC1336 lab 7 on lists and tuples.
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: r
# Enter the name of the file to be read: people
# Read the file
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: v
# Lu, Joe, Luis, Zelda, Chad, Nguyen, Mindy, Anne, Lee, George
# Max, Antoine, Terry, Maria, An, Victor, Larry, Steve, Anita, Joline
# Charles
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: i
# Enter a name to insert: chandler
# chandler added to the list
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: s
# Sorted the list
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: v
# An, Anita, Anne, Antoine, Chad, Charles, George, Joe, Joline, Larry
# Lee, Lu, Luis, Maria, Max, Mindy, Nguyen, Steve, Terry, Victor
# Zelda, chandler
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: d
# What name would you like to delete?: chandler
# Removed chandler from the list
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: u
# All names are uppercase
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: v
# AN, ANITA, ANNE, ANTOINE, CHAD, CHARLES, GEORGE, JOE, JOLINE, LARRY
# LEE, LU, LUIS, MARIA, MAX, MINDY, NGUYEN, STEVE, TERRY, VICTOR
# ZELDA
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: l
# All names are lowercase
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: v
# an, anita, anne, antoine, chad, charles, george, joe, joline, larry
# lee, lu, luis, maria, max, mindy, nguyen, steve, terry, victor
# zelda
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: w
# What file would you like to write to (default people_out.txt):
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: w
# What file would you like to write to (default people_out.txt): people_sorted.txt
# Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, s)ort, v)iew, u)ppercase, l)owercase, q)uit: q

# Goodbye
