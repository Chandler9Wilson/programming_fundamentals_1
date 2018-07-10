# Name: Chandler Wilson
# Date: 07/10/2018
# COSC1336, Lab 7, 3 parts:
#   part 1: Read and Sort a file
#   part 2: File menu with all associated actions
#   part 3: Uppercase and lowercase options to menu


def collect_filename():
    file_name = input('Enter the name of the file to be sorted: ')

    # Compare the last 4 characters of input to see if .txt
    if file_name[-4:] == '.txt':
        pass
    else:
        file_name += '.txt'

    return file_name


def read(file_name=None):
    """Given a file_name attempts to read the file and return a list"""
    if file_name:
        raise NotImplementedError
    else:
        file_name = collect_filename()

    try:
        file_object = open(file_name)
    except:
        print('ERROR: there was an error opening the file. Try again')
        read()
    else:
        file_list = file_object.read().splitlines()
        file_object.close()

    return file_name, file_list


def sort_write(file_name, file_list):
    """Given a filename and list sorts the list then writes to
    file_name_sorted.txt
    """
    sorted_list = sorted(file_list)

    sorted_file_name = file_name[:-4] + '_sorted' + file_name[-4:]

    print(file_name, 'opened,', str(len(file_list)),
          'lines found, sorted and saved to:', sorted_file_name)

    file_object = open(sorted_file_name, 'w')
    # Can't use writelines easily need to add \n back in
    for line in sorted_list:
        file_object.write(line + '\n')


def main():
    file_name, file_list = read()
    sort_write(file_name, file_list)


if __name__ == "__main__":
    main()
