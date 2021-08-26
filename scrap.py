import requests, re
from bs4 import BeautifulSoup
import time, winsound
import ctypes  # An included library with Python install.  
#from playsound import playsound
from datetime import datetime

def LoadWeb(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")    
    #print("Webpage succesfully loaded")
    return soup

URL = "https://nedrug.mfds.go.kr/pbp/CCBCE01/getList"
sleepTime = 30

while True:
    try:
        # Note: Python 2.x users should use raw_input, the 5equivalent of 3.x's input
        temp_input = input("몇 초마다 갱신할까요? (최소 5초 이상, 미입력시 기본 30초) ")
        if temp_input == '':
            break
        sleepTime = int(temp_input)
    except ValueError:
        print("숫자만 입력해 주세요")
        #better try again... Return to the start of the loop
        continue
    if sleepTime >= 5: 
        break
    else:
        print("5 이상으로 입력해 주세요")

while(True):
    soup = LoadWeb(URL)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    temp=soup.find_all('tr')
    for line in temp:
        eyegene = line.find("td", class_="al_l")
        if eyegene is None:
            continue
        elif("아이진" in eyegene):
            print("New application found")
            duration = 500  # milliseconds
            freq = 880  # Hz
            #play_tada()
            winsound.Beep(freq, duration)
            ctypes.windll.user32.MessageBoxW(0, "아이진!!!!!!!!!", "아이진!", 1)
            break
        else:
            print("아이진 승인됐니? 아니요 "+eyegene.find("span").text)        
    print("***")
    time.sleep(sleepTime)
