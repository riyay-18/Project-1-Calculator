from tkinter import Tk, Label, Entry, StringVar, Button, Radiobutton, Frame, LEFT

# Create the main window
window = Tk()
window.title("ARITHMETIC CALCULATOR")
window.geometry('800x200')

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        result_label.config(text="PLEASE ENTER VALID NUMBERS")
        return

    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result_label.config(text="CANNOT DIVIDE BY ZERO")
            return
        result = num1 / num2
    else:
        result_label.config(text="PLEASE SELECT AN OPERATION.")
        return

    result_label.config(text=f"RESULT: {result}")

# Create labels and entry fields
label1 = Label(window, text="Number 1:")
label1.grid(row=0, column=0, padx=10, pady=5)

entry1 = Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = Label(window, text="Number 2:")
label2.grid(row=1, column=0, padx=10, pady=5)

entry2 = Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Create operation selection
operation_var = StringVar()
operation_var.set("+")  # Default operation

label3 = Label(window, text="OPERATION:")
label3.grid(row=2, column=0, padx=10, pady=5)

operations_frame = Frame(window)
operations_frame.grid(row=2, column=1, padx=10, pady=5)

radio_add = Radiobutton(operations_frame, text="+", variable=operation_var, value="+")
radio_add.pack(side=LEFT)

radio_subtract = Radiobutton(operations_frame, text="-", variable=operation_var, value="-")
radio_subtract.pack(side=LEFT)

radio_multiply = Radiobutton(operations_frame, text="*", variable=operation_var, value="*")
radio_multiply.pack(side=LEFT)

radio_divide = Radiobutton(operations_frame, text="/", variable=operation_var, value="/")
radio_divide.pack(side=LEFT)

# Create calculate button
submit_button = Button(window, text="CALCULATE", command=calculate)
submit_button.grid(row=3, column=0, columnspan=2, pady=5)

# Create result label
result_label = Label(window, text="RESULT: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Run the application
window.mainloop()
