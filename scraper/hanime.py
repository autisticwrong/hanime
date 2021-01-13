import os
import time
import requests
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

BASE_LINK = "https://hanime.tv/"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
hrome_options.add_argument("--window-size=1920,1080")


class Hanime():
    def __init__(self, config):
        self.config = config
        self.driver = webdriver.Chrome(
            executable_path=self.config['driver_path'], options=chrome_options)
        self.driver.get(BASE_LINK + "browse/images")
        self.links = []

    def run(self):
        if not os.path.exists(self.config["target_path"]):
            os.mkdir(self.config["target_path"])
        os.chmod(self.config["target_path"], 0o777)

        pages = self.pages()
        self.current_page = 1

        self.driver.find_element_by_xpath(
            """//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[1]/div""").click()
        time.sleep(1)

        while self.current_page <= pages:
            self.scrape()
            nextPage = self.driver.find_element_by_xpath(
                """//*[@id="app"]/div[4]/main/div/div/div/div[4]/button[3]/div""")
            nextPage.click()
            self.current_page += 1

        print(len(self.links))

        # self.download(self.links)

    def pages(self):
        self.pages = int(input("How many pages do you want to scrape? "))
        return self.pages

    def scrape(self):
        for i in range(1, 100):
            try:
                content = self.driver.find_element_by_xpath(
                    """//*[@id="app"]/div[4]/main/div/div/div/div[5]/a[{0}]""".format(i)).get_attribute("href")
                print(content)
                self.links.append(content)

            except:
                pass

    def download(self):
        image_list = self.links
        count = 1
        for i in image_list:
            if "threading" in self.config and self.config['threading']:
                threading.Thread(target=self._save_image, args=[i, count]).start()
            else:
                self._save_image(i, count)
            count += 1

    def _save_image(self, link, count):
        img_data = requests.get(link).content
        with open(f'./images/image{count}.jpg', 'wb') as handler:
            handler.write(img_data)
