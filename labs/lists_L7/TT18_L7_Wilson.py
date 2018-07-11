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
            self.file_name = input('Enter the name of the file to be sorted: ')

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
            print('ERROR: there was an error opening the file. Try again')
            self.read()
        else:
            self.names_list = file_object.read().splitlines()
            file_object.close()

        return self.names_list

    def sort(self):
        self.names_list = sorted(self.names_list)

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

            return namelist

        new_name = input('Enter a name to insert: ')

        self.names_list = insertName(self.names_list, new_name)

    def delete(self):
        pass

    def find(self):

        def findName(namelist, target):
            if target in namelist:
                return True
            else:
                return False

        find_name = input('What name would you like to find?: ')

        found = findName(self.names_list, find_name)

        if found:
            print(find_name, 'is in the list')
        else:
            print(find_name, 'is NOT in the list')

    def view(self):
        pass

    def uppercase(self):
        pass

    def lowercase(self):
        pass

    def input_loop(self):
        print('Hello. This is COSC1336 lab 7 on lists and tuples.')

        while True:
            option = input(
                'Enter choice: r)ead, w)rite, i)nsert, d)elete, f)ind, ' +
                's)ort, v)iew, u)ppercase, l)owercase, q)uit: ')
            option = option.lower()
            print(type(option))

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
