# Name: Chandler Wilson
# Date: 07/31/2018
# COSC1336, Exam 3, 4 parts:
#   part 1: notice, load_dictionary, and main functions
#   part 2: spellcheck function
#   part 3: enhance spellcheck
#   part 4: status message (extra credit)
import string


def load_dictionary(wordlist):
    dictionary = 'dictionary.txt'

    try:
        infile = open(dictionary)
    except:
        print('  Could not find %s in the local directory' % dictionary)
    else:
        for line in infile:
            wordlist.append(line.strip())

        print('  Found %s words in the dictionary' %
              format(len(wordlist), ','))

        infile.close()

        return True


def spellcheck(dictionary):

    def remove_punct(line, save_to):
        for word in line:
            save_to.append(word.strip(string.punctuation))

    def proccess_file(filename, dictionary):
        try:
            infile = open(filename)
        except:
            print('  Could not open %s' % filename)
        else:
            misspelled_words = []
            correct_words = []

            for line_number, line in enumerate(infile):
                # Lists to loop over for punctuation removal
                unformatted_words = line.split()
                lower_words = line.lower().split()

                # These will have punctuation removed
                original_punct_words = []
                formatted_words = []

                remove_punct(lower_words, formatted_words)
                remove_punct(unformatted_words, original_punct_words)

                for word_number, word in enumerate(formatted_words):
                    if word in dictionary:
                        correct_words.append(original_punct_words[word_number])
                    else:
                        misspelled_msg = '  %s on line %s not found' % (
                            original_punct_words[word_number], line_number + 1)

                        misspelled_words.append(
                            original_punct_words[word_number])
                        print(misspelled_msg)

            print('  %s of %s words not found in file: %s' %
                  (len(misspelled_words),
                   len(misspelled_words + correct_words),
                   filename))

    def format_filename(filename):
        if filename.endswith('.txt'):
            return filename
        else:
            return filename + '.txt'

    while True:
        file_to_check = input(
            'Name of file to spell check (.txt optional, enter nothing ' +
            'to quit): ')

        if file_to_check:
            formatted_filename = format_filename(file_to_check)

            proccess_file(formatted_filename, dictionary)

        else:
            break


def notice(exam_number):
    notice_str = 'Spell checking program for Exam %s lab' % (exam_number)

    return notice_str


def main():
    print(notice(3))
    dictionary = []

    if load_dictionary(dictionary):
        spellcheck(dictionary)

    print('\nGood bye!')


if __name__ == "__main__":
    main()

# Test Output below:
# Spell checking program for Exam 3 lab
#   Found 80,372 words in the dictionary
# Name of file to spell check (.txt optional, enter nothing to quit): letter
#   Selena on line 2 not found
#   horss on line 5 not found
#   werds on line 6 not found
#   Plinkerton on line 10 not found
#   4 of 41 words not found in file: letter.txt
# Name of file to spell check (.txt optional, enter nothing to quit): nope
#   Could not open nope.txt
# Name of file to spell check (.txt optional, enter nothing to quit):

# Good bye!
