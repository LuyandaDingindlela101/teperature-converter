#   Challenge 1:Temperature Conversion
#   In this program, you are expected to design and code a program to convert temperature from celsius to fahrenheit
#   and fahrenheit to celsius.

#   IMPORT THE PYTHON GUI TKINTER MODULE AND ASSIGN IT TO tkinter_module
import tkinter as tkinter_module
from tkinter import messagebox

window = tkinter_module.Tk()

#   ADD PADDING ON THE ENTIRE window
window.config(padx=20, pady=20)
#   RESIZE THE window
window.geometry("650x500")

#   CREATE THE TITLE OF THE TKINTER WINDOW
window.title("Temperature Converter Web Service Client")

#   CREATE A VARIABLE THAT WILL HOLD THE CONVERSION VALUE
conversion_value = ""


#   THIS FUNCTION WILL CLOSE THE PROGRAM ON CLICK OF THE exit_btn
def exit_program():
    message_box = tkinter_module.messagebox.askquestion('Exit Application', 'Are you sure you want to exit', icon='warning')
    if message_box == 'yes':
        window.destroy()
    else:
        #   ELSE, JUST GO BACK TO THE APPLICATION SCREEN
        pass


#   THIS FUNCTION WILL TOGGLE THE STATE OF THE celsius_entry
def toggle_celsius_entry():
    #   IF THE celsius_entry IS DISABLED, THEN ENABLE IT
    if celsius_entry["state"] == tkinter_module.DISABLED:
        celsius_entry.config(state=tkinter_module.NORMAL)

        #   WE HAVE TO GET ACCESS TO THE conversion_value BY USING THE global KEYWORD
        global conversion_value
        #   NOW, WE ASSIGN "Celsius" TO conversion_value
        conversion_value = "Celsius"

    #     IF THE celsius_entry IS ENABLED, THEN DISABLE IT
    else:
        celsius_entry.config(state=tkinter_module.DISABLED)

    #   DISABLE THE fahrenheit_entry
    fahrenheit_entry.config(state=tkinter_module.DISABLED)


#   THIS FUNCTION WILL TOGGLE THE STATE OF THE fahrenheit_entry
def toggle_fahrenheit_entry():
    #   IF THE fahrenheit_entry IS DISABLED, THEN ENABLE IT
    if fahrenheit_entry["state"] == tkinter_module.DISABLED:
        fahrenheit_entry.config(state=tkinter_module.NORMAL)
        #   WE HAVE TO GET ACCESS TO THE conversion_value BY USING THE global KEYWORD
        global conversion_value
        #   NOW, WE ASSIGN "Fahrenheit" TO conversion_value
        conversion_value = "Fahrenheit"

        #     IF THE fahrenheit_entry IS ENABLED, THEN DISABLE IT
    else:
        fahrenheit_entry.config(state=tkinter_module.DISABLED)

    #   DISABLE THE celsius_entry
    celsius_entry.config(state=tkinter_module.DISABLED)


#   FUNCTION WILL CONVERT CELSIUS TO FAHRENHEIT
def celsius_to_fahrenheit(temperature):
    #   TO CALCULATE THE FAHRENHEIT, YOU:
    #   1.) TAKE THE TEMPERATURE AND MULTIPLY IT BY 1.8
    #   2.) TAKE THAT ANSWER ADD 32
    converted_temperature = (temperature * 1.8) + 32
    results_entry.insert(0, converted_temperature)


#   FUNCTION WILL CONVERT FAHRENHEIT TO CELSIUS
def fahrenheit_to_celsius(temperature):
    #   TO CALCULATE THE CELSIUS, YOU:
    #   1.) TAKE THE TEMPERATURE AND SUBTRACT 32
    #   2.) TAKE THAT ANSWER AND DIVIDE IT BY 1.8
    converted_temperature = (temperature - 32) / 1.8
    results_entry.insert(0, converted_temperature)


