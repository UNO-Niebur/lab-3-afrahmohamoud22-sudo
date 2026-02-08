#ApproxPi.py
#Name: Afrah Mohamoud
#Date: 2/05/2026
#Assignment: Lab 3
#Purpose: Approximate pi and report timing.
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #round pi to 2 decimal places
  precision = 2

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approximation = 0.0
  denominator = 1.0
  sign = 1.0
  target = round(realPi, precision)

  while round(approximation, precision) != target: 
    approximation += sign * (4.0 / denominator)
    denominator += 2.0
    sign *= -1.0

  end = time.time()

  elapsedTime = end - start
  print(f"Approx pi: {round(approximation, precision)}")
  print(f"Math pi  : {round(realPi, precision)}")
  print(f"Matched to {precision} decimals in {elapsedTime:.6f} seconds.")

if __name__ == '__main__':
  main()
