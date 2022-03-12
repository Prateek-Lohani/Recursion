def power(x,y):
    
    
    if  y==0:
        return 1
    small_output=(x)**(y-1)
    return x*small_output
    




a, b = input().split()
a = int(a)
b = int(b)

print(power(a,b))