import time
import sys
def massprint():
  againagain = int(times)
  even=0
  odd=1
  consec=0
  while againagain >= 0:
    time.sleep(0.02)
    againagain -= 1
    if eoc=="e":
      print(even,flush=True, end=" ")
      even=even+2
    elif eoc=="o":
      print(odd,flush=True, end=" ")
      odd=odd+2
    elif eoc=="c":
      print(consec,flush=True, end=" ")
      consec=consec+1
    else:
      print("Unrecognized. Type either e, o or c")

  if againagain<=1:
    print(" \n")
print("Do you want to print even numbers, odd numbers \nor just consecutive numbers? ")
eoc=input("e/o/c ")
time.sleep(1)
times=input("And how many times should it do this? ")
print(" ")
massprint()