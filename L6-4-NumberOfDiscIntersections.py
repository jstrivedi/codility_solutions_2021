# Wasn't able to write an efficient algorithm for this one. The easy solution gave only 50% score as it ran with O(N^2). 
#John Mee has written an efficient algorithm for this problem 
#and he has made it available on Github: https://github.com/johnmee/codility/blob/master/ex-6-4-NumberOfDiscIntersections.py



# Task description
# We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

# The figure below shows discs drawn for N = 6 and A as follows:

#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0


# There are eleven (unordered) pairs of discs that intersect, namely:

# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:

# def solution(A)

# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# Given array A shown above, the function should return 11, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].

def solution(A):
    # write your code in Python 3.6
    # pass
    N= len(A)
    if N<2:
        return 0
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if A[i]+A[j]>=abs(i-j):ans+=1
            if ans>10000000:return -1
    return ans
