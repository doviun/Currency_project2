import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\doviu\\PycharmProjects\\Currency_converter_project\\results.txt", title="Select Text File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
                text_widget.delete(1.0, tk.END)  # Clear the text widget
                text_widget.insert(tk.END, file_contents)
        except Exception as e:
            # Handle any exceptions that may occur while reading the file
            print(f"Error opening the file: {e}")

root = tk.Tk()
root.title("Open Text File")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()

root.mainloop()


