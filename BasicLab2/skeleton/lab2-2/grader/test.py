"""
Lab2-2. Wolfram-Beta OO
support cos, sin, exp
float type degree & factor

Object Oriented
using classes
    WolframBeta
    Terms (has terms_dict)
"""
import traceback
import math


class Terms:
    def __init__(self, equation=None):
        """
        :param equation: str, 문자열로 표현된 함수
                        None 인 경우 terms_dict 를 생성만 함
        """
        # make Terms.terms : dict {key = degree, val = factor}
        # store the equation if not None
        self.terms_dict = dict()
        self.equation = None
        pass

    def __str__(self):
        """
        :return: str equation
        """
        # this function support interface
        # str(Terms) -> string (equation)
        return self.print_equation()

    def __eq__(self, other):
        """
        :param other: Terms
        :return: True when equal, ow False
        """
        # don't modify this function
        if type(other) != Terms:
            return False

        t1 = self.terms_dict
        t2 = other.terms_dict
        eps = 1e-6

        keys = set(t1.keys()).union(t2.keys())
        for k in keys:
            if not math.isclose(t1.get(k, 0), t2.get(k, 0),
                                rel_tol=eps, abs_tol=eps):
                return False
        return True

    @staticmethod
    def print_term(degree, factor):
        """
        :param degree: float, 항의 계수
        :param factor: float, 항의 차수
        :return: str
        """
        if degree == 0:
            terms_str = '0'
        elif degree == 1:
            terms_str = str(factor)
        elif degree == 2:
            terms_str = str(factor * degree) + 'x'
        else:
            terms_str = str(factor * degree) + 'x^' + str(degree - 1)

        return terms_str

    def print_equation(terms):
        """
        :param self: self.terms_dict: dict {key=degree, value=factor}
        :return: str equation
        """
        # use wolfram_beta's print_equation
        for key, value in terms.items():
            if key == 1:
                equation_str = ' + ' + str(value) + 'x'
            else:
                equation_str = ' + ' + str(value) + 'x^' + str(key)

        return equation_str

    @staticmethod
    def parse_term(term_str):
        """
        :param term_str: str (a single term <- a part of equation)
        :return: 2-tuple (degree: float/str, factor: float)
        """
        # use wolfram_beta's parse_term
        # now, degree is float
        #             or (cos(x), sin(x), exp(x)
        #      factor is float
        # print(' parse_ter = {}'.format(term_str))
        if 'x' in term_str:
            if 'x^' in term_str:  # "x^ 처리"
                index = term_str.index('x^')

                # factor 구하기
                if index == 0:
                    factor = 1
                elif term_str[: index] != '':
                    if term_str[: index] == '-':
                        factor = -1
                    else:
                        factor = int(term_str[: index])

                # degree 구하기
                if term_str[index + 2:] != '':
                    degree = int(term_str[index + 2:])
            else:  # 오직 "x"만 처리
                index = term_str.index('x')

                # factor 구하기
                if index == 0:
                    factor = 1
                elif term_str[: index] != '':
                    if term_str[: index] == '-':
                        factor = -1
                    else:
                        factor = int(term_str[: index])

                degree = 1
        else:
            factor = int(term_str)
            degree = 0

        return degree, factor

    def parse_equation(self, equation):
        """
        :param equation: str
        :return: None (modify self.terms_dict)
        """

        # update self.terms_dict
        # terms in equation is separated by ' + '
        # use dict.get(key, default)
        # self.terms_dict = dict()
        # my_dic = dict

        dic = {}
        iterms = Terms()
        # self.terms_dict = dict()
        iterms.terms_dict = dict()

        degree, factor = Terms().parse_term(str(equation))
        # iterms.terms_dic[degree] = factor
        dic[degree] = factor

        # print(iterms.terms_dic)

        return dic  # iterms.terms_dic

    def d_dx_as_terms(terms):
        """
        :return: Terms : that result of differential
        """
        # make Terms that result of differential
        dterms = Terms()

        # process each term (degree, factor) in terms
        # use dict.get(key, default)
        diff_dic = dict()

        for k, v in terms.items():
            if k == 0:
                degree = 0
                value = 0
            else:
                degree = k
                value = v

            diff_dic[degree] = value

        return diff_dic

    def integral_as_terms(terms, constant):
        """
        :param constant: float
        :return: Terms : that result of integral
        """
        # make Terms that result of integral
        iterms = Terms()

        # process each term (degree, factor) in terms
        # use dict.get(key, default)
        integral_dic = dict()

        integral_dic[0] = constant

        for k, v in terms.items():
            degree = k + 1
            value = int(v / (k + 1))
            integral_dic[degree] = value

        return integral_dic

    def compute_as_terms(terms, x):
        """
        :param x: float
        :return: float
        """
        result = 0.0
        # compute the result using Terms
        for k, v in terms.items():
            if k == 0:
                result = v * 1
            else:
                result = (float(x) ** float(k)) * v

        return result


