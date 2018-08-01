# Name: Chandler Wilson
# Date: 07/31/2018
# COSC1336, Exam 3, 4 parts:
#   part 1: notice, load_dictionary, and main functions
#   part 2: spellcheck function
#   part 3: enhance spellcheck
#   part 4: status message (extra credit)


def load_dictionary(wordlist):
    dictionary = 'dictionary.txt'

    try:
        infile = open(dictionary)
    except:
        print('Could not find %s in the local directory' % dictionary)
    else:
        for line in infile:
            wordlist.append(line.strip())

        print('Found %s words in the dictionary' % format(len(wordlist), ','))

        infile.close()

        return True


def notice(exam_number):
    notice_str = 'Spell checking program for Exam %s lab' % (exam_number)

    return notice_str


def input_loop():
    return


def main():
    print(notice(3))
    dictionary = []
    load_dictionary(dictionary)
    print('\nGood bye!')


if __name__ == "__main__":
    main()
