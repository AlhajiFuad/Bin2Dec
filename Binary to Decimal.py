from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Bin2Dec")
window.config(padx=20, pady=20)


def calc():
    number = bin_input.get()
    x = len(number)  # x = exponent or power.
    result = 0

    for n in number:
        x -= 1
        n = int(n)
        if n == 0 or n == 1:
            result += n * 2 ** x
        else:
            messagebox.showwarning(title="Error", message="Input is not a binary number.\nInput must be 0s and 1s.")

    dec_result.config(text=result)


header = Label(text="Binary To Decimal Converter.")
header.grid(row=0, column=1)
header.config(pady=20)

bin_label = Label(text="Enter a binary number: ")
bin_label.grid(row=1, column=0)

dec_label = Label(text="Decimal number is: ")
dec_label.grid(row=3, column=0)

bin_input = Entry()
bin_input.grid(row=1, column=1)

dec_result = Label(text=0)
dec_result.grid(row=3, column=1)

calc_button = Button(text="Calculate", command=calc)
calc_button.grid(row=2, column=2)

window.mainloop()
