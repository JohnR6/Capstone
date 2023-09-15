print("Importing my_module.py...")

def give_int(num):
    while True:
        try:
            num = int(input("Input integer: "))
            print("Recieved: ", num)
        except Exception:
            print("This is not an int.")
        return(num)