# 1.1. For loops
factorial = 1
# n = int(input("Enter the number (positive integer) n: "))  # factorial from 5
n = 5  # factorial from 5
for i in range(1, n + 1):
    factorial *= i
print(factorial)
print('---------------------------------')
# n = int(input("Enter the number of rows: "))
n = 4
# loop through rows
for i in range(1, n + 1):
    # print asterisks separated by spaces
    for j in range(i):
        print("*", end=" ")
        # move to the next line after each row is printed
    print()
print('---------------------------------')
n = 4
# loop through rows in descending order
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end=' ')
    for j in range(2 * i - 1):
        print('*', end=' ')
    print()
print('#################################')
# 1.2. While loops
result = 0
while n > 0:
    n = n // 10
    result += 1
print(result)
print('---------------------------------')
a = 0
b = 1
n = 13
while a <= n:
    print(a)
    c = a +b
    a = b
    b = c
print('#################################')
# 1.3. Looping over collections of values
days = {'mon': 'Monday', 'tue': 'Tuesday', 'wed': 'Wednesday', 'thu': 'Thursday', 'fri': 'Friday',
'sat': 'Saturday', 'sun': 'Sunday'}

for day in days:
    print(day, 'stands for', days[day])