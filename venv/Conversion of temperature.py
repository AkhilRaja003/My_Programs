temp = int(input("Temperature of the person:"))
def calculate(C):
    fahrenheit = 9/5 * C + 32
    print("F = {:.1f} °F".format(fahrenheit))
calculate(temp) 