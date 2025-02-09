from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()
window.title("Bin2Dec")
window.config(padx=20, pady=20)

# Function to validate input (only allow 0 and 1)
def validate_input(char):
    return char in "01"

# Binary to Decimal Conversion Logic
def calc():
    number = bin_input.get()
    if not number:  # Check if input is empty
        messagebox.showwarning(title="Error", message="Input cannot be empty!")
        return
    
    x = len(number)  # x = exponent or power
    result = 0

    for n in number:
        x -= 1
        n = int(n)
        if n == 0 or n == 1:
            result += n * 2 ** x
        else:
            dec_result.config(text=0)  # Reset result
            messagebox.showwarning(title="Error", message="Input is not a binary number.\nInput must be 0s and 1s.")
            return
    
    dec_result.config(text=result)

# Reset the input and output fields
def reset():
    bin_input.delete(0, END)
    dec_result.config(text=0)

# GUI Components
header = Label(text="Binary To Decimal Converter.")
header.grid(row=0, column=1, pady=20)

bin_label = Label(text="Enter a binary number: ")
bin_label.grid(row=1, column=0)

dec_label = Label(text="Decimal number is: ")
dec_label.grid(row=3, column=0)

# Input field with validation
validate_cmd = window.register(validate_input)
bin_input = Entry(validate="key", validatecommand=(validate_cmd, '%S'))
bin_input.grid(row=1, column=1)

# Output result
dec_result = Label(text=0)
dec_result.grid(row=3, column=1)

# Buttons
calc_button = Button(text="Calculate", command=calc)
calc_button.grid(row=2, column=1, pady=10)

reset_button = Button(text="Clear", command=reset)
reset_button.grid(row=4, column=1, pady=10)

# Run the main event loop
window.mainloop()
