age = int(input("Age of the person:"))
Celsius = float(input("Celsius value:"))
Fahrenheit = 9/5 * (Celsius) + 32
print("F={:.1f}""°F".format(Fahrenheit))
if age >= 12:
    print("Adult")
    if Fahrenheit < 98.6:
        print("Low Fever")
    elif Fahrenheit <= 99.1:
        print("Normal Condition")
    else:
        print("High Fever")
else:
    print("Child")
    if Fahrenheit < 97.7:
        print("Low Fever")
    elif Fahrenheit <= 100.4:
        print("Normal Condition")
    else:
        print("High Fever")