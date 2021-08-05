import datetime as dt
import json
import os
import requests
import shutil
import pickle
import requests
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from urllib.parse import quote
import pyautogui as pg
import webbrowser as web

 
class WhatsAppElements:
    search = (By.CSS_SELECTOR, "#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text")
 
class WhatsApp:
    browser =  None
    timeout = 10  # The timeout is set for about ten seconds
    def __init__(self, wait, screenshot=None, session=None):
        self.browser = webdriver.Firefox(executable_path="C:/Users/Kushagra/Documents/py/geckodriver.exe")# change path
        self.browser.get("https://web.whatsapp.com/") #to open the WhatsApp web
        # you need to scan the QR code in here (to eliminate this step, I will publish another blog
        WebDriverWait(self.browser,wait).until( 
        EC.presence_of_element_located(WhatsAppElements.search)) #wait till search element appears
    def goto_main(self):
        try:
            self.browser.refresh()
            Alert(self.browser).accept()
        except Exception as e:
            print(e)
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            WhatsAppElements.search))

 
    def get_last_message_for(self, name):
        messages = list()
        search = self.browser.find_element(*WhatsAppElements.search)
        search.send_keys(name+Keys.ENTER)
        time.sleep(3)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        for i in soup.find_all("div", class_="message-in"):
            message = i.find("span", class_="selectable-text")
            if message:
                message2 = message.find("span")
                if message2:
                    messages.append(message2.text)
        messages = list(filter(None, messages))
        return messages
    def sendwhatmsg_instantly(self,phone_no: str, message: str, wait_time: int = 20,
                              tab_close: bool = False) -> None:
        """Send WhatsApp Message Instantly"""

        if "+" not in phone_no:
            raise CountryCodeException("Country code missing from phone_no")

        parsed_message = quote(message)
        self.browser.get('https://web.whatsapp.com/send?phone=' +
                 phone_no + '&text=' + parsed_message)
        time.sleep(2)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        time.sleep(wait_time - 2)
        pg.press('enter')
        #if tab_close:
        #    close_tab()

    def sendwhats_image(phone_no: str, img_path: str, caption: str = " ", wait_time: int = 15):
        if '+' not in phone_no:
            raise CountryCodeException("Please provide country code!")

        self.browser.get('https://web.whatsapp.com/send?phone=' +
                 phone_no + '&text=' + caption)
        time.sleep(5)
        if system().lower() == "linux":
            if img_path.split("/")[-1].endswith(("PNG", "png")):
                os.system(
                    f"xclip -selection clipboard -target image/png -i {img_path}")
            elif img_path.split("/")[-1].endswith(("jpg", "JPG", "jpeg", "JPEG")):
                os.system(
                    f"xclip -selection clipboard -target image/jpg -i {img_path}")
            time.sleep(wait_time)
            pg.hotkey("ctrl", "v")
            time.sleep(5)
            pg.press('enter')
        elif system().lower() == "windows":
            import win32clipboard
            from io import BytesIO
            from PIL import Image

            image = Image.open(img_path)
            output = BytesIO()
            image.convert('RBG').save(output, "BMP")
            data = output.getvalue()[14:]
            output.close()
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
            win32clipboard.CloseClipboard()
            time.sleep(wait_time)
            pg.hotkey("ctrl", "v")
            time.sleep(3)
            pg.press("enter")

        else:
            print(f"{system()} not supported!")

    def text_to_handwriting(string: str, save_to: str = "pywhatkit.png", rgb: tuple = (0, 0, 138)) -> None:
        """Convert the given str to handwriting"""
        data = requests.get(
            "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (string, rgb[0], rgb[1], rgb[2])).content
        with open(save_to, "wb") as file:
            file.write(data)
            file.close()

