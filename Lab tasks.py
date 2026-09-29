# Question = 01

my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
smallest = my_list[0]

for num in my_list:
    if num < smallest:
        smallest = num

print(smallest)

# Question = 02

my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
total_sum = 0

for num in my_list:
    total_sum += num

average = total_sum / len(my_list)
print(average)

# Question = 03

students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
name = input("Enter a student name: ")

if name in students:
    print("Student Found")
else:
    print("Student Not Found")

# Question = 04

shopping = []

for i in range(5):
    item = input("Enter a shopping item: ")
    shopping.append(item)

print(shopping)
