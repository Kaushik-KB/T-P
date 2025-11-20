# Name: Kaushik Barnwal
# Enrollment: 0157AL231102
# batch : 5 Batch 
# Time : (10.30)
# Python Assignment: Loops and Conditional statements


# Part A: Basic If-else Conditional Problems
# ================================================

# Question 1: Check if a number is positive, negative, or zero ===
print("\n--- Question 1 ---")
val = int(input("Input a number: "))
if val > 0:
    print(f"The number {val} is positive.")
elif val < 0:
    print(f"The number {val} is negative.")
else:
    print("The number is zero.")


# Question 2: Check if a number is even or odd ===
print("\n--- Question 2 ---")
num = int(input("Input a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


# Question 3: Check if a year is a leap year ===
print("\n--- Question 3 ---")
year = int(input("Input a year: "))
is_leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
    else:
        is_leap = True

if is_leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Question 4: Find the greater of two numbers ===
print("\n--- Question 4 ---")
x = int(input("Input the first number: "))
y = int(input("Input the second number: "))
if x > y:
    print(f"The greater number is {x}.")
elif y > x:
    print(f"The greater number is {y}.")
else:
    print("Both numbers are equal.")


# Question 5: Check voting eligibility ===
print("\n--- Question 5 ---")
person_age = int(input("Input age: "))
if person_age >= 18:
    print("This person is eligible to vote.")
else:
    print("This person is not eligible to vote.")


# Question 6: Check for a vowel or consonant ===
print("\n--- Question 6 ---")
character = input("Input a character: ")
vowel_list = ['a', 'e', 'i', 'o', 'u']
if character.lower() in vowel_list:
    print(f"'{character}' is a vowel.")
else:
    print(f"'{character}' is a consonant.")


# Question 7: Check if divisible by 5 ===
print("\n--- Question 7 ---")
num_check = int(input("Input a number: "))
if num_check % 5 == 0:
    print(f"{num_check} is divisible by 5.")
else:
    print(f"{num_check} is not divisible by 5.")


# Question 8: Check number of digits ===
print("\n--- Question 8 ---")
val = int(input("Input a positive number: "))
if 0 <= val <= 9:
    print("It is a single-digit number.")
elif 10 <= val <= 99:
    print("It is a two-digit number.")
else:
    print("It has more than two digits.")


# Question 9: Check if passed or failed ===
print("\n--- Question 9 ---")
score = int(input("Input marks: "))
if score >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")


# Question 10: Check if a multiple of 3 and 7 ===
print("\n--- Question 10 ---")
num_val = int(input("Input a number: "))
if num_val % 21 == 0:
    print(f"{num_val} is a multiple of both 3 and 7.")
else:
    print(f"{num_val} is not a multiple of both 3 and 7.")

# Part B: Ladder if & Nested if else
# ================================================

# Question 11: Find the greatest among three numbers ===
print("\n--- Question 11 ---")
n1 = int(input("Input the first number: "))
n2 = int(input("Input the second number: "))
n3 = int(input("Input the third number: "))
largest = n1
if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3
print(f"The largest number is {largest}.")


# Question 12: Classify a person based on age ===
print("\n--- Question 12 ---")
age_val = int(input("Input age: "))
if age_val < 13:
    category = "Child"
elif age_val <= 19:
    category = "Teenager"
elif age_val <= 59:
    category = "Adult"
else:
    category = "Senior"
print(f"This person is a {category}.")


# Question 13: Assign grades based on marks ===
print("\n--- Question 13 ---")
marks = int(input("Input marks: "))
grade = ''
if 90 <= marks <= 100:
    grade = "A"
elif 75 <= marks <= 89:
    grade = "B"
elif 50 <= marks <= 74:
    grade = "C"
elif 35 <= marks <= 49:
    grade = "D"
else:
    grade = "Fail"
print(f"The grade is: {grade}")


# Question 14: Check the type of triangle ===
print("\n--- Question 14 ---")
s1 = int(input("Input side 1: "))
s2 = int(input("Input side 2: "))
s3 = int(input("Input side 3: "))
if s1 == s2 and s2 == s3:
    print("The triangle is Equilateral.")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")


# Question 15: Check the type of character ===
print("\n--- Question 15 ---")
inp_char = input("Input a character: ")
if inp_char.islower():
    print("The character is lowercase.")
elif inp_char.isupper():
    print("The character is uppercase.")
elif inp_char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special symbol.")


# Question 16: Calculate electricity bill ===
print("\n--- Question 16 ---")
units = int(input("Input units consumed: "))
total_bill = 0
if units <= 100:
    total_bill = units * 5
elif units <= 200:
    total_bill = (100 * 5) + ((units - 100) * 7)
else:
    total_bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print(f"Total electricity bill: {total_bill}")


# Question 17: Find the largest of four numbers ===
print("\n--- Question 17 ---")
val1 = int(input("Input number 1: "))
val2 = int(input("Input number 2: "))
val3 = int(input("Input number 3: "))
val4 = int(input("Input number 4: "))
max_val = val1
if val2 > max_val:
    max_val = val2
if val3 > max_val:
    max_val = val3
if val4 > max_val:
    max_val = val4
print(f"The largest value is {max_val}.")


# Question 18: Check for a century leap year ===
print("\n--- Question 18 ---")
check_year = int(input("Input a year: "))
if check_year % 100 == 0:
    if check_year % 400 == 0:
        print("This is a century leap year.")
    else:
        print("This is a century year, but not a leap year.")
else:
    print("This is not a century year.")


# Question 19: Classify BMI value ===
print("\n--- Question 19 ---")
bmi_val = float(input("Input BMI value: "))
if bmi_val < 18.5:
    result = "Underweight"
elif bmi_val < 25:
    result = "Normal"
elif bmi_val < 30:
    result = "Overweight"
else:
    result = "Obese"
print(f"The BMI category is: {result}")


# Question 20: Find the smallest of three numbers ===
print("\n--- Question 20 ---")
v1 = int(input("Input number 1: "))
v2 = int(input("Input number 2: "))
v3 = int(input("Input number 3: "))
smallest = v1
if v2 < smallest:
    smallest = v2
if v3 < smallest:
    smallest = v3
print(f"The smallest value is {smallest}.")

# Part C: For Loop Problems
# ================================================

# Question 21: Find Armstrong numbers between 100 and 999 ===
print("\n--- Question 21 ---")
for num_iter in range(100, 1000):
    total = 0
    temp_num = num_iter
    while temp_num > 0:
        digit = temp_num % 10
        total += digit ** 3
        temp_num //= 10
    if num_iter == total:
        print(num_iter)


# Question 22: Generate the first n prime numbers ===
print("\n--- Question 22 ---")
limit = int(input("How many prime numbers to generate?: "))
primes_found = 0
check_num = 2
while primes_found < limit:
    is_prime_flag = True
    for i in range(2, int(check_num**0.5) + 1):
        if check_num % i == 0:
            is_prime_flag = False
            break
    if is_prime_flag:
        print(check_num)
        primes_found += 1
    check_num += 1


# Question 23: Numbers from 1 to 500 divisible by 3 with digit sum <= 10 ===
print("\n--- Question 23 ---")
for i in range(1, 501):
    if i % 3 == 0:
        digit_sum = sum(int(digit) for digit in str(i))
        if digit_sum <= 10:
            print(i)


# Question 24: Print a pyramid of stars ===
print("\n--- Question 24 ---")
height = int(input("Input pyramid height: "))
for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))


