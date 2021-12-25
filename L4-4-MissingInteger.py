# Task description
# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    # write your code in Python 3.6
    # pass
    sorA = sorted(A)
    if sorA[-1]<1: return 1
    if 1 not in sorA: return 1
    else:
        idx = sorA.index(1)
        possorA = sorA[idx:]
        num = 0
        for i in range(1,possorA[-1]):
            flag=0
            while possorA[num]==i:
                flag +=1
                # possorA.remove(i)
                num+=1
            if flag==0: return i
        return sorA[-1]+1
