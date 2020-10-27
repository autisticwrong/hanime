import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

BASE_LINK = "https://hanime.tv/"

config = {
  "target_path": './images/', 
  "tags": 
    {
    "SFW": { "enabled": False, "divIndex": 1 },
    "NSFW": { "enabled": True, "divIndex": 2 },
    "Furry": { "enabled": False, "divIndex": 3 },
    "Futa": { "enabled": False, "divIndex": 4 },
    "Yaoi": { "enabled": False, "divIndex": 5 },
    "Yuri": { "enabled": True, "divIndex": 6 },
    "Trap": { "enabled": False, "divIndex": 7 },
    "3D": { "enabled": False, "divIndex": 8 },
  }
}

class Hanime():
  def __init__(self, config):
    self.config = config
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get(BASE_LINK + "browse/images")
    self.links = []
  
  def run(self):
    if not os.path.exists(self.config["target_path"]):
      os.mkdir(self.config["target_path"])
    os.chmod(self.config["target_path"], 0o777)
    pages = self.pages()
    
    for i in range(pages):
      if i < pages:
        self.scrape()
    print(len(self.links))
    
  def pages(self):
    self.pages = int(input("How many pages do you want to scrape? "))
    return self.pages
    
  def scrape(self):
    for i in range(1, 100):
      try:
        content = self.driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[5]/a[{0}]""".format(i)).get_attribute("href")
        print(content)
        self.links.append(content)
    
      except:
        pass
