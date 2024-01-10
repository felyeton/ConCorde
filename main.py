from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from settings import *

# driver = webdriver.Firefox()
# driver.get("https://www.melihov.tech/concorde/")
# # assert "Python" in driver.title, "NOT PYTHON"
# elem = driver.find_element(By.NAME, "q")
# sleep(10)
# elem.clear()
# sleep(10)
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# sleep(10)
# # assert "No results found." not in driver.page_source
# sleep(10)
# driver.close()


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options,
                          # executable_path=r"webdriver\chromedriver.exe"
                          )

driver.maximize_window()

driver.get("https://www.melihov.tech/concorde/")
sleep(1)
# elem = driver.find_element(By.NAME, "name")
login = driver.find_element(By.XPATH,  '//input[@autocomplete="name"]')
login.send_keys(LOGIN)

password = driver.find_element(By.XPATH,  '//input[@autocomplete="password-current"]')
password.send_keys(PASSWORD)
# elem.send_keys(Keys.ENTER)
# actions = ActionChains

go_button = driver.find_element(By.XPATH,  '//b[@class="bt lp"]')



go_button.click()
# class="bt lp"

# driver.refresh()

sleep(1)


# tmp = driver.find_element(By.XPATH,  '//b[@class="active"]')
tmp = driver.find_element(By.XPATH,  '//i[@data-bt="-content_1;-contbar_1;-content_0;-contbar_0;-toolbar;mod:flaws"]')
print(tmp.text)
sleep(1)
tmp.click()
sleep(1)

# for row in driver.find_elements(By.XPATH,  '//tr[@class="ln rd"]'):
row = driver.find_element(By.XPATH,  '//tr[@class="ln rd"]')
row.click()
sleep(2)
tmp_tmp = driver.find_element(By.XPATH, '//b[@class ="bt" and @data-bt="-contbar_1;-content_1"]')
# tmp_tmp = driver.find_element(By.XPATH, '//b[@class ="bt" and @data-bt="mod:comments;flaw:185535283"]')

sleep(2)
print(tmp_tmp)
sleep(2)
ActionChains(driver).move_to_element(tmp_tmp).perform()
sleep(1)
tmp_tmp.click()
# sleep(10)







# driver.quit()
driver.close()

