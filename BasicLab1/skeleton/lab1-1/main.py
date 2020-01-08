import os
input_files = output_files = answer_files = range(2)
path = './data/'
program = 'wordCnt.py'


def grader(program, input_files, output_files, answer_files):
    pid = os.fork()
    if pid == 0:
        # child process
        for i in range(len(input_files)):
            inputf = path + 'input' + str(input_files[i]) + '.txt'
            outputf = path + 'output' + str(output_files[i]) + '.txt'

            os.system('python3 '+program+' < '+inputf+' > '+outputf)
        exit(0)

    else:
        # parent process
        os.waitpid(pid, 0)

        # after all test is done
        try:
            rf = open('./record.txt', 'w')
            wf = open('./wrong.txt', 'w')
        except:
            print('record fail')
            exit(0)

        # recording the result
        wf.write('')
        total = 0
        for i in range(len(output_files)):
            outputf = path + 'output' + str(output_files[i]) + '.txt'
            answerf = path + 'answer' + str(answer_files[i]) + '.txt'

            try:
                of = open(outputf)
                af = open(answerf)
            except:
                print('fail')
                exit(1)

            of_lines = of.readlines()
            af_lines = af.readlines()

            right = 0
            for j in range(len(of_lines)):
                if of_lines[j].strip() == af_lines[j].strip():
                    right += 1
                else:
                    print('output',output_files[i],j+1)
                    wf.write('output ' + str(output_files[i]) + ' ' + str(j+1) + '\n')

            if len(of_lines) == 0:
                print('output ' + str(output_files[i]) + ' all')
                wf.write('output ' + str(output_files[i]) + ' all\n')

            rf.write(str(right) + '/' + str(len(af_lines)) + '\n')
            total += right
            of.close()
            af.close()

        rf.write(str(total))
        rf.close()
        wf.close()
        exit(0)


if __name__ == '__main__':
    grader(program, input_files, output_files, answer_files)