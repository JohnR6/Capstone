print("Please input the employee's name:")
first = input("First name: ")
last = input("Last name: ")
print("Please input the employee's age and year of birth:")
age = input("Age: ")
year = input("Birth Year: ")
print("Thank you.")
email = first + "." + last + year[-2:] + "@company.com"
print(email)