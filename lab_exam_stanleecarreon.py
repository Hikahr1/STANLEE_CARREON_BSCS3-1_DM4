import sys
#Stanlee Carreon BSCS 3-1
#Prelim Exam Lab

#Task 1
print("Enter grade: ")
grade = int(input())

def grade_student():

    if grade >100 or grade < 0:
        print("invalid grade")

    else:
        if grade >= 90:
            print("A")
        elif grade >= 80:
            print("B")
        elif grade >= 70:
            print("C")
        elif grade >= 60:
            print("D")
        else:
            print("F")

grade_student()
print("\n")

#Task 2
print("String Manipulation")
print("Enter Words: ")
words = input()

def process_string():
    upper = words.upper()
    reverse = words[::-1]

    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels = set(vowel_list)
    vowel_counter = 0
    for char in words:
        if char in vowels:
            vowel_counter += 1

    return upper, reverse, vowel_counter


upper_word, reverse_word, vowel_counter_word = process_string()
print("upper word: ", upper_word)
print("reverse word: ", reverse_word)
print("vowel count: ", vowel_counter_word)
print("\n")

#Task 3 looping and list
print("Enter 5 Numbers: ")

def sum_and_average():
    numbers = []
    sum_value = 0
    for i in range(5):
        number = float(input("enter number: "))
        numbers.append(number)
        sum_value += number
    average = sum_value / 5

    return numbers, average, sum_value

numbers_list, numbers_average, numbers_sum = sum_and_average()
print("numbers_list: ", numbers_list)
print("numbers_sum: ", numbers_sum)
print("numbers_average: ", numbers_average)
print("\n")

#Task 4 CLI
if len(sys.argv) > 1:
    filename = sys.argv[1]
    try:
        with open(filename, "r") as f:
            content = f.read()
            print("File Content:\n")
            print(content)
    except FileNotFoundError:
        print("File not found.")
else:
    print("No file provided.")


#Task 5 Arguments

def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="Alice", age=25, city="Tokyo")

