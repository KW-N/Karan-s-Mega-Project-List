"""
Script based on the projects found in https://github.com/karan/Projects 
Unit Converter (temp, currency, volume, mass and more) - 
Converts various units between one another. 
The user enters the type of unit being entered, the type of unit they want to convert to and then the value. 
The program will then make the conversion.
""" 
import tkinter as tk                    # Used for the GUI
from tkinter import messagebox, ttk     # Used for error messages 
from decimal import Decimal, getcontext # Used for calculations to get them to act like decimals

getcontext().prec = 18

def main():
    """ Unit converter """
    root = tk.Tk()
    root.title('Unit converter')
    root.geometry("900x200")
    #----- Functions used by the GUI 
    def display_result(text, position):
        """ Clear existing result and display new text in the tkinter GUI """
        for widget in root.grid_slaves():
            if int(widget.grid_info()["row"]) == position and int(widget.grid_info()["column"]) == 5:
                widget.destroy()
        label = tk.Label(root, text=text)
        label.grid(row=position, column=5)

    def length_converter():
        """Gets the information from the GUI converts it and displays it"""
        try:
            length_value = Decimal(length.get())
            input_unit = drop_down_length_input_unit.get()
            output_unit = drop_down_length_output_unit.get()
            length_unit = {"Millimeters": Decimal('16093400'),
                        "Centimeters": Decimal('160934'),
                        "Inches": Decimal('63360') , 
                        "Feet": Decimal('5280'), 
                        "Yard":Decimal('1760'),
                        "Meter": Decimal('1609.34'),
                        "Kilometers": Decimal('1.60934'),
                        "Miles": Decimal('1')}
            
            if input_unit in input_unit and output_unit in output_unit:
                length_in_miles = length_value / length_unit[input_unit]
                converted_length = length_in_miles * length_unit[output_unit]
                display_result(f"{length_value} {input_unit} = {converted_length:.8f} {output_unit}", 1)
        except ValueError:
            messagebox.showerror("Error", f"Please only enter numbers in the length converter.")
        
    def temperature_converter():
        """Gets the information from the GUI, converts it, and displays it."""
        try:
            temperature_value = float(temperature.get())
            input_unit = drop_down_temperature_input_unit.get()
            output_unit = drop_down_temperature_output_unit.get()
            
            if input_unit == "Kelvin (K)":
                temp_in_c = temperature_value - 273.15
            elif input_unit == "Fahrenheit (F)":
                temp_in_c = (temperature_value - 32) / 1.8
            elif input_unit == "Rankine (R)":
                temp_in_c = (temperature_value - 491.67) / 1.8
            elif input_unit == "Reaumur (Re)":
                temp_in_c = temperature_value / 0.8
            elif input_unit == "Celsius (C)":
                temp_in_c = temperature_value
            else:
                raise ValueError("Invalid input unit.")

            if output_unit == "Kelvin (K)":
                converted_temperature = temp_in_c + 273.15
            elif output_unit == "Fahrenheit (F)":
                converted_temperature = temp_in_c * 1.8 + 32
            elif output_unit == "Rankine (R)":
                converted_temperature = (temp_in_c + 273.15) * 1.8
            elif output_unit == "Reaumur (Re)":
                converted_temperature = temp_in_c * 0.8
            elif output_unit == "Celsius (C)":
                converted_temperature = temp_in_c
            else:
                raise ValueError("Invalid output unit.")

            display_result(
                f"{temperature_value} {input_unit} = {converted_temperature:.2f} {output_unit}", 2)
        except ValueError:
            messagebox.showerror("Error", "Please only enter numbers in the temperature converter.")
    
    def volume_converter():
        """Gets the information from the GUI converts it and displays it"""
        try:
            volume_value = Decimal(volume.get())
            input_unit = drop_down_volume_input_unit.get()
            output_unit = drop_down_volume_output_unit.get()
            volume_unit = {"Cubic centimeter": Decimal('1000000'),
                           "Cubic inch": Decimal('61023.7'), 
                           "pint (US)": Decimal('2113.38'), 
                           "Litre": Decimal('1000'),
                           "Gallon (US)": Decimal('264.172'), 
                           "Cubic foot": Decimal('35.3147'),
                           "Cubic meter": Decimal('1')}
            
            if input_unit in input_unit and output_unit in output_unit:
                volume_in_m3 = volume_value / volume_unit[input_unit]
                converted_volume = volume_in_m3 * volume_unit[output_unit]
                display_result(f"{volume_value} {input_unit} = {converted_volume:.8f} {output_unit}", 3)
        except ValueError:
            messagebox.showerror("Error", f"Please only enter numbers in the volume converter.")

    def mass_converter():
        """Gets the information from the GUI converts it and displays it"""
        try:
            mass_value = Decimal(mass.get())
            input_unit = drop_down_mass_input_unit.get()
            output_unit = drop_down_mass_output_unit.get()
            mass_unit = {"Picogram (pg)": Decimal('1016050000000000000'),
                           "Nanogram (ng)": Decimal('1016050000000000'), 
                           "Microgram (\u03BCg)": Decimal('1016050000000'), 
                           "Milligram (mg)": Decimal('1016050000'), 
                           "Gram (g)": Decimal('1016050'),
                           "Ounce (oz)": Decimal('35840'),
                           "Pound (lb)": Decimal('2240'),
                           "Kilogram (kg)": Decimal('1016.5'),
                           "US ton (ton)": Decimal('1.12'),
                           "tonne (t)": Decimal('1.01605'),
                           "UK ton (ton)": Decimal('1')}
            
            if input_unit in input_unit and output_unit in output_unit:
                mass_in_uk_ton = mass_value / mass_unit[input_unit]
                converted_mass = mass_in_uk_ton * mass_unit[output_unit]
                if converted_mass < Decimal('1e-8'):
                    display_result("Some values are so small that they can be calculated")
                else:
                    display_result(f"{mass_value} {input_unit} = {converted_mass:.8f} {output_unit}", 4)
        except ValueError:
            messagebox.showerror("Error", f"Please only enter numbers in the mass converter.")



    #----- GUI setup subdivided for each function of the converter for clarity 
    #-- Labels for the GUI
    label_converter_type = tk.Label(root, text = 'Converter type')
    label_converter_type.grid(row=0,column=0)

    label_input_value = tk.Label(root, text = 'Input value')
    label_input_value.grid(row=0, column=1)
    
    label_input_unit = tk.Label(root, text = 'Input unit')
    label_input_unit.grid(row=0, column=2)

    label_output_unit = tk.Label(root, text = 'Output unit')
    label_output_unit.grid(row=0, column=3)

    Label_output_result = tk.Label(root, text = 'Result')
    Label_output_result.grid(row=0, column=5)

    #-- Length converter  
    label_length = tk.Label(root, text = 'Length converter')
    label_length.grid(row=1,column=0)

    length = tk.Entry(root)
    length.grid(row=1, column=1,)

    drop_down_length_input_unit = ttk.Combobox(state="readonly",
                                                  values=["Millimeters",
                                                          "Centimeters", 
                                                          "Inches", 
                                                          "Feet", 
                                                          "Yard",
                                                          "Meter",
                                                          "Kilometers",
                                                          "Miles" ])
    drop_down_length_input_unit.grid(row=1, column=2)
    drop_down_length_input_unit.set("Millimeters") 

    drop_down_length_output_unit = ttk.Combobox(state="readonly",
                                                  values=["Millimeters",
                                                          "Centimeters", 
                                                          "Inches", 
                                                          "Feet", 
                                                          "Yard",
                                                          "Meter",
                                                          "Kilometers",
                                                          "Miles" ])
    drop_down_length_output_unit.grid(row=1, column=3)
    drop_down_length_output_unit.set("Millimeters") 

    button_convert_length = tk.Button(root, text = "Convert", command = lambda: length_converter())
    button_convert_length.grid(row=1, column=4)

    #-- Temperature converter  
    label_temperature = tk.Label(root, text = 'Temperature  converter')
    label_temperature.grid(row=2,column=0)

    temperature = tk.Entry(root)
    temperature.grid(row=2, column=1,)

    drop_down_temperature_input_unit = ttk.Combobox(state="readonly",
                                                  values=["Kelvin (K)",
                                                          "Celsius (C)", 
                                                          "Fahrenheit (F)", 
                                                          "Rankine (R)", 
                                                          "Reaumur (Re)"])
    drop_down_temperature_input_unit.grid(row=2, column=2)
    drop_down_temperature_input_unit.set("Kelvin (K)") 

    drop_down_temperature_output_unit = ttk.Combobox(state="readonly",
                                                  values=["Kelvin (K)",
                                                          "Celsius (C)", 
                                                          "Fahrenheit (F)", 
                                                          "Rankine (R)", 
                                                          "Reaumur (Re)"])
    drop_down_temperature_output_unit.grid(row=2, column=3)
    drop_down_temperature_output_unit.set("Kelvin (K)") 

    button_convert_temperature = tk.Button(root, text = "Convert", command = lambda: temperature_converter())
    button_convert_temperature.grid(row=2, column=4)

    #-- Volume converter  
    label_volume = tk.Label(root, text = 'Volume  converter')
    label_volume.grid(row=3,column=0)

    volume = tk.Entry(root)
    volume.grid(row=3, column=1,)

    drop_down_volume_input_unit = ttk.Combobox(state="readonly",
                                                  values=["Cubic centimeter",
                                                          "Cubic inch", 
                                                          "pint (US)", 
                                                          "Gallon (US)", 
                                                          "Litre",
                                                          "Cubic foot",
                                                          "Cubic meter"])
    drop_down_volume_input_unit.grid(row=3, column=2)
    drop_down_volume_input_unit.set("Cubic centimeter") 

    drop_down_volume_output_unit = ttk.Combobox(state="readonly",
                                                  values=["Cubic centimeter",
                                                          "Cubic inch", 
                                                          "pint (US)", 
                                                          "Gallon (US)", 
                                                          "Litre",
                                                          "Cubic foot",
                                                          "Cubic meter"])
    drop_down_volume_output_unit.grid(row=3, column=3)
    drop_down_volume_output_unit.set("Cubic centimeter") 

    button_convert_volume = tk.Button(root, text = "Convert", command = lambda: volume_converter())
    button_convert_volume.grid(row=3, column=4)

    #-- Mass converter  
    label_mass = tk.Label(root, text = 'Mass  converter')
    label_mass.grid(row=4,column=0)

    mass = tk.Entry(root)
    mass.grid(row=4, column=1,)

    drop_down_mass_input_unit = ttk.Combobox(state="readonly",
                                                  values=["Picogram (pg)",
                                                          "Nanogram (ng)", 
                                                          "Microgram (\u03BCg)", 
                                                          "Milligram (mg)", 
                                                          "Gram (g)",
                                                          "Ounce (oz)"
                                                          "Pound (lb)",
                                                          "Kilogram (kg)",
                                                          "US ton (ton)",
                                                          "tonne (t)",
                                                          "UK ton (ton)"])
    drop_down_mass_input_unit.grid(row=4, column=2)
    drop_down_mass_input_unit.set("Gram (g)") 

    drop_down_mass_output_unit = ttk.Combobox(state="readonly",
                                                  values=["Picogram (pg)",
                                                          "Nanogram (ng)", 
                                                          "Microgram (\u03BCg)", 
                                                          "Milligram (mg)", 
                                                          "Gram (g)",
                                                          "Ounce (oz)"
                                                          "Pound (lb)",
                                                          "Kilogram (kg)",
                                                          "US ton (ton)",
                                                          "tonne (t)",
                                                          "UK ton (ton)"])
    drop_down_mass_output_unit.grid(row=4, column=3)
    drop_down_mass_output_unit.set("Gram (g)") 

    button_convert_mass = tk.Button(root, text = "Convert", command = lambda: mass_converter())
    button_convert_mass.grid(row=4, column=4)

    # Runs the user interface 
    root.mainloop()


main()