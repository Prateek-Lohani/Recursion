def print_n_to_1(num):
    if num==0:
        return
    print(num)
    print_n_to_1(num-1)
    
    return


num=int(input())
print_n_to_1(num)