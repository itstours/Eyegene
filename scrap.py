import requests, re
from bs4 import BeautifulSoup
import time, winsound
import ctypes  # An included library with Python install.  
from playsound import playsound

def LoadWeb(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    print("Webpage succesfully loaded")
    return soup

URL = "https://nedrug.mfds.go.kr/pbp/CCBCE01/getList"
sleepTime = 30

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        sleepTime = int(input("몇 초마다 갱신할까요? (최소 15초 이상) "))
    except ValueError:
        print("숫자만 입력해 주세요")
        #better try again... Return to the start of the loop
        continue
    if sleepTime >= 15: 
        break
    else:
        print("15 이상으로 입력해 주세요")

while(True):
    soup = LoadWeb(URL)
    eyegene = soup.find("td", class_="al_l").text
    if("아이진" in eyegene):
        print("New application found")
        duration = 500  # milliseconds
        freq = 880  # Hz
        #play_tada()
        winsound.Beep(freq, duration)
        ctypes.windll.user32.MessageBoxW(0, "아이진!!!!!!!!!", "아이진!", 1)
        break
    else:
        print("아이진 승인됐니? 아니요 "+eyegene)
    time.sleep(sleepTime)
