import math
import tkinter as tk

class ResponsiveCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Básica")

        # Variable para almacenar la entrada del usuario
        self.expression = ""

        # Configuración de la entrada
        self.entry = tk.Entry(self.root, font=("Arial", 18), justify="right", bd=5)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Botones
        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('⇍', 1, 3),
            ('⅟x', 2, 0), ('x²', 2, 1), ('√x', 2, 2), ('÷', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('×', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('C', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 18),
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Configuración responsiva
        for i in range(7):  # 6 filas de botones + 1 fila de entrada
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 columnas de botones
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if self.expression == "Error":
            self.expression = ""

        if char == "C":
            self.expression = ""
        elif char == "⇍":
            self.expression = self.expression[:-1]
        elif char == "sin":
            try:
                self.expression = str(math.sin(math.radians(float(self.expression))))
            except:
                self.expression = "Error"
        elif char == "cos":
            try:
                self.expression = str(math.cos(math.radians(float(self.expression))))
            except:
                self.expression = "Error"
        elif char == "tan":
            try:
                self.expression = str(math.tan(math.radians(float(self.expression))))
            except:
                self.expression = "Error"
        elif char == "⅟x":
            try:
                self.expression = str(1 / float(self.expression))
            except:
                self.expression = "Error"
        elif char == "x²":
            try:
                self.expression = str(float(self.expression) ** 2)
            except:
                self.expression = "Error"
        elif char == "√x":
            try:
                self.expression = str(math.sqrt(float(self.expression)))
            except:
                self.expression = "Error"
        elif char == "=":
            try:
                self.expression = str(eval(self.expression.replace('÷', '/').replace('×', '*')))
            except Exception as e:
                self.expression = "Error"
        else:
            if char not in ["sin", "cos", "tan", "⅟x", "x²", "√x", "⇍", "="]:
                self.expression += char
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ResponsiveCalculator(root)
    root.mainloop()
