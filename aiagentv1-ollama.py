import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import simpledialog
import openai
import threading
from openai import OpenAI
import os
import subprocess
from tkinter import ttk

from openai import OpenAI  # Ensure openai package is installed
client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

#save and run the code locally using python only
def save_and_run_code(file_name, code):
    try:
        code = code.strip()
        if code.startswith("```python"):
            code = code[len("```python"):].strip()
        if code.endswith("```"):
            code = code[:-len("```")].strip()

        with open(file_name, 'w') as file:
            file.write(code)

        result = subprocess.run(
            ['python', file_name],
            text=True,
            capture_output=True
        )

        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error:\n{result.stderr}"

    except Exception as e:
        return f"An exception occurred: {e}"

#Local host mode, using Ollama
def send_request():
    user_input = input_text.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    def request():
        try:
            completion = client.chat.completions.create(
                model="llama3.1:latest",
                messages=[
                    {"role": "system", "content": "you are advance python code assistant, generate best quality code.  Output raw code only:"},
                    {"role": "user", "content":  "you are advance python code assistant, generate best quality code.  Output raw code only: "+user_input}
                ],
                #max_tokens=150
            )
            ai_response = completion.choices[0].message.content.strip()
            save_and_run_code("C:\\Users\\Thomas_Yiu\\Downloads\\temp.py", ai_response)
            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, ai_response)
            output_text.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            send_button.config(state=tk.NORMAL)

    #send_button.config(state=tk.DISABLED)
    threading.Thread(target=request).start()

# Menu functionalities
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                input_text.delete("1.0", tk.END)
                input_text.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".py",
        filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(input_text.get("1.0", tk.END))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def change_font():
    # Create a new top-level window
    top = tk.Toplevel()
    top.title("Change Font")

    # Get the list of all system font families
    font_families = list(font.families())
    font_families.sort()  # Sort alphabetically if you like

    # Label and Combobox for Font Family
    tk.Label(top, text="Font Family:").pack(pady=(10,0))
    font_combo = ttk.Combobox(top, values=font_families, state='readonly')
    font_combo.pack(pady=5)
    # Optionally set a default selection (e.g., first in list)
    font_combo.current(0)

    # Label and Combobox for Font Sizes
    tk.Label(top, text="Font Size:").pack(pady=(10,0))
    sizes = [str(size) for size in range(6, 50)]  # Customize range as needed
    size_combo = ttk.Combobox(top, values=sizes, state='readonly')
    size_combo.pack(pady=5)
    # Optionally set a default size
    default_size_index = sizes.index('12')
    size_combo.current(default_size_index)

    # Function to apply selected font family and size
    def apply_changes():
        chosen_font = font_combo.get()
        chosen_size = size_combo.get()

        if chosen_font and chosen_size:
            # Set font on your text widgets
            input_text.config(font=(chosen_font, int(chosen_size)))
            output_text.config(font=(chosen_font, int(chosen_size)))

        top.destroy()

    # Button to confirm the user’s selection
    apply_button = tk.Button(top, text="Apply", command=apply_changes)
    apply_button.pack(pady=10)

    # Optional Cancel button
    cancel_button = tk.Button(top, text="Cancel", command=top.destroy)
    cancel_button.pack(pady=(0, 10))

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        input_text.config(fg=color)
        output_text.config(fg=color)

def change_bg_color():
    color = colorchooser.askcolor()[1]
    if color:
        input_text.config(bg=color)
        output_text.config(bg=color)

# Create the main window
root = tk.Tk()
root.title("Aurora AI Agent")
root.geometry("800x600")  # Improved: Increased window size for better usability

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu for font and color settings
format_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Change Font", command=change_font)
format_menu.add_command(label="Change Text Color", command=change_text_color)
format_menu.add_command(label="Change Background Color", command=change_bg_color)

# Input label and text box
input_label = tk.Label(root, text="Input:")
input_label.pack(pady=(10, 0))
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=15)
input_text.pack(padx=10, pady=(0, 10))

# Send button
send_button = tk.Button(root, text="Send", command=send_request)
send_button.pack(pady=5)

# Output label and text box
output_label = tk.Label(root, text="Output:")
output_label.pack(pady=(10, 0))
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=15, state=tk.DISABLED)
output_text.pack(padx=10, pady=(0, 10))

# Run the application
root.mainloop()