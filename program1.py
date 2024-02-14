#Basis input / output
a=input("Enter your name\n")
print(type(a))
print(type(20))
print(type(True))

#String built-in methods
b="  Dishi Pandey   "
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("Pandey","22cse034"))

string="one, two, three, four, five"
print(string.split(','))
print(string.count("o"))
print(string.find("g"))
print(string.index("h"))

#Looping and slicing  
for x in "GwecAjmer":
    print(x.upper(), end="")
    break

string1 = "abcdefgh"
print(string1[2:8])
print(string1[ :6])
print(string1[ :9:2])
print(string1[-8:-3])
print(string1[-2:-7:-1])
print(string1[:])
print(string1[: :-1])


#String formatting
Qty=2
price=100.506
store="Ajmer store"

A1="Order from {} has been placed for Quantity {} for price{}"
print (A1.format(store, Qty, price))

msg=F"Order from {store} has been placed for Quantity {Qty} for price{price}"
print(msg)
