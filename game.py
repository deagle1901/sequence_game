def minDistanceDynamic(s1, s2):
    x = len(s1) + 1 
    y = len(s2) + 1 

    A = [[-1 for i in range(y)] for j in range(x)]
    for i in range(x):
        A[i][0] = i

    for j in range(y):
        A[0][j] = j

    for i in range(1, x):
        for j in range(1, y):
            if s1[i- 1] == s2[j - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(
                        A[i - 1][j] + 1,
                        A[i][j - 1] + 1,
                        A[i - 1][j - 1] + 1
                        )
    return A[x-1][y-1]
n=int(input())
s1=list(map(int,input().strip().split()))
m=int(input())
s2=list(map(int,input().strip().split()))
print(minDistanceDynamic(s1, s2))
