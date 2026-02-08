#TempConvert.py
#Name: Afrah Mohamoud
#Date: 02/05/2026
#Assignment: Lab 03
#Purpose: Convert Fahrenheit to Celsius and display the result.

def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal precision
  #Output converted temperature.
  try:
    tempF = float(input("Enter temperature in Fahrenheit: "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    return

  tempC = (tempF - 32) * 5 / 9
  tempC = round(tempC, 1)

  print(f"{tempF} is {tempC} degrees Celsius.")
if __name__ == '__main__':
  main()


