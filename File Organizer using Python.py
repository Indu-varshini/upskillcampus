import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".png", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Others": []
    }

    for folder in file_types:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, folder, file))
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, os.path.join(folder_path, "Others", file))

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        status_label.config(text=f"Selected Folder:\n{folder}")
        organize_files(folder)
        messagebox.showinfo("Success", "Files organized successfully!")

# ---------- GUI DESIGN ----------
root = tk.Tk()
root.title("File Organizer Application")
root.geometry("420x300")
root.configure(bg="#f2f2f2")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="📁 File Organizer",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2",
    fg="#333333"
)
title.pack(pady=15)

# Description
desc = tk.Label(
    root,
    text="This application organizes files\ninto Images, Documents, Music, Videos, etc.",
    font=("Arial", 11),
    bg="#f2f2f2",
    fg="#555555"
)
desc.pack(pady=5)

# Button
select_btn = tk.Button(
    root,
    text="Choose Folder",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=20,
    pady=8,
    command=select_folder
)
select_btn.pack(pady=20)

# Status label
status_label = tk.Label(
    root,
    text="No folder selected",
    font=("Arial", 10),
    bg="#f2f2f2",
    fg="#000000",
    wraplength=380,
    justify="center"
)
status_label.pack(pady=10)

root.mainloop()