# Question 25: Check if a string is a pangram ===
print("\n--- Question 25 ---")
text = input("Input a string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
found_letters = set()
for char in text.lower():
    if char in alphabet:
        found_letters.add(char)
if len(found_letters) == 26:
    print("The text is a pangram.")
else:
    print("The text is not a pangram.")


# Question 26: Find twin primes between 1 and 100 ===
print("\n--- Question 26 ---")
prime_list = []
for num in range(2, 101):
    is_p = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_p = False
            break
    if is_p:
        prime_list.append(num)

for i in range(len(prime_list) - 1):
    if prime_list[i+1] - prime_list[i] == 2:
        print(f"({prime_list[i]}, {prime_list[i+1]})")


# Question 27: Check for a Harshad number ===
print("\n--- Question 27 ---")
num_input_str = input("Input a number: ")
num_val = int(num_input_str)
sum_of_digits = 0
for digit_char in num_input_str:
    sum_of_digits += int(digit_char)
if num_val > 0 and num_val % sum_of_digits == 0:
    print("This is a Harshad Number.")
else:
    print("This is not a Harshad Number.")


# Question 28: Generate Pascal's Triangle ===
print("\n--- Question 28 ---")
rows = int(input("Input number of rows: "))
current_row = [1]
for i in range(rows):
    print(" ".join(map(str, current_row)))
    next_row = [1]
    for j in range(len(current_row) - 1):
        next_row.append(current_row[j] + current_row[j+1])
    next_row.append(1)
    current_row = next_row


# Question 29: Calculate the sum of squares series ===
print("\n--- Question 29 ---")
n_limit = int(input("Input the value of n: "))
total_sum = 0
for i in range(1, n_limit + 1):
    total_sum += i * i
print(f"The sum is: {total_sum}")


# Question 30: Check for a Strong number ===
print("\n--- Question 30 ---")
facts = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}
num_str = input("Input a number: ")
fact_sum = 0
for digit in num_str:
    fact_sum += facts[digit]
