def isSorted(a,si):
    l=len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    is_smaller_sorted=isSorted(a,si+1)  
    return is_smaller_sorted
    



arr=[1,2,3,4,5]
start_index=0

print(isSorted(arr,start_index))