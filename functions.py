import tkinter as tk

#TO DO LIST FUNCTIONS VERSION 2

lists = {}#stores all lists
current_list = None#stores which list is open


#REFRESH FUNCTIONS
def refresh_lists(list_listbox):
    list_listbox.delete(0, tk.END)#clear listbox
    for name in lists:
        list_listbox.insert(tk.END, name)#insert each list name


def refresh_items(item_listbox):
    item_listbox.delete(0, tk.END)#clear listbox
    for item in lists[current_list]:
        item_listbox.insert(tk.END, item)#insert each item


#LIST FUNCTIONS
def add_list(root, list_listbox):
    popup = tk.Toplevel(root)
    popup.title("Add List")

    tk.Label(popup, text="List name:").pack(pady=5)#user enters list name
    entry = tk.Entry(popup)
    entry.focus_set()
    entry.pack(pady=5)

    def save():
        name = entry.get()
        if name != "":
            lists[name] = []#create empty list
            refresh_lists(list_listbox)#update UI
            popup.destroy()#close popup

    tk.Button(popup, text="Add", command=save).pack(pady=10)#add list button


def delete_list(list_listbox):
    try:
        index = list_listbox.curselection()[0]#get selected list
        name = list_listbox.get(index)
        del lists[name]#delete list
        refresh_lists(list_listbox)#update UI
    except:
        pass#ignore if nothing selected


def open_list(list_listbox, show_frame, list_frame, item_listbox, title_label):
    global current_list

    try:
        index = list_listbox.curselection()[0]#get selected list
        name = list_listbox.get(index)
    except:
        return#do nothing if nothing selected

    current_list = name#set active list
    title_label.config(text=f"Items in: {name}")#update title
    refresh_items(item_listbox)#load items
    show_frame(list_frame)#switch screen


#ITEM FUNCTIONS
def add_item(root, item_listbox):
    popup = tk.Toplevel(root)
    popup.title("Add Item")

    tk.Label(popup, text="Item:").pack(pady=5)#user enters item
    entry = tk.Entry(popup)
    entry.focus_set()
    entry.pack(pady=5)

    def save():
        item = entry.get()
        if item != "":
            lists[current_list].append(item)#add item
            refresh_items(item_listbox)#update UI
            popup.destroy()

    tk.Button(popup, text="Save", command=save).pack(pady=10)


def delete_item(item_listbox):
    try:
        index = item_listbox.curselection()[0]#get selected item
        item = item_listbox.get(index)
        lists[current_list].remove(item)#delete item
        refresh_items(item_listbox)#update UI
    except:
        pass#ignore if nothing selected


def check_item(item_listbox):
    try:
        index = item_listbox.curselection()[0]#get selected item
        item = item_listbox.get(index)

        if not item.startswith("✓ "):#only add checkmark once
            lists[current_list][index] = "✓ " + item
            refresh_items(item_listbox)#update UI
    except:
        pass


#TOOLTIP SYSTEM
tooltip = None#tooltip window
tooltip_label = None#tooltip text label
tooltip_timer = None#timer for delayed tooltip


def create_tooltip_window(root):
    global tooltip, tooltip_label
    tooltip = tk.Toplevel(root)#create tooltip window
    tooltip.withdraw()#hide by default
    tooltip.overrideredirect(True)#remove window border

    tooltip_label = tk.Label(
        tooltip,
        text="",
        background="#ffffe0",
        relief="solid",
        borderwidth=1,
        font=("Segoe UI", 10)
    )
    tooltip_label.pack(ipadx=5, ipady=3)


def show_tooltip_now(event, text):
    x = event.widget.winfo_rootx() + 20#tooltip X position
    y = event.widget.winfo_rooty() + 40#tooltip Y position
    tooltip.geometry(f"+{x}+{y}")
    tooltip_label.config(text=text)#set tooltip text
    tooltip.deiconify()#show tooltip


def hide_tooltip(event):
    global tooltip_timer
    tooltip.withdraw()#hide tooltip

    if tooltip_timer is not None:
        event.widget.after_cancel(tooltip_timer)
        tooltip_timer = None


def add_tooltip(widget, text, delay=1000):
    def schedule_tooltip(event):
        global tooltip_timer
        tooltip_timer = widget.after(delay, lambda: show_tooltip_now(event, text))

    widget.bind("<Enter>", schedule_tooltip)#start timer on hover
    widget.bind("<Leave>", hide_tooltip)#hide tooltip on exit
