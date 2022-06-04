import os
import time
import webbrowser

#input variables to get the meeting time, name and link
cl = input('class name>> ')
tol = input(' what time is the meeting?this is only for you ')
ttsm = float(input('enter time left in minutes\n{this is important}>> '))
tts = int(ttsm*60)
link = input('link to open after the given time>> ')
sno = 10

#showing information
print("----------------------\ndon't close me, i'll open a " + cl.upper()+ " meeting at "+tol+" Inshallah\n----------------------")

#a timer to show how many minutes passed and left
for i in range(tts):
    if i % sno == 0:
        print(str(i)+'  sec passed and ' +str(tts-i) +'sec left')
        time.sleep(sno)

#terminating and opening the given link        
print(str(tts)+ 'sec paased, i can open the link now' + link)
webbrowser.open(link)
