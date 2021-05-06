#   Challenge 1:Temperature Conversion
#   In this program, you are expected to design and code a program to convert temperature from celsius to fahrenheit
#   and fahrenheit to celsius.

#   IMPORT THE PYTHON GUI TKINTER MODULE AND ASSIGN IT TO tkinter_module
import tkinter as tkinter_module


#   THIS FUNCTION WILL CLOSE THE PROGRAM ON CLICK OF THE exit_btn
def exit_program():
    window.destroy()


#   THIS FUNCTION WILL TOGGLE THE STATE OF THE degrees_entry
def enable_celsius_entry():
    #   IF THE degrees_entry IS DISABLED, THEN ENABLE IT
    if degrees_entry["state"] == tkinter_module.DISABLED:
        degrees_entry.config(state=tkinter_module.NORMAL)
        conversion_value = "Degrees"
    #     IF THE degrees_entry IS ENABLED, THEN DISABLE IT
    else:
        degrees_entry.config(state=tkinter_module.DISABLED)

    #   DISABLE THE fahrenheit_entry
    fahrenheit_entry.config(state=tkinter_module.DISABLED)


#   THIS FUNCTION WILL TOGGLE THE STATE OF THE fahrenheit_entry
def enable_fahrenheit_entry():
    #   IF THE fahrenheit_entry IS DISABLED, THEN ENABLE IT
    if fahrenheit_entry["state"] == tkinter_module.DISABLED:
        fahrenheit_entry.config(state=tkinter_module.NORMAL)
        conversion_value = "Fahrenheit"
    #     IF THE fahrenheit_entry IS ENABLED, THEN DISABLE IT
    else:
        fahrenheit_entry.config(state=tkinter_module.DISABLED)

    #   DISABLE THE degrees_entry
    degrees_entry.config(state=tkinter_module.DISABLED)


#   FUNCTION WILL CONVERT DEGREES CELSIUS TO FAHRENHEIT
def degrees_to_fahrenheit(temperature):
    #   TO CALCULATE THE FAHRENHEIT, YOU:
    #   1.) TAKE THE TEMPERATURE AND MULTIPLY IT BY 1.8
    #   2.) TAKE THAT ANSWER ADD 32
    return round((temperature * 1.8) + 32, 2)


#   FUNCTION WILL CONVERT FAHRENHEIT TO DEGREES CELSIUS
def fahrenheit_to_degrees(temperature):
    #   TO CALCULATE THE DEGREES, YOU:
    #   1.) TAKE THE TEMPERATURE AND SUBTRACT 32
    #   2.) TAKE THAT ANSWER AND DIVIDE IT BY 1.8
    return round((temperature - 32) / 1.8, 2)


def convert_temperature():
    if conversion_value == "Fahrenheit":
        results_entry.config(text=str(fahrenheit_to_degrees(fahrenheit_entry.get())))
    pass
    # if degrees_radio.get() == 1:
    #     result_label.configure(text="now")
        # result_label.config(text=str(degrees_to_fahrenheit(fahrenheit_entry.get())))
    # else:
    #     result_label.configure(text="now")
        # result_label.config(text=str(fahrenheit_to_degrees(degrees_entry.get())))


#   CREATE AN INSTANCE OF THE tkinter_module
window = tkinter_module.Tk()

#   ADD PADDING ON THE ENTIRE window
window.config(padx=20, pady=20)
#   RESIZE THE window
window.geometry("650x500")

#   CREATE THE TITLE OF THE TKINTER WINDOW
window.title("Temperature Converter Web Service Client")

#   CREATE A VARIABLE THAT WILL HOLD THE CONVERSION VALUE
conversion_value = ""

#   CREATE THE celsius_label_frame FOR THE CELSIUS TO FAHRENHEIT CONVERSION
celsius_label_frame = tkinter_module.LabelFrame(window, text="Celsius to Fahrenheit ", width=200, height=100)
celsius_label_frame.place(x=10, y=10)

#   CREATE THE ENTRY BOX INSIDE THE celsius_label_frame
degrees_entry = tkinter_module.Entry(celsius_label_frame, state=tkinter_module.DISABLED)
degrees_entry.place(x=0, y=0)

#   CREATE THE fahrenheit_label_frame FOR THE FAHRENHEIT TO  CELSIUS CONVERSION
fahrenheit_label_frame = tkinter_module.LabelFrame(window, text="Fahrenheit to Celsius ", width=200, height=100)
fahrenheit_label_frame.place(x=300, y=10)

#   CREATE THE ENTRY BOX INSIDE THE fahrenheit_label_frame
fahrenheit_entry = tkinter_module.Entry(fahrenheit_label_frame, state=tkinter_module.DISABLED)
fahrenheit_entry.place(x=0, y=0)

#   CREATE THE BUTTON TO TRIGGER THE celsius_entry STATE CHANGE
celsius_to_fahrenheit_btn = tkinter_module.Button(window, text="Activate - Celsius to Fahrenheit ", command=enable_celsius_entry)
celsius_to_fahrenheit_btn.place(x=10, y=150)

#   CREATE THE BUTTON TO TRIGGER THE fahrenheit_entry STATE CHANGE
fahrenheit_to_celsius_btn = tkinter_module.Button(window, text="Activate - Fahrenheit TO Celsius ", command=enable_fahrenheit_entry)
fahrenheit_to_celsius_btn.place(x=300, y=150)

calculate_conversion_btn = tkinter_module.Button(window, text="Calculate Conversion", command=convert_temperature)
calculate_conversion_btn.place(x=10, y=200)

results_entry = tkinter_module.Entry(window, width=30, bg='#389738')
results_entry.place(x=200, y=200)

clear_btn = tkinter_module.Button(window, text="Clear")
clear_btn.place(x=460, y=200)

exit_btn = tkinter_module.Button(window, text="Exit Program", command=exit_program)
exit_btn.place(x=460, y=250)


window.mainloop()
