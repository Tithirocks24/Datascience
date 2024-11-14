import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""

        # Entry widget for displaying calculations
        self.display = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Create buttons and place them on the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, 
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:  # Move to the next row after 4 buttons
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                self.expression = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, self.expression)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += button
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
