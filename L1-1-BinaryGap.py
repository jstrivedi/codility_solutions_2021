def solution(N):
    # write your code in Python 3.6
    # pass
    binary = str(format(N,'b'))
    
    ones = []
    for i in range(len(binary)):
        if binary[i]=='1':
            ones.append(i)
    ans = 0

    for i in range(len(ones)-1):
        a = ones[i+1]-ones[i]-1
        if a > ans:
            ans=a
    return ans
