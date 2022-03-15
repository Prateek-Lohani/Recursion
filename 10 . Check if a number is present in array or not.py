def checkNumber(arr, x):
    # Please add your code here
    l=len(arr)
    if l==1:
        return x==arr[0]
    small_array=arr[:l-1]
    check_smallarray=checkNumber(small_array,x)
    return check_smallarray or (x==arr[l-1])
    


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
