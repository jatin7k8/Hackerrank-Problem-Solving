#Link : https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*(i))
n = int(input())
staircase(n)