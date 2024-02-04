def convert_temperature(temp, unit):
    if  unit == "C":
        return (temp * 9/5)+ 32 # Celsius to Fahrenheit
    elif unit == "F":
        return (temp-32)
    else: 
        return None
# Asking for user input for num_dice and num_sides.
temp_input = float(input("Enter the temperature: "))
unit_input = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

print ("Convertin 100F to celcius", convert_temperature(100, "F"))
print ("Convertin 0C to celcius", convert_temperature(0,"C"))




