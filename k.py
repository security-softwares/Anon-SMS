import requests
import json
from datetime import datetime
import pyfiglet
print ("\033[1;32;40m] tool made by Hackers Tech:-")
print ("-"*50)
print("date and time & millisecond " ,datetime.now())
p=datetime.now()
print ("\033[93m .")
print ("year=",p.year,"month 0",p.month,"day",p.day)
print ("hour",p.hour,"minutes",p.minute)
print ("\033[1;32;40m hi ")
a=pyfiglet.figlet_format("HACKERS \n TECH")
print(a)
print("\033[91m also follow us on instagram id ")
bn='''
||     ||      ############
||     ||           ##
||=====||           ##
||     ||           ##
||     ||           ##
                    ##
'''
print(bn)
number = input(" enter number with + code etc what ever you hve for india code is +91 !!!\n ->")

Message = input(" \n enter Message ")
k=Message[0:70]

m =input("send message Y/N ")
if m== "y" or m== "Y":
  print("\n"+number+"\n"+k+"\n")
  p = requests.post('https://textbelt.com/text', {
  'phone': number,
  'message': k,
  'key': 'textbelt',
    })
  print(p.json())
elif m =="N" or m== "n":
  print ("exiting !!!!")
  Quit()
else :
  print("failed")
  
