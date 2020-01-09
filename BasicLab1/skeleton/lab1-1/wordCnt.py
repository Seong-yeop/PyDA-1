
"""
Python Basic Lab 1-1
Word Count with 2 lists
without 'dict'

word_cnt_list(path)
    interface that interacts with user

word_cnt_db(path)
    making 2 lists 'words' and 'cnts'
"""


def word_cnt_db(path):
    """
    :param path: path of file
    :return: [words, cnts]
    """
    # try open file at 'path' (parameter)

    # making 2 lists words & cnts
    # words's index and cnts's index are corresponding
    words = list()  # store words (dict's key)
    cnts = list()  # store counts (dict's val)

    # CAUTION : word's len < 1
    #           end with white space or [, . ? : ; ' " \n]
    #           ignore n:n
    #           be careful '\n' : using strip()

    return [words, cnts]


def word_cnt_list(path):
    """
    :param path: path file
    :return: None
    """
    # use 'word_cnt_db(path)' get Database

    # while user enter "EXITprogram" get word to find
    # CAUTION : get input without prompt
    #   -> just call input() not input( 'anything' )

    # CAUTION : if there are no 'word2find' in words print '0'

    # exit program
    # CAUTION : if user enter 'EXITprogram', then print 'exit'
    exit(0)


if __name__ is '__main__':
    path = './genesis.txt'
    word_cnt_list(path)
