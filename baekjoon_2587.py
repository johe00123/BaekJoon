import sys

numbers = [int(input()) for _ in range(5)]
print(sum(numbers) // 5) #평균
numbers.sort()
print(numbers[2]) #중앙값