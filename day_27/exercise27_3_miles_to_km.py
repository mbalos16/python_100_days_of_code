# Exercise27.2 Miles to km Converter


import tkinter

window = tkinter.Tk()
window.title("BMM • Mile to KM Converter")
window.minsize(width=200, height=50)
window.config(padx=20, pady=20)


def calculate_km():
    to_calculate = ask_miles.get()
    km_result = round((float(to_calculate) * 1.609), 2)
    result.config(text=km_result)


# Ask user for the miles that wants to convert
ask_miles = tkinter.Entry(width=7)
ask_miles.insert(tkinter.END, string="0")
print(ask_miles.get())
ask_miles.grid(column=1, row=0)


# Miles
miles = tkinter.Label(text="Miles", font=("Arial", 14))
miles.grid(column=2, row=0)


# Is equal to
equal = tkinter.Label(text="is equal to", font=("Arial", 14))
equal.grid(column=0, row=1)


# result
result = tkinter.Label(text="0", font=("Arial", 14))
result.grid(column=1, row=1)

# km
km = tkinter.Label(text="Km", font=("Arial", 14))
km.grid(column=2, row=1)


# button
calculate = tkinter.Button(text="Calculate", font=("Arial", 14), command=calculate_km)
calculate.grid(column=1, row=2)


window.mainloop()
