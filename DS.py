Dict = {}

print("Please enter your information:")
d1 = input("Name: ")
d2 = input("Age: ")
d3 = input("Years Coding:")

Dict["Name"] = d1
Dict["Age"] = d2
Dict["Years Coding"] = d3

print("Please enter your three first programming languages.")
t1 = input("#1: ")
t2 = input("#2: ")
t3 = input("#3: ")

tuple = (t1, t2, t3)

print("Please enter your three favorite programming languages.")
l1 = input("#1: ")
l2 = input("#2: ")
l3 = input("#3: ")

lost = [l1, l2, l3]

st = set(tuple)
sl = set(lost)
set = list(st.intersection(sl))

print(Dict)
print(tuple)
print(lost)
print(set)