#   THIS FUNCTION WILL CONVERT THE TEMPERATURE BASED ON THE conversion_value
def convert_temperature():
    #   IF THE conversion_value IS Fahrenheit, THEN RUN THE fahrenheit_to_celsius FUNCTION
    if conversion_value == "Fahrenheit":
        #   FIRST, WE GET THE VALUE OF THE fahrenheit_entry
        temperature = fahrenheit_entry.get()
        #   THEN WE CHECK IF temperature IS A DIGIT OR NOT
        if temperature.isdigit():
            fahrenheit_to_celsius(int(fahrenheit_entry.get()))
        else:
            #   INFORM THE USER THAT THEY SHOULD INPUT ONLY NUMBERS
            tkinter_module.messagebox.showinfo("Input Error", "Only integers are allowed in entries")
            #   NOW, WE CLEAR THE fahrenheit_entry FOR THE USER
            fahrenheit_entry.delete(0, tkinter_module.END)

        #   IF THE conversion_value IS Celsius, THEN RUN THE celsius_to_fahrenheit FUNCTION
    elif conversion_value == "Celsius":
        #   FIRST, WE GET THE VALUE OF THE celsius_entry

        temperature = celsius_entry.get()
        #   THEN WE CHECK IF temperature IS A DIGIT OR NOT
        if temperature.isdigit():
            celsius_to_fahrenheit(int(celsius_entry.get()))
        else:
            #   INFORM THE USER THAT THEY SHOULD INPUT ONLY NUMBERS
            tkinter_module.messagebox.showinfo("Input Error", "Only integers are allowed in entries")
            #   NOW, WE CLEAR THE celsius_entry FOR THE USER
            celsius_entry.delete(0, tkinter_module.END)


def clear_entries():
    celsius_entry.delete(0, tkinter_module.END)
    results_entry.delete(0, tkinter_module.END)
    fahrenheit_entry.delete(0, tkinter_module.END)


#   CREATE THE celsius_label_frame FOR THE CELSIUS TO FAHRENHEIT CONVERSION
celsius_label_frame = tkinter_module.LabelFrame(window, text="Celsius to Fahrenheit ", width=200, height=100, fg="#de1a1a")
celsius_label_frame.place(x=10, y=10)

#   CREATE THE ENTRY BOX INSIDE THE celsius_label_frame
celsius_entry = tkinter_module.Entry(celsius_label_frame, state=tkinter_module.DISABLED)
celsius_entry.place(x=0, y=0)

#   CREATE THE fahrenheit_label_frame FOR THE FAHRENHEIT TO  CELSIUS CONVERSION
fahrenheit_label_frame = tkinter_module.LabelFrame(window, text="Fahrenheit to Celsius ", width=200, height=100, fg="#de1a1a")
fahrenheit_label_frame.place(x=400, y=10)

#   CREATE THE ENTRY BOX INSIDE THE fahrenheit_label_frame
fahrenheit_entry = tkinter_module.Entry(fahrenheit_label_frame, state=tkinter_module.DISABLED)
fahrenheit_entry.place(x=0, y=0)

#   CREATE THE BUTTON TO TRIGGER THE celsius_entry STATE CHANGE
celsius_to_fahrenheit_btn = tkinter_module.Button(window, text="Activate - Celsius to Fahrenheit ", command=toggle_celsius_entry, fg="#de1a1a")
celsius_to_fahrenheit_btn.place(x=10, y=150)

#   CREATE THE BUTTON TO TRIGGER THE fahrenheit_entry STATE CHANGE
fahrenheit_to_celsius_btn = tkinter_module.Button(window, text="Activate - Fahrenheit TO Celsius ", command=toggle_fahrenheit_entry, fg="#de1a1a")
fahrenheit_to_celsius_btn.place(x=360, y=150)

#   CREATE THE BUTTON TO TRIGGER THE convert_temperature
calculate_conversion_btn = tkinter_module.Button(window, text="Calculate Conversion", command=convert_temperature, fg="#de1a1a")
calculate_conversion_btn.place(x=10, y=250)

#   CREATE THE results_entry TO HOLD THE RESULTS OF THE CONVERSION
results_entry = tkinter_module.Entry(window, width=30)
results_entry.place(x=230, y=250)

#   CREATE THE BUTTON TO TRIGGER THE clear_entries
clear_btn = tkinter_module.Button(window, text="Clear", command=clear_entries, fg="#de1a1a")
clear_btn.place(x=540, y=250)

#   CREATE THE BUTTON TO TRIGGER THE exit_program
exit_btn = tkinter_module.Button(window, text="Exit Program", command=exit_program, fg="#de1a1a")
exit_btn.place(x=250, y=400)

window.mainloop()
