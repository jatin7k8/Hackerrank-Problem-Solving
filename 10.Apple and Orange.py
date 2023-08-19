
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = 0
    oranges_count = 0
    for i in range(len(apples)):
        if s<= a + apples[i] <= t:
            apples_count += 1
    for j in range(len(oranges)):
        if s<= b + oranges[j] <=t:
            oranges_count += 1
    print(apples_count)
    print(oranges_count)

first_multiple_input = input().rstrip().split()
s = int(first_multiple_input[0]) # sam house starting point
t = int(first_multiple_input[1]) # sam house ending point

second_multiple_input = input().rstrip().split()
a = int(second_multiple_input[0]) # Location of apple
b = int(second_multiple_input[1]) # location of orange

third_multiple_input = input().rstrip().split()
m  = int(second_multiple_input[0]) # no of apple
n = int(second_multiple_input[1]) # no of orange

apples = list(map(int,input().rstrip().split()))
oranges = list(map(int,input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
