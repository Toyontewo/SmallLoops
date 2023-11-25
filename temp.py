# ceelc = int(input("Enter Degrees in Celsius: "))
# faren = int(input("Enter Degrees in Fahrenheit: "))
#
# celsius = (faren - 32) * 5 / 9
# fareheight = (ceelc * 9/5) + 32
#
#
# print(f"{celsius} is {fareheight} in Farenheit \n{fareheight} is {celsius} in Celsuis")
# #
# # test = int(input("1. Degrees to Fahrenheit \n 2. Fahrenheit to Degreees"))
# #
# # game_on = True
# #
# # while game_on:
# #     if test == 1:
# #         deg = int(input("Degrees: "))
# #         deg

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Convert Celsius to Fahrenheit
celsius = int(input("Enter in Celcius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")

# Convert Fahrenheit to Celsius
fahrenheit = int(input("Enter in fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is {celsius}°C")
