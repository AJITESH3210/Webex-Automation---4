import subprocess
import pyautogui
import time
import pandas as pd
import webbrowser

from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

df = pd.read_csv("timings.csv")
print(df)

def sign_in(meetingid, pswd):
      subprocess.call('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
      time.sleep(2)

      title_btn = pyautogui.locateCenterOnScreen('titlebar.png')
      pyautogui.moveTo(title_btn)
      #pyautogui.click()
      pyautogui.write('https://meetingsapac29.webex.com/join/pr1563552244') # this link is che class
      pyautogui.press('enter')
      time.sleep(7)
      pyautogui.press('left')
      pyautogui.press('enter')
      
      time.sleep(15)
      # Now it will open webex 

      #meeting_id_btn = pyautogui.locateCenterOnScreen('join_btn_press.png')
      #pyautogui.moveTo(meeting_id_btn)
      #pyautogui.click()
      #pyautogui.write(meetingid)
      #pyautogui.press('enter')

      #time.sleep(15)

      clear_btn = pyautogui.locateAllOnScreen('clear1.png')
      for btn in clear_btn:
            pyautogui.moveTo(btn)
            pyautogui.click()

      clear_btn = pyautogui.locateAllOnScreen('clear2.png')
      for btn in clear_btn:
            pyautogui.moveTo(btn)
            pyautogui.click()

      name_btn = pyautogui.locateCenterOnScreen('name.png')
      pyautogui.moveTo(name_btn)
      pyautogui.click()
      pyautogui.write('J AJITESH')

      email_btn = pyautogui.locateCenterOnScreen('email.png')
      pyautogui.moveTo(email_btn)
      pyautogui.click()
      pyautogui.write('jalluri3210@gmail.com')

      remember_btn = pyautogui.locateCenterOnScreen('remember.png')
      pyautogui.moveTo(remember_btn)
      pyautogui.click()

      join_pop_btn = pyautogui.locateCenterOnScreen('join_pop.png')
      pyautogui.moveTo(join_pop_btn)
      pyautogui.click()

      join_final_btn = pyautogui.locateCenterOnScreen('join_final.png')
      pyautogui.moveTo(join_final_btn)
      pyautogui.click()

sign_in("1563552244", "8AmcpK")
