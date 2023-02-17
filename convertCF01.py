# FILE NAME - convertCF01.py
# NAME - Md Wara
# DATE- 02-08-2023
# DISCRIPTION - converts Celsius to Fahrenheit

def main():
    convertCF()

def convertCF():
    TemperatureCelsius = float (input("Enter a temperature in Celsius: "))
    TemperatureFahrenheit = float((TemperatureCelsius *9/5) + 32)
    print(TemperatureCelsius, "degrees Celsius is", TemperatureFahrenheit, "degrees Fahrenheit." )
    
main()


