A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
w = 1
n = 10
while w%2==1:
    if A[n//2]%2 == 0 and A[n // 2 - 1]%2 == 1:
        w = A[n // 2]
        print(w)
    elif A[n//2]%2 == 0:
        n=n-n//2
    else:
        n=n+n//2


