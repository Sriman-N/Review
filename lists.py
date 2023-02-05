#creating lists
my_list = ["apple", "banana", "cherry"]

print(my_list)


my_list = ["apple", "banana", "cherry", "apple", "cherry"]

print(my_list)

print(len(my_list))

thislist = list(("apple", "banana", "cherry"))

print(thislist)

#accessing list items
print(my_list[0])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#changing item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)