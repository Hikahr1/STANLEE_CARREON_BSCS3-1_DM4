#part of python
#1
hometown = "Santiago City"
population = "69,000"
province =  "Isabela"

print(hometown)
print(population)
print(province)

#2
P = float(input("Principal interest:"))
R = float(input("Rate:"))
T = float(input("Time:"))

def interest ():
    return (P * R * T)/100
print(interest())

#3 and or not
num1 = float(input("First number:"))
num2 = float(input("Second number:"))

if num1 == num2 :
    print("num 1 and num 2 is same")
if num1 == 0 or num2 == 0:
    print("num 1 and num2 is zero")
if num1 !=1 and num2 !=1:
    print("num 1 and num2 is not 1")

#control statements

#divisible by 3

number = int(input("Input number to be checked by div3:"))

def checker():

    if number % 3 == 0 :
        return "Number is divisible by 3"
    else:
        return "Number is not divisible by 3"

print(checker())

#grades checker

grade = float(input("Grade:"))
if grade >= 95:
    print("Outstanding")
elif grade >= 85:
    print("Very Good")
elif grade >= 75:
    print("Passed")
else:
    print("Failed")

#print first 10 prime

y = 2
x = 0
while y < 10:
    print(y)
    y += 2
    x +=1

#print number 1 - 10 skip 2 stop 9

for i in range (1,11):
    if i == 2:
        continue
    if i == 9:
        break
    print(i)

