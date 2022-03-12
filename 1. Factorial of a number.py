def fact(n):
    if n==0:
        return 1
    small_output=fact(n-1)
    return n*small_output

n=int(input("Enter a number: "))
print(fact(n))