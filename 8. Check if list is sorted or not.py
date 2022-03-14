def isSorted(li):
    
    l=len(li)
    if l==0 or l==1:
        return True
    if li[0]>li[1]:
        return False
        
    small_list=li[1:]
    small_list_sorted=isSorted(small_list)
    if small_list_sorted:
        return True
    else:
        return False
    
    
    
li=[1,3,5,7,8,9]  
print(isSorted(li))