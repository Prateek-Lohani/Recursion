def last_Index(a,n,si):
    l=len(a)
    if si==l:
        return -1
    smaller_list=last_Index(a,n,si+1)
    if smaller_list!=-1:
        return smaller_list
    else:
        if a[si]==x:
            return si
        else:
            return -1
 
arr=[1,2,3,4,5,3,6,7,6,3,4,6]
x=6
start_index=0
print(last_Index(arr,x,start_index))