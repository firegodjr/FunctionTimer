# Pre-condition:
# Post-condition:

import math

########################################################################################################################


def optimal_parenth(s, i, j):
    if i == j:
        return ("A" + str(i))
    else:
        return "(" + optimal_parenth(s, i, s[i][j]) + optimal_parenth(s, s[i][j] + 1, j) + ")"


########################################################################################################################


def recursive_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[0 for x in range(n)] for y in range(n)]
    i = 0
    j = n - 1
    recursive_matrix_chain(p, i, j, m, s)
    return s


########################################################################################################################


# Pre-condition: p must be a list of integers with size >= 2, i and j are the first and last matrices respectively
# within the subset of p that are going to be multiplied. m and s are n x n matrices, where n = len(p). m and n are
# initialized to have their entries be 0.
# Post-condition: m contains the number of computations made for each and every combination of matrices multiplied.
# s contains the k values that resulted in the least computations to be later used in optimal_parenth().
def recursive_matrix_chain(p, i, j, m, s):
    assert len(p) >= 2
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


'''
Recursive Matrix Multiplication– Implemented as recursive_matrix_chain in code 
At the beginning of each iteration of the loop in lines 6-10, the value stored in m[i,j] will be the smallest number of 
multiplications for that portion of range being looked through of i to j-1 (inclusive). 

Initialization: Before the first iteration of the loop, m[i,j] is set to infinity.  Since no iterations/multiplications 
have been calculated/executed yet, infinity is trivially the minimum value of multiplications available/possible for 
m[i,j]. Thus the loop invariant holds. 

Maintenance: During each iteration of the loop, the value of q is computed by comparing the possible values of matrix 
multiplication (through the recursive matrix chain function) for all values from k = i to j-1 (inclusive), and then the 
current stored values of multiplication in the p matrix.  At any point in time, if q, which is set to the value of the 
matrix multiplication values and the previous multiplications stored in p, is less than m[i,j], then m[i,j] is set to q. 
If not, then q remains the currently stored value and then obviously q is less than the multiplications present from the 
p array and performing the multiplications.  After this executes, trivially and as shown above, m[i,j] will hold the 
minimum value of multiplications at the point of evaluation being examined. Thus the loop invariant holds. 

Termination: After the last iteration of the loop in lines 6-10, i = j. The previous iteration ensured that the final 
iteration of m[i,j] which will be the total number of multiplications for the values stored to be multiplied in p, will 
be the minimum value of all possible branches of multiplications and previous multiplications for m[i,j].  At the end of 
the loop, m will be transformed such that at the maximum i and j, m[i,j] will contain this minimum possible value 
holding the minimum number of multiplications for the array of values in p. Thus the loop invariant holds at 
termination.
'''

########################################################################################################################


def bottom_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[0 for x in range(n)] for y in range(n)]
    bottom_up_mcm(p, m, s)
    return s

########################################################################################################################


# Pre-condition: p must be a list of integers with size >= 2. m and s are n x n matrices, where n = len(p). m and n are
# initialized to have their entries be 0.
# Post-condition: m contains the number of computations made for each and every combination of matrices multiplied.
# s contains the k values that resulted in the least computations to be later used in optimal_parenth().
def bottom_up_mcm(p, m, s):
    assert len(p) >= 2
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
    return


