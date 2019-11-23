# Pre-condition:
# Post-condition:

import sys
import math

def optimal_parenth(s, i, j):
    if i == j:
        return ("A" + str(i))
    else:
        return "(" + optimal_parenth(s, i, s[i][j]) + optimal_parenth(s, s[i][j] + 1, j) + ")"


########################################################################################################################


def recursive_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[math.inf for x in range(n)] for y in range(n)]
    i = 0
    j = n - 1
    recursive_matrix_chain(p, i, j, m, s)
    return s


########################################################################################################################


def recursive_matrix_chain(p, i, j, m, s):
    if i == j:
        return 0
    m[i][j] = math.inf
    q = 0
    for k in range(i, j):
        q = recursive_matrix_chain(p, i, k, m, s) + recursive_matrix_chain(p, k + 1, j, m, s) + (p[i - 1])*(p[k])*(p[j])
        if q < m[i][j]:
            m[i][j] = q
            s[i][j] = k
    return q


########################################################################################################################


def bottom_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[math.inf for x in range(n)] for y in range(n)]
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
            m[i][j] = math.inf
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + (p[i-1])*(p[k])*(p[j])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m


########################################################################################################################


def memo_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[math.inf for x in range(n)] for y in range(n)]
    memoized_matrix_chain(p, m, n, s)
    return s


########################################################################################################################


def memoized_matrix_chain(p, m, n, s):
    for i in range(n):
        for j in range(i, n):
            m[i][j] = math.inf
    return lookup_chain(m, p, 0, n-1, s)


def lookup_chain(m, p, i, j, s):
    if m[i][j] < math.inf:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k, s) + lookup_chain(m, p, k + 1, j, s) + (p[i - 1])*(p[k])*(p[j])
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
    return m[i][j]


########################################################################################################################
