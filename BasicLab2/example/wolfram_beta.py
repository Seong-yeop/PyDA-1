
"""
Lab2-1. Wolfram-Beta
only int range degree & factor

Not Object Oriented,
just functions (not class)
"""
import traceback


def print_term(degree, factor):
    """
    :param degree: int, 항의 차수
    :param factor: int, 항의 계수
    :return: str
    """
    if degree == 0: # constant
        return str(factor)
    else: # degree != 0
        if factor == 0: # always 0
            return '0'
        term_str =  '-' if factor == -1 else '' if factor == 1 else str(factor)
        term_str += 'x^' + str(degree) if degree != 1 else 'x'
        return term_str


def print_equation(terms):
    """
    :param terms: dict {key=degree, value=factor}
    :return: str
    """
    equation = str()
    for degree, factor in terms.items():
        equation += print_term(degree, factor) + ' + '
    return equation[:-3]  # truncate last ' + '


def parse_term(term_str):
    """
    :param term_str: str
    :return: 2-tuple (degree: int, factor: int)
    """
    if 'x' in term_str: # not constant
        factor, degree = term_str.split('x')
        factor = -1 if factor == '-' else 1 if factor == '' else factor
        degree = 1 if len(degree) < 1 else int(degree[1:])
        return degree, int(factor)
    else: # constant
        return 0, int(term_str)


def parse_equation(equation):
    """
    :param equation: str
    :return: dict {key=degree, value=factor}
    """
    terms = dict()
    term_str_list = equation.split(' + ')
    for term_str in term_str_list:
        term = parse_term(term_str.strip())  # get tuple (degree, factor)
        terms[term[0]] = terms.get(term[0], 0) + term[1]
    return terms


def d_dx_as_terms(terms):
    """
    :param terms: dict {key=degree, value=factor}
    :return: dict {key=degree, value=factor}
             terms와 동일한 형식, 값은 terms의 미분 결과
    """
    dterms = dict()
    for degree, factor in terms.items():
        dfactor = factor * degree
        ddegree = degree - 1
        dterms[ddegree] = dterms.get(ddegree, 0) + dfactor
    return dterms


def d_dx(equation):
    """
    :param equation: str
    :return: str (differential result)
    """
    terms = parse_equation(equation)
    dterms = d_dx_as_terms(terms)
    return print_equation(dterms)


def integral_as_terms(terms, constant):
    """
    :param terms: dict (key=degree, value=factor)
    :param constant: int
    :return: dict {key=degree, value=factor}
             terms와 동일한 형식, 값은 terms의 적분 결과
    """
    iterms = dict()
    for degree, factor in terms.items():
        idegree = degree + 1
        ifactor = factor / idegree
        iterms[idegree] = iterms.get(idegree, 0) + ifactor
    iterms[0] = iterms.get(0, 0) + constant
    return iterms


def integral(equation, constant):
    """
    :param equation: str
    :param constant: str
    :param constant: str (integral result)
    """
    terms = parse_equation(equation)
    iterms = integral_as_terms(terms, int(constant))
    return print_equation(iterms)


def compute_as_terms(terms, x):
    """
    :param terms: dict (key=degree, value=factor)
    :param x: int
    :return: int
    """
    result = 0
    for degree, factor in terms.items():
        result += factor * (x ** degree)  # accumulate
    return result


def compute(equation, x):
    """
    :param equation: str
    :param x: str
    :return: str <- not int type
    """
    terms = parse_equation(equation)
    return str(compute_as_terms(terms, int(x)))


def solve_query(line):
    """
    :param line: str
    :return: str
    """
    try:
        query = line.split(',')
        if query[0] == 'D':
            return d_dx(query[1])
        elif query[0] == 'I':
            return integral(query[1], query[2])
        elif query[0] == 'C':
            return compute(query[1], query[2])
        else:
            return ''
    except:
        traceback.print_exc()
        return ''


def solve(input_path, output_path):
    """
    :param input_path: str
    :param output_path: str
    :return: None (파일 입출력으로 문제 해결)
    """
    with open(input_path, 'r') as fr:
        with open(output_path, 'w') as fw:
            for line in fr:
                fw.write(solve_query(line) + '\n')


if __name__ == '__main__':
    ipath = 'input_sample.txt'
    opath = 'output_sample.txt'

    solve(ipath, opath)