if fact_sum == int(num_str):
    print("This is a Strong Number.")
else:
    print("This is not a Strong Number.")

# Part D: While Loop Problems
# ================================================

# Question 31: Reverse a number and check if the reverse is prime ===
print("\n--- Question 31 ---")
original_num = int(input("Input a number: "))
reversed_num = 0
temp = original_num
while temp > 0:
    reversed_num = (reversed_num * 10) + (temp % 10)
    temp //= 10

is_p_flag = True
if reversed_num < 2:
    is_p_flag = False
else:
    divisor = 2
    while divisor * divisor <= reversed_num:
        if reversed_num % divisor == 0:
            is_p_flag = False
            break
        divisor += 1
if is_p_flag:
    print(f"The reversed number {reversed_num} is prime.")
else:
    print(f"The reversed number {reversed_num} is not prime.")


# Question 32: Accept numbers until the sum of their digits exceeds 100 ===
print("\n--- Question 32 ---")
master_sum = 0
while master_sum <= 100:
    print(f"Current sum of all digits: {master_sum}")
    inp_str = input("Input a number: ")
    current_digit_sum = sum(int(digit) for digit in inp_str)
    master_sum += current_digit_sum
print(f"The final sum {master_sum} has exceeded 100.")


# Question 33: Check for a Duck number ===
print("\n--- Question 33 ---")
num_as_str = input("Input a number: ")
if num_as_str[0] != '0' and '0' in num_as_str:
    print("This is a Duck Number.")
else:
    print("This is not a Duck Number.")


# Question 34: Check for a Happy number ===
print("\n--- Question 34 ---")
num = int(input("Input a number: "))
history = set()
while num != 1 and num not in history:
    history.add(num)
    num = sum(int(digit)**2 for digit in str(num))
if num == 1:
    print("This is a Happy Number.")
else:
    print("This is not a Happy Number.")


# Question 35: Find the largest prime factor of a number ===
print("\n--- Question 35 ---")
num = int(input("Input a number: "))
largest_factor = -1
d = 2
temp_val = num
while d * d <= temp_val:
    while temp_val % d == 0:
        largest_factor = d
        temp_val //= d
    d += 1
if temp_val > 1:
    largest_factor = temp_val
print(f"The largest prime factor is: {largest_factor}")


# Question 36: Repeatedly accept a string until it is a palindrome ===
print("\n--- Question 36 ---")
while True:
    text_input = input("Input a string: ")
    reversed_text = "".join(reversed(text_input))
    if text_input == reversed_text:
        print("Palindrome detected. Exiting loop.")
        break


# Question 37: Find the digital root of a number ===
print("\n--- Question 37 ---")
num = int(input("Input a number: "))
while num >= 10:
    num = sum(int(digit) for digit in str(num))
print(f"The digital root is: {num}")


# Question 38: Generate the Collatz sequence ===
print("\n--- Question 38 ---")
n = int(input("Input a number: "))
while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(1)


# Question 39: Check for a Kaprekar number ===
print("\n--- Question 39 ---")
k_num = int(input("Input a number: "))
square_str = str(k_num**2)
is_kaprekar = False
for i in range(1, len(square_str)):
    part1_str = square_str[:i]
    part2_str = square_str[i:]
    if part1_str and part2_str:
        part1 = int(part1_str)
        part2 = int(part2_str)
        if part1 > 0 and part2 > 0 and part1 + part2 == k_num:
            is_kaprekar = True
            break
if is_kaprekar:
    print("This is a Kaprekar Number.")
else:
    print("This is not a Kaprekar Number.")


# Question 40: Simulate an ATM machine ===
print("\n--- Question 40 ---")
balance = 1000
while True:
    print("\n-- ATM --")
    print("1. View Balance")
    print("2. Make a Deposit")
    print("3. Make a Withdrawal")
    print("4. Quit")
    choice = int(input("Select an option: "))
    if choice == 1:
        print(f"Your current balance is: {balance}")
    elif choice == 2:
        deposit_amt = int(input("Enter deposit amount: "))
        balance += deposit_amt
    elif choice == 3:
        withdraw_amt = int(input("Enter withdrawal amount: "))
        if withdraw_amt <= balance:
            balance -= withdraw_amt
        else:
            print("Action failed: Insufficient funds.")
    elif choice == 4:
        break
    else:
        print("Invalid option selected.")
