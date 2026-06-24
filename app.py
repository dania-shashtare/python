# print even numbers from 1 to 9 using for loop

num = 0
count = 0
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
        count += 1

print(f"we have {count} even numbers")

# print even numbers from 1 to 9 using while loop

num2 = 0
count2 = 0
while num2 < 9:
    num2 += 1
    if num2 % 2 == 0:
        print(num2)
        count2 += 1

print(f"we have {count2} even numbers")
