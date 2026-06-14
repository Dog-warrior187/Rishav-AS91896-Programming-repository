import tkinter as tk
import functions

root = tk.Tk()
root.title("To-Do-List")
root.geometry("230x400")


#Fram switching
def show_frame(frame):
    frame.tkraise()


#MAIN MENU AND LIST FRAME
main_menu_frame = tk.Frame(root)
list_frame = tk.Frame(root)

main_menu_frame.grid(row=0, column=0, sticky="nsew")
list_frame.grid(row=0, column=0, sticky="nsew")


#MAIN MENU
title = tk.Label(main_menu_frame, text="Your Lists", font=("Arial", 16))
title.grid(row=0, column=0, pady=20)

list_listbox = tk.Listbox(main_menu_frame, width=30)
list_listbox.grid(row=1, column=0, padx=20)
#add a list
add_list_button = tk.Button(
    main_menu_frame,
    text="Add List",
    command=lambda: functions.add_list(root, list_listbox)
)
add_list_button.grid(row=2, column=0, pady=10)
#delete a list
delete_list_button = tk.Button(
    main_menu_frame,
    text="Delete List",
    command=lambda: functions.delete_list(list_listbox)
)
delete_list_button.grid(row=3, column=0, pady=10)


#open selected list
open_list_button = tk.Button(
    main_menu_frame,
    text="Open List",
    command=lambda: functions.open_list(
        list_listbox, show_frame, list_frame, item_listbox, list_title
    )
)
open_list_button.grid(row=4, column=0, pady=10)


#LIST SCREEN
list_title = tk.Label(list_frame, text="List Items", font=("Arial", 16))
list_title.grid(row=0, column=0, pady=20)

item_listbox = tk.Listbox(list_frame, width=30)
item_listbox.grid(row=1, column=0, padx=20)

add_item_button = tk.Button(
    list_frame,
    text="Add Item",
    command=lambda: functions.add_item(root, item_listbox)
)
add_item_button.grid(row=2, column=0, pady=5)

#Deleting an Item from the list
delete_item_button = tk.Button(
    list_frame,
    text="Delete Item",
    command=lambda: functions.delete_item(item_listbox)
)
delete_item_button.grid(row=3, column=0, pady=5)

#Checking off an Item
check_item_button = tk.Button(
    list_frame,
    text="Checkmark Item",
    command=lambda: functions.check_item(item_listbox)
)
check_item_button.grid(row=4, column=0, pady=5)

#go back to the main menu
back_button = tk.Button(
    list_frame,
    text="Back",
    command=lambda: show_frame(main_menu_frame)
)
back_button.grid(row=5, column=0, pady=20)


#Show the main menu frame
show_frame(main_menu_frame)

root.mainloop()
