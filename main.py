import time
import random
from random import randint
from random import choices
import sys
chars= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","$","%","&","(",")","*",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","0","1","2","3","4","5","6","7","8","9"]
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
      print(even,flush=True, end=inbetween)
      even=even+2
    elif eocr=="o":
      print(odd,flush=True, end=inbetween)
      odd=odd+2
    elif eocr=="c":
      print(consec,flush=True, end=inbetween)
      consec=consec+1
    elif eocr=="r":
      print(random.randint(int(randlowcap),int(randhighcap)),flush=True, end=inbetween)
    elif eocr=="p":
      password=random.sample(chars,letters)
      divider = ""
      password = divider.join(password) 
      print(password,flush=True, end=inbetween)
    elif eocr=="pr":
      password=choices(chars, k=letters)
      divider = ""
      password = divider.join(password) 
      print(password,flush=True, end=inbetween)
    else:
      print("Unrecognized. Type either e, o or c or r")

  if againagain<=1:
    print(" \n")
print("even, odd, consecutive, random, password or password-repeat ")
eocr=input("e/o/c/r/p/pr ")
time.sleep(1)
times=input("How many times/strings? ")
againagain=int(times)
time.sleep(1)
speed=input("What speed should it print, \nAnswer in seconds. (0.02 Is Normal-ish speed) ")
time.sleep(1)
inbetween=input("What should be inbetween each string (eg: space, comma, newline (/n).). \nAnswer with the string inbetween, Not the name of it \n(write ' ' , not 'space') ")
if inbetween=="/n":
  inbetween="\n"
else:
  print("")
if eocr=="e":
  print("Alright, The final number will be",str(againagain * 2))
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
  else:
    print("\n")
elif eocr=="o":
  print("Alright, The final number will be",str(againagain * 2+1))
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
  else:
    print("\n")
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
    print("\n")
elif eocr=="p":
  letters=int(input("Alright, How many characters should the password have? (no higher than 88) "))
  time.sleep(1)
  print("Okay, It will print",times,"passwords,\nEach with",letters," NON-REPEATING characters each")
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    times=int(times)-1
    times=str(times)
    massprint()
    time.sleep(1)
    print("Done!")
elif eocr=="pr":
  letters=int(input("Alright, How many characters should the password have? "))
  time.sleep(1)
  print("Okay, It will print",times,"passwords,\nEach with",letters," REPEATING characters each")
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    times=int(times)-1
    times=str(times)
    massprint()
    time.sleep(1)
    print("Done!")
else:
  print("Restart and input 'e' or 'o' or 'c' or 'r' or 'p'")
print("Press the Enter key to exit")
exit1=input(" ")
exit()