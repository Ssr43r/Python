friends = []

while True:
    print(" 1.add \n 2.remove \n 3.list friend \n 4.search name \n 5.edit name \n 6.clear list \n 7.exit")
    user_input = input("What are you doing? ").lower().strip()
# ADD
    if user_input in ("1", "add"):
        while True:
            name = input("Enter name to add (type /stop to exit): ").strip()
            if name.lower() == "/stop":
                break
            friends.append(name)
            print(f"add {name} in list.")
# REMOVE
    elif user_input in ("2", "remove"):
        while True:
            name = input("Enter name to remove (type /stop to exit): ").strip()
            if name == "/stop":
                break
            if name in friends:
                print("yes to remove / no to cancle.")
                confirm = input(f"are you confirm remove {name}: ").lower().strip()
                if confirm == "yes":
                    friends.remove(name)
                    print(f"{name} remove to friends.")
                elif confirm == "no":
                    break
                else:
                    print("Invaliable cheack again.")
            else:
                print("Not found!!!")

                                
# SHOW
    elif user_input in ("3", "list friends"):
        while True:
            if len(friends) == 0:
                print("No friends.")
            else:
                i = 0
                while i < len(friends):
                    print(f"{i+1}. {friends[i]}")
                    i += 1
            again = input("Refresh list? (yes to refresh/no to stop): ").lower()
            if again != "yes":
                break
    #search name
    elif user_input in ("4" , "search name"):
        while True:
            name = input("Put name your friends (type /stop to exit): ")
            if name in friends:
                print(f"{name} in the list")
            elif name == "/stop":
                break
            else:
                print("Not found!!!")
    #edit name
    elif user_input in ("5" , "edit name"):
        while True:
            old = input("In put name your friends to edit(tpye /stop to exit.): ")
            if old in friends:
                new = input("New name: ").lower()
                index = friends.index(old)
                friends [index] = new
                print("Update!!!")
            elif old == "/stop":
                break
            else:
                print("Not found!!!")
#Clear list
    elif user_input in ("6" , "Clear list"):
        while True:
            sure = input("Do you want clear list.(yes to clear / no to cancle and exit.)").lower()
            if sure == "yes":
                friends.clear()
                print("Claer list your friends.")
            elif sure == "no":
                break
            else:
                print("Inviable cmd.")
# Exit
    elif user_input in ("7", "exit"):
        print("End program!!!")
        break
    else:
        print("Error!!! Read a menu.")