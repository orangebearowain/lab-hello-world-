item = ["food", "color", "location"]
item2 = ["Pizza", "Blue", "Chicago"]
items = 0
end = "e"

while True:
    print("Your favorite categories are: ", item)
    items = input("Which category would you like to see? ")
    if items in item:
        print("My favorite " , items ," is ", item2[item.index(items)])
    else:
        print("Doesn't exist")
    items = input("Would you like to add a new favorite category? (yes/no) ")
    if items == "yes":
        items = input ("Enter new category: ")
        item.append(items)
        items = input(f"Enter your favorite for {items}: ")
        item2.append(items)
    else:
        print("Invalid input")
    print("Here are all your favorites: ")
    for i in range (len(item)):
        print(item[i] + " : " + item2[i])
    end = input("Would you like to end?  ")
    if end == "yes":
        break
        