def convertToFahrenheit(degreesCelsius):
    # Calculate and return the degrees Fahrenheit:
    return degreesCelsius * (9 / 5) + 32


def convertToCelsius(degreesFahrenheit):
    # Calculate and return the degrees Celsius:
    return (degreesFahrenheit - 32) * (5 / 9)


def doConversion(temp, kind):
    while kind not in ["F","C"]:
        kind = input("Enter a unit (F or C) which you want converted to the other.")
    if kind == "F":
        answer = convertToFahrenheit(temp)
    elif kind == "C":
        answer = convertToCelsius(temp)
    return answer

def main():
    temperature = float(input("What temp would you like to convert?"))
    unit = input("type F if you want to convert Fahrenheit, type C if you want to convert Celsius.")
    result = doConversion(temperature, unit)
    print (f"The converted temp is: {result} degrees")


if __name__ == "__main__":
    main()