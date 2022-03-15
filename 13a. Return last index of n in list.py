def last_Index(a,n):
    l=len(a)
    if l==0:
        return -1
    small_arraay=a[1:]
    last_Index_small=last_Index(small_arraay,x)
    if last_Index_small!=-1:
        return last_Index_small+1
    else:
        if a[0]==n:
            return 0
        else:
            return -1



arr=[1,2,3,4,5,3,6,7,6,3,4,6]
x=6
print(last_Index(arr,x))