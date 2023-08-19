
# Link :  https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

def diagonalDifference(arr):

    primary_diagonal = 0
    secondary_diagonal = 0 
    
    for i in range(len(arr)):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][n-1-i]
    diagonal_diff = abs(primary_diagonal - secondary_diagonal)
    return diagonal_diff

n = int(input().strip())
arr =[]

for j in range(n):
    arr.append(list(map(int,input().rstrip().split())))

result = diagonalDifference(arr)
print(result)