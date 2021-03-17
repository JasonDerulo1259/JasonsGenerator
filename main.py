import time
import random
from random import randint
from random import choices
import sys
import os
import math
import datetime
from datetime import datetime
now = datetime.now()
timestamp = now.strftime("Created %d %b, %H:%M \n")
filetimestamp=now.strftime("%d.%m.%y_%H-%M-%S")
chars= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","$","%","&","(",")","*",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","0","1","2","3","4","5","6","7","8","9"]
startat=0
startatstr="0"

def massprint():
  startat=int(startatstr)
  againagain = int(times)
  even=startat
  odd=startat+1
  consec=startat
  rand=0
  import os
  if os.path.exists("output_"+filetimestamp+".txt"):
    os.remove("output_"+filetimestamp+".txt")
  else:
    print("",flush=True, end="")
  fixvar1="output_"+filetimestamp+".txt"
  time.sleep(0.1)
  f=open(fixvar1,"w")
  f.write(timestamp)
  f.close()
  time.sleep(1)
  while againagain >= 0:
    time.sleep(float(speed))
    againagain -= 1
    if eocr=="e":
      if conran=="c":
        f=open(fixvar1,"a")
        print(even,flush=True, end=inbetween, file=f)
        print(even,flush=True, end=inbetween)
        f.close()
        even=even+2
      elif conran=="r":
        random_float = random.uniform(int(randlowcap), int(randhighcap))
        roundedeven=math.ceil(random_float / 2.) * 2
        f=open(fixvar1,"a")
        print(roundedeven,flush=True, end=inbetween, file=f)
        print(roundedeven,flush=True, end=inbetween)
        f.close()
    elif eocr=="o":
      if conran=="c":
        f=open(fixvar1,"a")
        print(odd,flush=True, end=inbetween, file=f)
        print(odd,flush=True, end=inbetween)
        f.close()
        odd=odd+2
      elif conran=="r":
        random_float = random.uniform(int(randlowcap), int(randhighcap))
        roundedodd=math.ceil(random_float / 2.) * 2+1
        f=open(fixvar1,"a")
        print(roundedodd,flush=True, end=inbetween, file=f)
        print(roundedodd,flush=True, end=inbetween)
    elif eocr=="c":
      f=open(fixvar1,"a")
      print(consec,flush=True, end=inbetween, file=f)
      print(consec,flush=True, end=inbetween)
      f.close()
      consec=consec+1
    elif eocr=="r":
      f=open(fixvar1,"a")
      print(random.randint(int(randlowcap),int(randhighcap)),flush=True, end=inbetween, file=f)
      print(random.randint(int(randlowcap),int(randhighcap)),flush=True, end=inbetween)
      f.close()
    elif eocr=="p":
      password=random.sample(chars,letters)
      divider = ""
      password = divider.join(password) 
      f=open(fixvar1,"a")
      print(password,flush=True, end=inbetween, file=f)
      print(password,flush=True, end=inbetween)
      f.close()
    elif eocr=="pr":
      password=choices(chars, k=letters)
      divider = ""
      password = divider.join(password) 
      f=open(fixvar1,"a")
      print(password,flush=True, end=inbetween, file=f)
      print(password,flush=True, end=inbetween)
      f.close()
    else:
      print("Unrecognized. Type either e, o or c or r")

  if againagain<=1:
    print(" \n")
print("even, odd, consecutive, random, password or password-repeat ")
eocr=input("e/o/c/r/p/pr ")
time.sleep(0.5)
times=input("How many times/strings? ")
againagain=int(times)
time.sleep(0.5)
speed=input("What speed should it print, \nAnswer in seconds. (0.02 Is Normal-ish speed) ")
time.sleep(0.5)
inbetween=input("What should be inbetween each string (eg: space, comma, newline (/n).). \nAnswer with the string inbetween, Not the name of it \n(write ' ' , not 'space') ")
if inbetween=="/n":
  inbetween="\n"
else:
  print("")
if eocr=="e":
  conran=input("Should It Be consecutive, or random?\n c/r ")
  if conran=="c":
    print("Consecutive Selected.")
    time.sleep(0.5)
    startatstr=input("What number should it start at? ")
    time.sleep(0.5)
    print("Alright, The final number will be",str((againagain * 2)+int(startatstr)))
  elif conran=="r":
    print("Random Selected.")
    time.sleep(0.5)
    randhighcap=input("And what do you want the highest random number to be? ")
    time.sleep(0.5)
    randlowcap=input("And what do you want the lowest random number to be? ")
    time.sleep(0.5)
    print("It will print" ,times, "random, even numbers.\nWith a high cap of",randhighcap,"\nAnd A low cap of",randlowcap,". ")
    time.sleep(0.5)
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
  else:
    print("\n")
elif eocr=="o":
  conran=input("Should It Be consecutive, or random?\n c/r ")
  if conran=="c":
    print("Consecutive Selected.")
    time.sleep(0.5)
    time.sleep(0.5)
    startatstr=input("What number should it start at? ")
    print("Alright, The final number will be",str((againagain * 2+1)+int(startatstr)))
  elif conran=="r":
    print("Random Selected.")
    time.sleep(0.5)
    randhighcap=input("And what do you want the highest random number to be? ")
    time.sleep(0.5)
    randlowcap=input("And what do you want the lowest random number to be? ")
    time.sleep(0.5)
    print("It will print" ,times, "random, odd numbers.\nWith a high cap of",randhighcap,"\nAnd A low cap of",randlowcap,". ")
    time.sleep(0.5)
  else:
    print("Error. Invalid response.")
    time.sleep(1)
    exit()
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
  else:
    print("\n")
elif eocr=="c":
  time.sleep(0.5)
  startatstr=input("What number should it start at? ")
  time.sleep(0.5)
  print("Alright, The final number will be",str((againagain)+int(startatstr)))
  varcontinue=input("Is this okay? (y/n) ")
  if varcontinue=="y":
    print(" ")
    massprint()
    time.sleep(1)
    print("Done!")
elif eocr=="r":
  time.sleep(0.5)
  randhighcap=input("And what do you want the highest random number to be? ")
  time.sleep(0.5)
  randlowcap=input("And what do you want the lowest random number to be? ")
  time.sleep(0.5)
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
  time.sleep(0.5)
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
  time.sleep(0.5)
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