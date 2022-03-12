def sum_of_nNaturals(n):
    if n==0:
        return 0
    small_output=sum_of_nNaturals(n-1)
    return n+small_output

n=int(input())
print(sum_of_nNaturals(n))
    