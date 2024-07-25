import tkinter as tk
from tkinter import messagebox

# Function to perform addition
def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        entry_result.delete(0, tk.END)  # Clear previous result
        entry_result.insert(0, result)  # Display new result
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform subtraction
def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        entry_result.delete(0, tk.END)  # Clear previous result
        entry_result.insert(0, result)  # Display new result
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform multiplication
def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        entry_result.delete(0, tk.END)  # Clear previous result
        entry_result.insert(0, result)  # Display new result
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform division
def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed")
        else:
            result = num1 / num2
            entry_result.delete(0, tk.END)  # Clear previous result
            entry_result.insert(0, result)  # Display new result
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
label_num1 = tk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root, width=15)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_operation = tk.Label(root, text="Operation:")
label_operation.grid(row=0, column=2, padx=10, pady=10)

# Dropdown for operation selection
operations = ['+', '-', '*', '/']
variable_operation = tk.StringVar(root)
variable_operation.set('+')  # Default operation
dropdown_operation = tk.OptionMenu(root, variable_operation, *operations)
dropdown_operation.grid(row=0, column=3, padx=10, pady=10)

label_num2 = tk.Label(root, text="Number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=15)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

button_calculate = tk.Button(root, text="Calculate", width=15, command=lambda: calculate(variable_operation.get()))
button_calculate.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=2, column=0, padx=10, pady=10)

entry_result = tk.Entry(root, width=15)
entry_result.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

# Function to perform calculation based on operation selected
def calculate(operation):
    if operation == '+':
        add()
    elif operation == '-':
        subtract()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()

# Run the main loop
root.mainloop()