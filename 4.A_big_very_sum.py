# def aVeryBigSum(ar):
#     sum_val = 0
#     for i in ar:
#         sum_val += i
#     return sum_val

# arr_count = list(map(int,input().strip()))
# ar = list(map(int,input().rstrip().split()))
# result = aVeryBigSum(ar)
# print(result)

'''-------------using by while loop'''

def aVeryBigSum(ar):
    sum_val = 0
    i = 0
    while len(ar)>i:
        sum_val += ar[i]
        i += 1
    return sum_val

arr_count = list(map(int,input().strip()))
ar = list(map(int,input().rstrip().split()))
result = aVeryBigSum(ar)
print(result)