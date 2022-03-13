def print_1_to_n(num):
    if num==0:
        return
    print_1_to_n(num-1)
    print(num)
    return


num=int(input())
print_1_to_n(num)
