
"""
Lab2-1. Wolfram-Beta OO
support cos, sin, exp
int type degree & factor

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
        self.terms_dict = dict()
        self.equation = None
        if equation:
            self.parse_equation(equation)
            self.equation = equation

    def __str__(self):
        """
        :return: str equation
        """
        return self.print_equation()

    def __eq__(self, other):
        """
        :param other: Terms
        :return: True when equal, ow False
        """
        if type(other) != Terms:
            return False

        t1 = self.terms_dict
        t2 = other.terms_dict
        eps = 1e-6

        keys = set(t1.keys()).union(t2.keys())
        for k in keys:
            if not math.isclose(t1.get(k, 0), t2.get(k, 0), rel_tol=eps, abs_tol=eps):
                return False
        return True

    @staticmethod
    def print_term(degree, factor):
        """
        :param degree: int, 항의 차수
        :param factor: int, 항의 계수
        :return: str
        """
        if degree == 0: # constant
            return str(factor)
        else: # degree != 0
            if factor == 0:
                return '0'
            term_str = '-' if factor == -1 else '' if factor == 1 else str(factor)
            if type(degree) is str: # cos sin exp
                term_str += degree
            else:
                term_str += 'x^' + str(degree) if degree != 1 else 'x'
            return term_str

    def print_equation(self):
        """
        :param self: self.terms_dict: dict {key=degree, value=factor}
        :return: str equation
        """
        equation = list()
        for degree, factor in self.terms_dict.items():
            equation.append(self.print_term(degree, factor))
        return ' + '.join(equation)

    @staticmethod
    def parse_term(term_str):
        """
        :param term_str: str (a single term <- a part of equation)
        :return: 2-tuple (degree: int/str, factor: int)
        """
        if 'x' in term_str: # not constant
            if '^' in term_str:
                factor, degree = term_str.split('x^')
                degree = int(degree)
            else: # only x
                factor = term_str.split('x')[0]
                degree = 1
            factor = -1 if factor == '-' else 1 if factor == '' else factor
            return degree, int(factor)

        else:  # constant
            return 0, int(term_str)

    def parse_equation(self, equation):
        """
        :param equation: str
        :return: None (modify self.terms_dict)
        """
        for term_str in equation.split(' + '):
            degree, factor = self.parse_term(term_str.strip())
            self.terms_dict[degree] = self.terms_dict.get(degree, 0) + factor

    def d_dx_as_terms(self):
        """
        :return: Terms : that result of differential
        """
        dterms = Terms()
        for d, f in self.terms_dict.items():
            if d != 0:
                dterms.terms_dict[d - 1] = dterms.terms_dict.get(d - 1, 0) + (f * d)
        return dterms if len(dterms.terms_dict) else Terms('0')

    def integral_as_terms(self, constant):
        """
        :param constant: int
        :return: Terms : that result of integral
        """
        iterms = Terms(str(constant))
        for d, f in self.terms_dict.items():
            iterms.terms_dict[d + 1] = iterms.terms_dict.get(d + 1, 0) + (f / (d + 1))
        return iterms

    def compute_as_terms(self, x):
        """
        :param x: int
        :return: int
        """
        result = 0.0
        for d, f in self.terms_dict.items():
            result += f * (x ** d)  # accumulate
        return result


class WolframBeta:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        pass

    @staticmethod
    def d_dx(equation, n=1):
        """
        :param equation: str
        :param n: int
        :return: equation str (differential result)
        """
        terms = Terms(equation)
        dterms = terms.d_dx_as_terms()
        return str(dterms)

    @staticmethod
    def integral(equation, constant, n=1):
        """
        :param equation: str
        :param constant: str
        :param n: int
        :return: str equation (integral result)
        """
        terms = Terms(equation)
        iterms = terms.integral_as_terms(int(constant))
        return str(iterms)

    @staticmethod
    def compute(equation, x):
        """
        :param equation: str
        :param x: str
        :return: str <- not int type
        """
        terms = Terms(equation)
        return str(terms.compute_as_terms(int(x)))

    def solve_query(self, line):
        """
        :param line: str (query)
        :return: str (result)
        """
        try:
            query = line.split(',')
            if query[0] == 'D':
                return self.d_dx(query[1])
            elif query[0] == 'I':
                return self.integral(query[1], query[2])
            elif query[0] == 'C':
                return self.compute(query[1], query[2])
            else:
                return ''
        except:
            traceback.print_exc()
            return ''

    def solve(self):
        """
        :return: None (파일 입출력으로 문제 해결)
        """
        with open(self.input_path, 'r') as fr:
            with open(self.output_path, 'w') as fw:
                for line in fr:
                    fw.write(self.solve_query(line) + '\n')


if __name__ == '__main__':
    ipath = 'input.txt'
    opath = 'output.txt'

    wolfram_beta = WolframBeta(ipath, opath)
    wolfram_beta.solve()