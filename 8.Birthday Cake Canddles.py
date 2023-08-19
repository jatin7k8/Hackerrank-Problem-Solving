# Link :  https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true




'''1 st methode'''
# def birthdayCakeCandles(candles):
#     max_unit = max(candles)
#     count = 0
#     for i in range(len(candles)):
#         if candles[i] == max_unit:
#             count += 1
#     return count

# candles_count = int(input().strip())
# candles = list(map(int,input().rstrip().split()))
# result = birthdayCakeCandles(candles)
# print(result)

'''2nd methode'''

def birthdayCakeCandles(candles):
    max_unit = max(candles)
    count = 0
    for i in range(len(candles)):
        if candles[i] == max_unit:
            count += 1
    return count

candles_count = int(input().strip())
candles = list(map(int,input().rstrip().split()))
result = birthdayCakeCandles(candles)
print(result)