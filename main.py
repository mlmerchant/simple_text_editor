#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    """Open a file for editing."""
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def toggle_wrap():
    """Toggle text wrapping."""
    if txt_edit.cget("wrap") == "none":
        txt_edit.config(wrap="word")
    else:
        txt_edit.config(wrap="none")

# Set up the window
window = tk.Tk()
window.title("Simple Text Editor")
window.geometry("800x600") # Set default size of the window

# Create a frame for the text widget and scrollbar
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)

# Set up the text area
txt_edit = tk.Text(frame, wrap="word")
txt_edit.pack(side="left", fill="both", expand=True)

# Add a scrollbar
scrollbar = tk.Scrollbar(frame, command=txt_edit.yview)
scrollbar.pack(side="right", fill="y")
txt_edit.config(yscrollcommand=scrollbar.set)

# Set up the menu
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=window.quit)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Toggle Wrap", command=toggle_wrap)

# Run the application
window.mainloop()
