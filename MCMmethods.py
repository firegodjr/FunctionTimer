# Pre-condition:
# Post-condition:

import sys


def print_optimal_parenth(s, i, j):
    if i == j:
        print("A" + i)
    else:
        print("(" + print_optimal_parenth(s, i, s[i][j]) + print_optimal_parenth(s, s[i][j] + 1, j) + ")")
    return


########################################################################################################################


def recursive_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[sys.maxsize for x in range(n + 1)] for y in range(n + 1)]
    i = 1
    j = n
    recursive_matrix_chain(p, i, j, m, s)
    return s


########################################################################################################################


def recursive_matrix_chain(p, i, j, m, s):
    if i == j:
        return 0
    m[i][j] = sys.maxsize
    for k in range(i, j-1):
        q = recursive_matrix_chain(p, i, k) + recursive_matrix_chain(p, k + 1, j) + (p[i - 1])(p[k])(p[j])
        if q < m[i][j]:
            m[i][j] = q
            s[i][j] = q
    return q


########################################################################################################################


def bottom_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[sys.maxsize for x in range(n + 1)] for y in range(n + 1)]
    bottom_up_mcm(p, m, s)
    return s

########################################################################################################################


def bottom_up_mcm(p, m, s):
    n = len(p)
    for i in range(1, n):
        m[i][i] = 0
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j - 1):
                q = m[i][k] + m[k+1][j] + (p[i-1])(p[k])(p[j])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m


########################################################################################################################


def memo_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[sys.maxsize for x in range(n + 1)] for y in range(n + 1)]
    memoized_matrix_chain(p, m, n, s)
    return s


########################################################################################################################


def memoized_matrix_chain(p, m, n, s):
    for i in range(1, n):
        for j in range(i, n):
            m[i][j] = sys.maxsize
    return lookup_chain(m, p, 1, n, s)


def lookup_chain(m, p, i, j, s):
    if m[i][j] < sys.maxsize:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j-1):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k + 1, j) + (p[i - 1])(p[k])(p[j])
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = q
    return m[i][j]


########################################################################################################################
