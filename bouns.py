import json

def read_todo():
    try:
        with open("To-Do.json","r",encoding="UTF-8") as file:
            todo = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        todo = []
    return todo

def save_todo(todo):
    with open("To-Do.json","w",encoding="UTF-8") as file:
        json.dump(todo,file)


def io():
    while True:
        choice = input("do you want to add a new To-Do item? answer by [y/n/mark/search/exit]")

        if choice == "exit":
            print("thank you for using the To-Do program, come back again soon")
            break
        elif choice == "y":
            title = input("enter your new to-do title :").lower()
            date = input("enter the date and time (YYYY-MM-DD HH:MM:SS)")

            new_task = {
                "title" : title,
                "date_time" : date,
                "done" : False
            }

            todo = read_todo()
            todo.append(new_task)
            save_todo(todo)
            print("Added successfully")
        elif choice == "n":
            view_To_do = input("do you want to list your To-Do items ? answer by [y/n]")

            if view_To_do == "y":
                todo = read_todo()
                if todo:
                    print("Your To-Do List:")
                    for index , item in enumerate(todo,1):
                        if item["done"]:
                            staus = "done"
                        else:
                            staus = "not done"

                        print(f"{index}. {item['title']} - {item['date_time']} - {staus}")
                else:
                    print("the list is empty")
        elif choice == "mark":
            todo = read_todo()
            title_mark = input("enter the title of the task you want to mark: ")
            for task in todo:
                if task["title"].lower() == title_mark.lower():
                    task["done"] = True
                    save_todo(todo)
                    print(f"task '{title_mark}' marked as done")
                    break
            else:
                print("task not found")
        elif choice == "search":
            search_title = input("enter the title to search for: ")
            todo = read_todo()
            found = False
            for index, item in enumerate(todo,1):
                if search_title.lower() in item["title"].lower():
                    if item["done"]:
                        staus = "done"
                    else:
                        staus = "not done"
                        
                    print(f"{index}. {item['title']} - {item['date_time']} - {staus}")
                    found = True
            if not found:
                print(f"No tasks found with the title containing '{search_title}'.")

io()