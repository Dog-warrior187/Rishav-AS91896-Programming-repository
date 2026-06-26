import tkinter as tk
import functions

#TO DO LIST PROGRAM VERSION 3

root = tk.Tk()
root.title("To-Do-List")
root.geometry("370x415")
functions.create_tooltip_window(root)  # Creates the tooltip system


# Load and resize all png icons for the buttons
plus_img = tk.PhotoImage(file="plus.png").subsample(15, 15)
x_img = tk.PhotoImage(file="X.png").subsample(14, 14)
open_img = tk.PhotoImage(file="open.png").subsample(50, 50)
check_img = tk.PhotoImage(file="check.png").subsample(50, 50)
back_img = tk.PhotoImage(file="back.png").subsample(50, 50)
up_img = tk.PhotoImage(file="up.png").subsample(15, 15)
down_img = tk.PhotoImage(file="down.png").subsample(15, 15)


#Switches between frames
def show_frame(frame):
    frame.tkraise()


#MAIN MENU AND LIST FRAME
main_menu_frame = tk.Frame(root, width=370, height=350, bg="#B8F5E5")
list_frame = tk.Frame(root, width=370, height=350, bg="#B8F5E5")

main_menu_frame.grid(row=0, column=0, sticky="nsew")
list_frame.grid(row=0, column=0, sticky="nsew")

#Button frames for grouping buttons
menu_button_frame = tk.Frame(main_menu_frame, bg="#128C8C")
menu_button_frame.grid(row=1, column=0, sticky="w")

list_button_frame = tk.Frame(list_frame, bg="#128C8C")
list_button_frame.grid(row=1, column=0, sticky="w")


#MAIN MENU
title = tk.Label(main_menu_frame, text="Your Lists", font=("Arial", 20), bg="#B8F5E5")
title.grid(row=0, column=1, pady=0)

subheading = tk.Label(main_menu_frame, text="hover cursor over buttons for instuctions", font=("Arial", 10))
subheading.grid(row=5, column=1, pady=0)

#Listbox showing all lists
list_listbox = tk.Listbox(main_menu_frame, width=40, height=15)
list_listbox.grid(row=1, column=1, padx=0)
functions.load_data()
functions.refresh_lists(list_listbox)

#Add list button
add_list_button = tk.Button(
    menu_button_frame,
    image=plus_img,
    text="Add List",
    bg="white",
    compound="left",
    command=lambda: functions.add_list(root, list_listbox)
)
add_list_button.grid(row=1, column=0, pady=10, padx=5)
functions.add_tooltip(add_list_button, "Create a new list")

#Delete list button
delete_list_button = tk.Button(
    menu_button_frame,
    image=x_img,
    text="Delete List",
    bg="white",
    compound="left",
    command=lambda: functions.delete_list(list_listbox)
)
delete_list_button.grid(row=3, column=0, pady=10, padx=5)
functions.add_tooltip(delete_list_button, "Select a list, then click to delete")

#Open list button
open_list_button = tk.Button(
    menu_button_frame,
    image=open_img,
    text="Open List",
    bg="white",
    compound="left",
    command=lambda: functions.open_list(
        list_listbox, show_frame, list_frame, item_listbox, list_title
    )
)
open_list_button.grid(row=2, column=0, pady=10, padx=5)
functions.add_tooltip(open_list_button, "Select a list, then click to open")


#LIST SCREEN
list_title = tk.Label(list_frame, text="List Items", font=("Arial", 20), bg="#B8F5E5")
list_title.grid(row=0, column=1, pady=0)

subheading = tk.Label(list_frame, text="hover cursor over buttons for instuctions", font=("Arial", 10))
subheading.grid(row=4, column=1, pady=0)

#Listbox showing items inside the selected list
item_listbox = tk.Listbox(list_frame, width=40, height=15)
item_listbox.grid(row=1, column=1, padx=0)

#Add item button
add_item_button = tk.Button(
    list_button_frame,
    image=plus_img,
    text="Add item",
    bg="white",
    compound="left",
    command=lambda: functions.add_item(root, item_listbox)
)
add_item_button.grid(row=3, column=0, pady=10, padx=5)
functions.add_tooltip(add_item_button, "Click to add an item to the list")

#Delete item button
delete_item_button = tk.Button(
    list_button_frame,
    image=x_img,
    text="Delete item",
    bg="white",
    compound="left",
    command=lambda: functions.delete_item(item_listbox)
)
delete_item_button.grid(row=5, column=0, pady=10, padx=5)
functions.add_tooltip(delete_item_button, "Select an item then click to delete")

#Check item button
check_item_button = tk.Button(
    list_button_frame,
    text="Check item",
    bg="white",
    compound="left",
    image=check_img,
    command=lambda: functions.check_item(item_listbox)
)
check_item_button.grid(row=4, column=0, pady=10, padx=5)
functions.add_tooltip(check_item_button, "Select an item, then click to checkmark it")

#Back button
back_button = tk.Button(
    list_button_frame,
    text=" Go Back",
    bg="white",
    compound="left",
    image=back_img,
    command=lambda: show_frame(main_menu_frame)
)
back_button.grid(row=6, column=0, pady=20)
functions.add_tooltip(back_button, "Go back to previous menu")

#move item up button
move_up_button = tk.Button(
    list_button_frame,
    text="Move Up",
    bg="white",
     compound="left",
    image=up_img,
    command=lambda: functions.move_item_up(item_listbox)
)
move_up_button.grid(row=1, column=0, pady=5)
functions.add_tooltip(move_up_button, "Move selected item up in the list")

#move item down button
move_down_button = tk.Button(
    list_button_frame,
    text="Move Down",
    bg="white",
     compound="left",
    image=down_img,
    command=lambda: functions.move_item_down(item_listbox)
)
move_down_button.grid(row=2, column=0, pady=5)
functions.add_tooltip(move_down_button, "Move selected item down in the list")


#Show the main menu first
show_frame(main_menu_frame)

root.mainloop()
