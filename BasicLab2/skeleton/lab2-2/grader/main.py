"""
Python program grader

process:
    run testing
    compare the output & answer
    save score
    log the wrong cases

"""

# import requirements
from terms_checker import TermsChecker

# import student's program
# from wolfram_beta_OO import WolframBeta
from test import WolframBeta

# define path
input_path = 'input.txt'
output_path = 'output.txt'
answer_path = 'answer.txt'
logfile_path = 'log.txt'
score_path = 'score.txt'

# testing
with open(logfile_path, 'w') as logf:
    try:  # <- catch the exception in student's program
        # run the test (student's program)
        wolframBeta = WolframBeta(input_path, output_path)
        wolframBeta.solve()

        # reset log.txt
        logf.write('')
    except:
        # leave the ERROR message in log file
        logf.write('CAUTION\n'
                   'ERROR in Wolfram Beta\n'
                   '\n')

# load the data
inputs = list()
with open(input_path) as f:
    inputs = f.readlines()

outputs = list()
with open(output_path) as f:
    outputs = f.readlines()

answers = list()
with open(answer_path) as f:
    answers = f.readlines()


# val for scoring
correct = 0  # score of student
wrong_cases = []  # store wrong_cases
num = 1  # test case's number
perfect = 1100  # perfect score

# for 'zip' func work well, set the length
lendif = len(answers) - len(outputs)
if lendif > 0:
    outputs += ['\n'] * lendif

# scoring
for i, o, a in zip(inputs, outputs, answers):
    try:  # <- catch the student's wrong output format
        oterms = TermsChecker(o.strip())
        aterms = TermsChecker(a.strip())
    except:
        # wrong output format <- can log it
        wrong_cases.append((num, i, o, a))
        continue

    # compare the output & answer
    if oterms == aterms:  # using class's __eq__ func
        isCorrect = True

        # for additional wrong cases
        for wcase in [' 1.0x', ' -1.0x', ' 1x', ' -1x', 'x^1.0 ',  'x^1 ']:
            if wcase in o:  # wrong case in output
                # additional wrong case <- can log it
                wrong_cases.append((num, i, o, a))
                isCorrect = False
                break

        # check correctness
        if isCorrect:
            correct += 1
    else:
        # output != answer
        wrong_cases.append((num, i, o, a))

    # test case number update
    num += 1

# score (correct)
with open(score_path, 'w') as f:
    f.write(str(correct))

# log (wrong cases)
with open(logfile_path, 'a') as f:
    # L> 'a' option for append
    if len(wrong_cases):
        # there are wrong case
        for num, i, o, a in wrong_cases:
            f.write(
                f'Line #{num}\n' +
                f'Input: {i}' +
                f'Expected: {a}' +
                f'But you : {o}\n'
            )
    else:
        # there are no wrong case
        if correct == perfect:
            # perfect score
            f.write('PERFECT')
        else:
            # error in somewhere
            f.write('ERROR')
            # check last line in answer.txt, perfect,
            # student's program or other things
