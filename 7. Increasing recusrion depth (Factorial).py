import sys

sys.setrecursionlimit(2000)

def fact(num):
    if num==0:
        return 1
    small_Output=fact(num-1)
    return num*small_Output

n=int(input())
print(fact(n))
