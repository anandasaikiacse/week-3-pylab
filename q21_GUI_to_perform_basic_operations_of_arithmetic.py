import tkinter as tk

# Function to update the input field
def click_button(value):
    entry_field.insert(tk.END, value)

# Function to clear the input field
def clear_field():
    entry_field.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_field.get())  # Evaluates the expression
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator by Ananda Saikia")
root.geometry("370x410")

# Create input field
entry_field = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry_field.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "=":
            btn = tk.Button(root, text=text, font=("Arial", 20), command=calculate, width=5, height=2)
        elif text == "C":
            btn = tk.Button(root, text=text, font=("Arial", 20), command=clear_field, width=5, height=2)
        else:
            btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda val=text: click_button(val), width=5, height=2)
        
        btn.grid(row=i+1, column=j)

# Run the GUI event loop
root.mainloop()