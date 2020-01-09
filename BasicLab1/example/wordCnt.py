
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
    words = list()  # store words (dict's key)
    cnts = list()  # store counts (dict's val)

    # try open file at 'path' (parameter)
    try:
        f = open(path)
    except:
        print('file open fail')
        exit(1)

    # making 2 lists words & cnts
    # words's index and cnts's index are corresponding

    # CAUTION : word's len < 1
    #           end with white space or [, . ? : ; ' " \n]
    #           ignore n:n
    # way 1 : process line by line
    for line in f:
        rawWords = line.split(' ')
        for word in rawWords:
            if len(word) < 1 or (':' in word and word[-1] != ':'):
                continue

            while word[-1] in [',', '.', '?', ':', ';', "'", '"', '\n']:
                word = word[:-1]
                if len(word) < 1:
                    break

            if len(word) < 1:
                continue
            if word in words:
                cnts[words.index(word)] += 1
            else:
                words.append(word)
                cnts.append(1)

    f.close()
    return [words, cnts]


def word_cnt_db2(path):
    """
    :param path: path of file
    :return: [words, cnts]
    """
    words = list()  # store words (dict's key)
    cnts = list()  # store counts (dict's val)

    # try open file at 'path' (parameter)
    try:
        f = open(path)
    except:
        print('file open fail')
        exit(1)

    # making 2 lists words & cnts
    # words's index and cnts's index are corresponding

    # CAUTION : word's len < 1
    #           end with white space or [, . ? : ; ' " \n]
    #           ignore n:n
    # way 2 : using set & count
    rawWords = (f.read().replace('\n', ' ')).split(' ')
    all_words = list()
    for word in rawWords:
        if len(word) < 1 or word[0] in [str(i) for i in range(10)] :
            continue

        while word[-1] in [',', '.', '?', ':', ';', "'", '"', '\n']:
            word = word[:-1]
            if len(word) < 1:
                 break

        if len(word) < 1:
            continue
        all_words.append(word)

    words = list(set(all_words))
    for word in words:
        cnts.append(all_words.count(word))

    f.close()
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
        # CAUTION : get input without prompt
        #   -> just call input() not input( 'anything' )
        word2find = input()

        # CAUTION : if there are no 'word2find' in words print '0'
        if word2find == 'EXITprogram':
            break
        else:
            if word2find not in words:
                print(0)
            else:
                print(cnts[words.index(word2find)])

    # exit program
    # CAUTION : if user enter 'EXITprogram', then print 'exit'
    print('exit')
    exit(0)


def print_top_n(path, n=10):
    wordCnt = word_cnt_db(path)
    forTop = zip(wordCnt[0], wordCnt[1])
    sorted(forTop, reverse=True)
    if n > len(forTop):
        print(forTop)
    else:
        print(forTop[:n])


if __name__ == '__main__':
    path = './genesis.txt'
    word_cnt_list(path)
