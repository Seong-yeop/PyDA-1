
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
    try:
        f = open(path)
    except:
        print('file open fail')
        exit(0)

    # making 2 lists words & cnts
    # words's index and cnts's index are corresponding
    words = list()  # store words (dict's key)
    cnts = list()  # store counts (dict's val)

    for line in f:
        raw_words = (line.strip()).split(' ')

        # CAUTION : word's len < 1
        #           end with white space or [, . ? : ; ' " \n]
        #           ignore n:n
        #           be careful '\n' : using strip()
        for word in raw_words:
            while len(word) < 1 or word[-1] in [' ', ',', '?', ':', "'", '"', '\n']:
                word = word[:-1]
                if len(word) < 1:
                    break

            if len(word) < 1:
                continue

            # n:m
            if word[0] in ['0','1','2','3','4','5','6','7','8','9']:
                continue

            if word in words:
                cnts[words.index(word)] += 1
            else: # word not in words
                words.append(word)
                cnts.append(1)

    return [words, cnts]


def word_cnt_list(path):
    """
    :param path: path file
    :return: None
    """
    # use 'word_cnt_db(path)' get Database
    wordCnt = word_cnt_db(path)
    words = wordCnt[0]
    cnts = wordCnt[1]

    # while user enter "EXITprogram" get word to find
    while True:
        word2find = input()
        # CAUTION : get input without prompt
        #   -> just call input() not input( 'anything' )
        if word2find == 'EXITprogram':
            break # exit(0)

        # CAUTION : if there are no 'word2find' in words print '0'
        if word2find not in words:
            print(0)
        else:
            print(cnts[words.index(word2find)])
        # print(0 if word2find not in words else cnts[words.index(word2find)])

    # exit program
    # CAUTION : if user enter 'EXITprogram', then print 'exit'
    print('exit')
    exit(0)


if __name__ == '__main__':
    path = './genesis.txt'
    word_cnt_list(path)
