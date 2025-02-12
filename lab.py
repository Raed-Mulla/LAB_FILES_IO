def io():
    while True:
        choice = input("do you want to add a new To-Do item? answer by [y/n/exit]")

        if choice == "exit":
            print("thank you for using the To-Do program, come back again soon")
            break
        elif choice == "y":
            add_To_do = input("enter your new to-do items :")
            with open("To-Do.txt","a",encoding="UTF-8") as file:
                file.write(add_To_do + "\n")
            print("add successfully \n")
        
        elif choice == "n":
            view_To_do = input("do you want to list your To-Do items ? answer by [y/n]")

            if view_To_do == "y":
                with open("To-Do.txt","r",encoding="UTF-8") as file:
                    todo =file.readlines()
                    if todo:
                        print("Your To-Do List:")
                        for index , item in enumerate(todo,1):
                            print(f"{index}. {item.strip()}")
                    else:
                        print("the list is empty")

io()