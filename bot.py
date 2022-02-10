print("Type 'help' for show command")
import os
from colorama import init
from colorama import Fore
init()
c=1
while True :
    pw=input(Fore.RED + 'G-BOT>')
    print()
    if pw == 'help':
       print("----------COMMAND----------\n\n 1.hey g-bot\n 2.i am fine and you\n 3.who is your boss\n 4.who gave you this name\n 5.what is the g-one github account\n 6.Thank you for help")
    if pw == 'hey g-bot':
        os.system('espeak -a 200 -s 150 -p 70 -g 15  "hello sir how are you" -ven+f4') 
    if pw == 'i am fine and you':
        os.system('espeak -a 150 -s 140 -p 65 -g 11  "i am also fine sir" -ven+f4')      
    if pw == 'who is your boss':
        os.system('espeak -a 200 -s 150 -p 70 -g 15  "G-one sir is my boss" -ven+f4')   
    if pw == 'who gave you this name':
         os.system('espeak -a 150 -s 140 -p 65 -g 11  "G-one gave me this name" -ven+f4')       
    if pw == 'what is the g-one github account':
         os.system('espeak -a 200 -s 150 -p 70 -g 15  "G-one github account is:https://github.com/Juniorredcoder/" -ven+f4')
    if pw == 'Thank you for help':
         os.system('espeak -a 200 -s 150 -p 70 -g 15  "welcome sir" -ven+f4')     
    if pw == 'help':
         break
    c+=1
    if c == 500000 :
        print('you have reached the max number of attempts !!')
        break
        os.system('espeak -a 150 -s 140 -p 65 -g 11  "i dont understand" -ven+f4')

