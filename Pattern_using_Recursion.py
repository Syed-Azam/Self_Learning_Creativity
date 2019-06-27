# A Pattern Generator using Recursion
def pat(n):
    print('█'*n, ' '*n, '█'*n)
    if n > 1:
        pat(n-1)
    print('█'*n, ' '*n, '█'*n)

pat(10)
input()