# link: https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true

'''def simpleArraysSum(ar):
    return sum(ar)

ar_count = int(input().strip())
ar = list(map(int,input().rstrip().split()))
result = simpleArraysSum(ar)
print(result)
print(ar)
'''

# 2nd methode
'''def simpleArraysSum(ar):
    total_sum = 0 
    for i in range(len(ar)):
        total_sum += ar[i]
    return total_sum
ar_count = int(input().strip())
ar = list(map(int,input().rstrip().split()))
result = simpleArraysSum(ar)
print(result)
print(ar)'''

# 3rd using by while loop
def simpleArraysSum(ar):
    total_sum = 0 
    i = 0
    while i<len(ar):
        total_sum += ar[i]
        i += 1
    return total_sum
ar_count = int(input().strip()) # it is not impacting on bellow line that code 
ar = list(map(int,input().rstrip().split()))
result = simpleArraysSum(ar)
print(result)
print(ar)