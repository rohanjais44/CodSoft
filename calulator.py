import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("500x600")  # Increase the window size
        
        self.result_var = tk.StringVar()
        self.memory = [None, None]  # To store the last two calculations
        
        self.create_widgets()

    def create_widgets(self):
        # Display
        display = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, relief='ridge', justify='right', bg="#f0f0f0", fg="#333")
        display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Button Layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3),
            ('log', 6, 0), ('ln', 6, 1), ('^', 6, 2), ('(', 6, 3),
            (')', 7, 0), ('C', 7, 1), ('M1', 7, 2), ('M2', 7, 3),
            ('←', 8, 0, 2),  # Backspace button spans two columns
        ]

        button_config = {
            "font": ('Arial', 16),
            "relief": 'flat',
            "bg": "#333",
            "fg": "white",
            "activebackground": "#555",
            "activeforeground": "white",
            "bd": 0,
            "highlightthickness": 0,
            "padx": 15,
            "pady": 15,
        }

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1  # Default colspan to 1 if not specified

            b = tk.Button(self, text=text, **button_config)
            if text == "=":
                b.config(command=self.evaluate, bg="#f57c00", fg="white")
            elif text == "C":
                b.config(command=self.clear, bg="#e53935", fg="white")
            elif text == "M1":
                b.config(command=lambda: self.recall_memory(0))
            elif text == "M2":
                b.config(command=lambda: self.recall_memory(1))
            elif text == "←":
                b.config(command=self.backspace, bg="#ffa000", fg="white")
            else:
                b.config(command=lambda t=text: self.button_click(t))
            b.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        # Adjust row and column weights
        for i in range(9):  # Adjust for the extra row
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def button_click(self, text):
        current_text = self.result_var.get()

        # Mapping the button text to its corresponding math function
        if text in {'sin', 'cos', 'tan', 'log', 'ln', '√', '^', 'pi', 'e'}:
            if text == '√':
                text = 'math.sqrt('
            elif text == '^':
                text = '**'
            elif text == 'pi':
                text = str(math.pi)
            elif text == 'e':
                text = str(math.e)
            elif text == 'log':
                text = 'math.log10('
            elif text == 'ln':
                text = 'math.log('
            elif text == 'sin':
                text = 'math.sin(math.radians('
            elif text == 'cos':
                text = 'math.cos(math.radians('
            elif text == 'tan':
                text = 'math.tan(math.radians('

            # Automatically add a closing parenthesis if needed
            if text.endswith('('):
                self.result_var.set(current_text + text)
            else:
                self.result_var.set(current_text + text + ')')
        else:
            self.result_var.set(current_text + text)

    def backspace(self):
        current_text = self.result_var.get()
        self.result_var.set(current_text[:-1])  # Remove the last character

    def evaluate(self):
        try:
            expr = self.result_var.get()
            # Safely evaluate the expression
            result = eval(expr, {"math": math, "__builtins__": {}})
            self.result_var.set(result)
            # Save result to memory
            self.memory.append(result)
            if len(self.memory) > 2:
                self.memory.pop(0)
        except Exception:
            self.result_var.set("Error")

    def clear(self):
        self.result_var.set("")

    def recall_memory(self, index):
        if 0 <= index < len(self.memory) and self.memory[index] is not None:
            self.result_var.set(self.memory[index])

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
