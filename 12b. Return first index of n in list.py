def firstIndex(arr,si,x):
    # Please add your code here
    l=len(arr)
    
    if si==l:
        return -1
    if arr[si]==x:
        return si
    
    return firstIndex(arr,si+1,x)
        

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
start_index=0
print(firstIndex(arr,start_index,x))