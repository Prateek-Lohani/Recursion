def sumArray(arr):
    # Please add your code here
    l=len(arr)
    if l==0:
        return 0
    if l==1:
        return arr[0]
    
    small_array=arr[1:]
    sum_of_small_array=sumArray(small_array)
    
    return arr[0]+sum_of_small_array
    
    
    
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))