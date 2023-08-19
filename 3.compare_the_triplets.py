
# link := https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

# def compareTriplets(a,b):
#     ap = bp = 0
#     length = len(a)
#     for i in range(length):
#         if a[i]> b[i]:
#             ap += 1
#         elif b[i] >a[i]:
#             bp += 1
#     return ap, bp


# a = list(map(int, input().rstrip().split()))
# b = list(map(int, input().rstrip().split()))

# result = compareTriplets(a,b)
# print(result)

'''-----------------------------------------------------------------------------------------------'''
def compareTriplets(a,b):
    alice = bob = 0
    i = 0
    while i< len(a):
        if a[i] >b[i]:
            alice += 1
        elif b[i]>a[i]:
            bob += 1
        i += 1

    return alice, bob


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

result = compareTriplets(a,b)
print(result)