class WolframBeta:
    def __init__(self, input_path, output_path):
        """
        :param input_path: path of input query file
        :param output_path: path of output file storing result
                            generated by wolfram beta
        """
        self.input_path = input_path
        self.output_path = output_path

        # if you need more initializing process,
        # just write your code !

        pass

    @staticmethod
    def d_dx(equation):
        """
        :param equation: str
        :return: equation str (differential result)
        """
        new_str = ''

        for element in equation:
            if 'D' not in element:
                for i in range(len(element)):
                    diff_dic = dict()
                    diff_str = ''
                    degree, factor = Terms.parse_term(element[i])
                    diff_dic[degree] = factor
                    diff_dic = Terms.d_dx_as_terms(diff_dic)

                    for k, v in diff_dic.items():
                        if k != 0:
                            diff_str = Terms.print_term(k, v)
                        else:
                            diff_str = '0'

                        if i != 0:
                            if diff_str != '0':
                                if new_str != '':
                                    new_str = new_str + ' + ' + diff_str
                                else:
                                    new_str = diff_str
                        else:
                            if len(element) > 1:
                                if diff_str != '0':
                                    new_str = diff_str
                            else:
                                if diff_str != '0':
                                    new_str = diff_str
                                else:
                                    new_str = '0'

        print('최종 연산 결과: {}'.format(new_str))

        return new_str

    @staticmethod
    def integral(equation, constant):
        """
        :param equation: str
        :param constant: str
        :return: str equation (integral result)
        """
        # using Terms's class function
        equation_dic = dict()

        integral_str = ''
        for element in equation:
            if equation.index(element) == (len(equation) - 1):
                break

            if 'I' not in element:
                for i in range(len(element)):
                    # equation_dic =
                    equation_dic = Terms.parse_equation(i, element[i])
                    equation_dic = Terms.integral_as_terms(equation_dic, constant[0])
                    constant_str = equation_dic.get(0)
                    euqation_str = Terms.print_equation(equation_dic)
                    integral_str += euqation_str

        integral_str = constant_str + integral_str

        print('최종 연산 결과: {}'.format(integral_str))

        return str(integral_str)  # equation

    @staticmethod
    def compute(equation, x):
        """
        :param equation: str
        :param x: str
        :return: str <- not int type
        """
        # using Terms's class function
        tatal_val = 0
        for element in equation:
            if equation.index(element) == (len(equation) - 1):
                break

            if 'C' not in element:
                # print('here')
                for i in range(len(element)):
                    equation_dic = Terms.parse_equation(i, element[i])
                    calc = Terms.compute_as_terms(equation_dic, x[0])
                    tatal_val += calc
        # print(tatal_val)

        return str(tatal_val)  # result

    def solve_query(self, line):
        """
        :param line: str (query)
        :return: str (result)
        """
        try:
            for element in line[0]:
                if element == 'D':
                    wolf_str = self.d_dx(line)
                elif element == 'I':
                    wolf_str = self.integral(line, line[-1])
                else:
                    wolf_str = self.compute(line, line[-1])

            return wolf_str  # if line == 'D,x^2'
        except:
            traceback.print_exc()
            return ''

    def solve(self):
        """
        :return: None (파일 입출력으로 문제 해결)
        """
        # file open
        try:
            fh = open(self.input_path)
        except:
            print('{} file can not founded!'.format(self.input_path))
            exit(0)

        try:
            text = open(self.output_path, 'w')
        except:
            print('{} file can not founded!'.format(self.output_path))
            exit(0)

        for line in fh:
            element_str = ''

            line = line.strip().split(',')
            new_list = [line[i].split(' + ') for i in range(len(line))]
            calc_str = self.solve_query(new_list)

            data = "%s\n" % calc_str
            text.write(data)

        fh.close()
        text.close()

        return


if __name__ == '__main__':
    ipath = 'input_sample.txt'
    opath = 'output_sample.txt'

    wolfram_beta = WolframBeta(ipath, opath)
    wolfram_beta.solve()