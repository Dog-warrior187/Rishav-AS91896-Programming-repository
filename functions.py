import tkinter as tk

lists = {}#stores all lists
current_list = None#stores which list is open


#REFRESH FUNCTIONS

def refresh_lists(list_listbox):
    list_listbox.delete(0, tk.END)
    for name in lists:
        list_listbox.insert(tk.END, name)


def refresh_items(item_listbox):
    item_listbox.delete(0, tk.END)
    for item in lists[current_list]:
        item_listbox.insert(tk.END, item)


#LIST FUNCTIONS 

def add_list(root, list_listbox):
    popup = tk.Toplevel(root)
    popup.title("Add List")

    tk.Label(popup, text="List name:").pack(pady=5)#User Enters the name of the list to create
    entry = tk.Entry(popup)
    entry.pack(pady=5)

    def save():
        name = entry.get()
        if name != "":
            lists[name] = []
            refresh_lists(list_listbox)#refreshes the lists to update
            popup.destroy()

    tk.Button(popup, text="Add", command=save).pack(pady=10)#adds the list to the menu


def delete_list(list_listbox):
    try:
        index = list_listbox.curselection()[0]#Delete the list the user selected with curser
        name = list_listbox.get(index)
        del lists[name]
        refresh_lists(list_listbox)
    except:
        pass


def open_list(list_listbox, show_frame, list_frame, item_listbox, title_label):
    global current_list

    try:
        index = list_listbox.curselection()[0]
        name = list_listbox.get(index)
    except:
        return

    current_list = name
    title_label.config(text=f"Items in: {name}")
    refresh_items(item_listbox)
    show_frame(list_frame)


#ITEM FUNCTIONS

def add_item(root, item_listbox):
    popup = tk.Toplevel(root)
    popup.title("Add Item")

    tk.Label(popup, text="Item:").pack(pady=5)
    entry = tk.Entry(popup)
    entry.pack(pady=5)

    def save():
        item = entry.get()
        if item != "":
            lists[current_list].append(item)
            refresh_items(item_listbox)
            popup.destroy()

    tk.Button(popup, text="Save", command=save).pack(pady=10)


def delete_item(item_listbox):
    try:
        index = item_listbox.curselection()[0]
        item = item_listbox.get(index)
        lists[current_list].remove(item)
        refresh_items(item_listbox)
    except:
        pass


def check_item(item_listbox):
    try:
        index = item_listbox.curselection()[0]
        item = item_listbox.get(index)

        if not item.startswith("✓ "):
            lists[current_list][index] = "✓ " + item
            refresh_items(item_listbox)
    except:
        pass
