item = ["food", "color", "location"]
item2 = ["Pizza", "Blue", "Chicago"]
control = "n"

def printfav(lista, listb):
    print("Here are all your favorites: ")
    for i in range (len(lista)):
        print(lista[i] + " : " + listb[i])

def look(stuff, lista, listb):
    print("Your favorite categories are: ", lista)
    if stuff in lista:
        print("My favorite " , stuff ," is ", listb[lista.index(stuff)])
    else:
        print("Doesn't exist")

def add(stuff, lista, listb):
    stuff = input ("Enter new category: ")
    lista.append(stuff)
    stuff = input(f"Enter your favorite for {stuff}: ")
    listb.append(stuff)

    
def delete(stuff, lista, listb):
    if stuff in lista:
        index = lista.index(stuff)
        lista.pop(index)
        listb.pop(index)
    else:
        print("Invaild, doesn't exist.")
        
def update(stuff, lista, listb):
    if stuff in lista:
        index = lista.index(stuff)
        lista.pop(index)
        listb.pop(index)
        lista.append(stuff)
        stuff = input(f"What would you like to update in {stuff}? ")
        listb.append(stuff)
    else:
        print("Invaild, doesn't exist")


while True:
    control = input("What would you like to do? (lookup/add/update/delete/quit):  ")
    if control == "lookup": 
        look(stuff = input("Which category would you like to see? "), lista = item, listb = item2)
    elif control == "add":
        add(stuff = input("Would you like to add a new favorite category? (yes/no) "), lista = item, listb = item2)
    elif control == "update":
        update(stuff = input("What catergory would you like to update? "), lista = item, listb = item2)
    elif control == "delete":
        delete(stuff = input("What would you like to delete? "), lista = item, listb = item2)
    elif control == "quit":
        break
    else:
        print("Invaild input, try again!")
    printfav(item, item2)
   
   
    