'''
Bottom Up Matrix Multiplication: Implemented as bottom_up_mcm in code
At the beginning of each iteration of the loop of lines 5-13, m[i,j] will contain the lowest value of possible 
multiplications from the previous iteration and s[i,j] will contain the index of which the multiplication occurred from. 

Initialization: Prior to the first iteration of the loop, every position of the form m[i][i] in the m array is set to 0 
and s holds no set values.  0 is the only comparative value for the m array to be compared to and trivially is the least 
value of multiplication for the matrix multiplication. The s array has no previous iterations for which multiplications 
have occurred and therefore should be an ‘empty’ set.  Thus the loop invariant holds.

Maintenance:  There are multiple cases to be considered due to the 3 nested looping of the function. These will be dealt 
with by proving their general functionality and overall effect on the running of matrix multiplication. The loop from  
lines 6-13 runs through the values of 1 through  n-1 to 1.  This loop sets the j value for the current iteration and  
then sets the m[i,j] position in the array to the maximum value of a system.  This is to prepare the following for loop 
to find the least possible number of multiplications for this segment of the m and p arrays in the range determined 
by the first loop.  The third for loop runs from the range set by i (1 through n-1 to 1) to j-1.  At every instance in 
these ranges, the previous multiplications found in the p array and the multiplications needed in the m array are 
less than the currently stored lowest value in m[i,j], then this value is replaced and the current k value (which 
indexes the position of the multiplication array from p) is then stored in the s[i,j] position.  If at any time the 
next iterations value is less than that currently in m[i,j], then this value is replaced as described above.  If the 
opposite is true, that the value being calculated is greater than that in m[i,j], then no changes are made and the 
next iteration is started.  This repeats for all of the ranges for each of the nested loops continually finding the 
lowest value of multiplications for each m[i,j] evaluated and then storing the k value from p in s[i,j].  Thus the 
loop invariant holds for maintenance. 

Termination: After the last iteration of the loop in lines 5-13, l = n. The previous iteration ensured that the final 
iteration of m[i,j] which will be the total number of multiplications for the values stored to be multiplied in m, will  
be the minimum value of all possible branches of multiplications and previous multiplications for m[i,j] and that s[i,j] 
will hold the index of which the multiplication came from for the previous iteration.  At the end of the loop, m will 
be transformed such that at the maximum i and j, m[i,j] will contain this minimum possible value holding the minimum 
number of multiplications for the array of values in p. Thus the loop invariant holds at termination.

'''
########################################################################################################################


def memo_wrapper(p):
    n = len(p)
    s = [[0 for j in range(n)] for i in range(n)]
    m = [[0 for x in range(n)] for y in range(n)]
    memoized_matrix_chain(p, m, n, s)
    return s


########################################################################################################################


# Pre-condition: p must be a list of integers with size >= 2. m and s are n x n matrices, where n = len(p). m are
# initialized to have their entries be 0.
# Post-condition: m contains the number of computations made for each and every combination of matrices multiplied.
# s contains the k values that resulted in the least computations to be later used in optimal_parenth().
def memoized_matrix_chain(p, m, n, s):
    assert len(p) >= 2
    for i in range(n):
        for j in range(i, n):
            m[i][j] = math.inf
    return lookup_chain(m, p, 0, n-1, s)


# Pre-condition: p must be a list of integers with size >= 2, i and j are the first and last matrices respectively
# within the subset of p that are going to be multiplied. m and s are n x n matrices, where n = len(p). m is initialized
# to have it's entries be infinity for all indices representing two distinct matrices' product, and 0 for all indices of
# form m[i][i].
# Post-condition: m contains the number of computations made for each and every combination of matrices multiplied.
# s contains the k values that resulted in the least computations to be later used in optimal_parenth().
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


'''
Memoized Matrix Multiplication: Implemented as memoized_matrix_chain and lookup_chain in code
At the beginning of each iteration of the loop of lines 6-10,  m[i,j] will contain the lowest value of possible 
multiplications from the previous iteration.

Initialization: N/A.

Maintenance: There are a few possible cases to be considered for maintenance of memoized matrix multiplication but for 
proof, the timing of lookup_chain will be the portion of code being considered. Upon the entrance of lookup_chain, if 
at any time m[i,j] is less than the defaulted value of set to all m[i,j] in memoized_matrix_multiplication, the value of 
m[i,j] is returned because it is already the least possible value due to the recursive calls embedded in lookup_chain.  
If this is not the case, then if i and j are equal values then 0 is returned as there are no multiplications to be 
executed on a number and itself.  Then if neither of these conditionals are true, then a loop is introduced that runs 
from the values of the current i value to the current j value - 1.  This loop recursively runs through lookup_chain to 
find the least values possible for the current m[i,j]’s that are to be used in the multiplications and then added to the 
values found in the p array of previous multiplications.  If at any point in time, this addition produces a value less 
than the current value in m[i,j] then this value is the least possible value that has occurred and is stored in m[i,j].  
If at any time the calculated value is greater than what is currently stored in m[i,j] then that value in m[i,j] is 
already the least value of what has occurred so far and will remain.  Thus the loop invariant holds for maintenance.

Termination: After the last iteration of the loop in lines 6-10, k=j-1. The previous iteration ensured that the final 
iteration of m[i,j] which will be the total number of multiplications for the values stored to be multiplied in m, will 
be the minimum value of all possible branches of multiplications and previous multiplications for m[i,j] and then will 
be returned to memoized_matrix_chain.  Then this value is returned as it has ended the recursion of lookup_chain and  
m[i,j] will contain this minimum possible value holding the minimum number of multiplications. Thus the loop invariant 
holds at termination.
'''
########################################################################################################################
