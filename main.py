import time
import random
from random import randint
import sys
def massprint():
  againagain = int(times)
  even=0
  odd=1
  consec=0
  rand=0
  while againagain >= 0:
    time.sleep(float(speed))
    againagain -= 1
    if eocr=="e":
      print(even,flush=True, end=" ")
      even=even+2
    elif eocr=="o":
      print(odd,flush=True, end=" ")
      odd=odd+2
    elif eocr=="c":
      print(consec,flush=True, end=" ")
      consec=consec+1
    elif eocr=="r":
      print(random.randint(int(randlowcap),int(randhighcap)),flush=True, end=" ")
    else:
      print("Unrecognized. Type either e, o or c or r")

  if againagain<=1:
    print(" \n")
print("Do you want to print even numbers, odd numbers \n, consecutive or random numbers? ")
eocr=input("e/o/c/r ")
time.sleep(1)
times=input("And how many times should it do this? ")
time.sleep(1)
speed=input("Okay, And What speed should it print the numbers, \nAnswer in seconds. (0.02 Is Default) ")
time.sleep(1)
againagain = int(times)
if eocr=="e":
  print("Alright, The final number will be",str(againagain * 2))
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
  else:
    exit()
elif eocr=="o":
  print("Alright, The final number will be",str(againagain * 2+1))
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
  else:
    exit()
elif eocr=="c":
  print("Alright, The final number will be",str(againagain))
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
elif eocr=="r":
  time.sleep(1)
  randhighcap=input("And what do you want the highest random number to be? ")
  time.sleep(1)
  randlowcap=input("And what do you want the lowest random number to be? ")
  time.sleep(1)
  print("Alright, It will print",str(againagain),"random numbers \nWith a high cap of",randhighcap,"\nAnd a low cap of",randlowcap)
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
  else:
    exit()
else:
  exit()