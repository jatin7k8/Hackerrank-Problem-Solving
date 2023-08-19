# def plusMinus(arr):
#     p = n = z = 0
#     for i in range(len(arr)):
#         if arr[i]>0:
#             p += 1
#         elif arr[i]<0:
#             n += 1
#         else:
#             z += 1
#     print(p/len(arr))
#     print(n/len(arr))
#     print(z/len(arr))   

# n = int(input().strip())
# arr = list(map(int,input().rstrip().split()))
# plusMinus(arr)

'''--------------------------------------------------------------'''

def plusMinus(arr):
    p = n = z = 0
    i = 0
    while len(arr)>i:
        if arr[i]>0:
            p += 1
        elif arr[i]<0:
            n += 1
        else:
            z += 1
        i += 1
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))   

n = int(input().strip())
arr = list(map(int,input().rstrip().split()))
plusMinus(arr)



