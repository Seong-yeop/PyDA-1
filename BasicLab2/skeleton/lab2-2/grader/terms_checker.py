"""
TermsChecker

for scoring
"""
import math


class TermsChecker:
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

    def __eq__(self, other):
        """
        :param other: Terms
        :return: True when equal, ow False
        """
        try:
            t1 = self.terms_dict
            t2 = other.terms_dict
        except:
            return False

        eps = 1e-6

        keys = set(t1.keys()).union(t2.keys())
        for k in keys:
            if not math.isclose(t1.get(k, 0), t2.get(k, 0), rel_tol=eps, abs_tol=eps):
                return False
        return True

    @staticmethod
    def parse_term(term_str):
        """
        :param term_str: str (a single term <- a part of equation)
        :return: 2-tuple (degree: float/str, factor: float)
        """
        if 'x' in term_str:  # not constant
            if '^' in term_str:
                factor, degree = term_str.split('x^')
                degree = float(degree)
            elif '(' in term_str:  # cos(x), sin(x), exp(x)
                factor = term_str[:term_str.find('(') - 3]
                degree = term_str[term_str.find('(') - 3:]
            else:  # only x
                factor = term_str.split('x')[0]
                degree = 1
            factor = -1 if factor == '-' else 1 if factor == '' else factor
            return degree, float(factor)

        else:  # constant
            return 0, float(term_str)

    def parse_equation(self, equation):
        """
        :param equation: str
        :return: None (modify self.terms_dict)
        """
        term_str_list = equation.split(' + ')
        for term_str in term_str_list:
            term = self.parse_term(term_str.strip())
            self.terms_dict[term[0]] = self.terms_dict.get(term[0], 0) + term[1]