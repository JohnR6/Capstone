import datetime
employees = list()
def add_new_employee():
    first = input("First name: ")
    last = input("Last name: ")
    while True:
        try:
            age = int(input("Age: "))
        except:
            print("You did not enter a proper age")
        else:
            break
    email = f"{first}.{last}{str(datetime.date.today().year - age)[-2:]}@company.com"
    print(f"{first} {last} added to records with the email '{email}'")
    employees.append({"first_name" : first, "last_name" : last, "age" : age, "email" : email})

cont = True
while(cont):
    try:
        print("How many employees will you be adding? ")
        num = input()
        num = int(num)
        print(num)
        if not num.isdigit():
            raise Exception
    except Exception:
        print("That is not a num")
    else:
        cont = False
for i in range(num):
    add_new_employee()
