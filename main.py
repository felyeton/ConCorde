from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

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

driver.get("https://www.melihov.tech/concorde/")
sleep(10)
# elem = driver.find_element(By.NAME, "name")
login = driver.find_element(By.XPATH,  '//input[@autocomplete="name"]')
login.send_keys("Мелихов")

password = driver.find_element(By.XPATH,  '//input[@autocomplete="password-current"]')
password.send_keys("Durak")
# elem.send_keys(Keys.ENTER)

go_button = driver.find_element(By.XPATH,  '//b[@class="bt lp"]')
go_button.click()
# class="bt lp"

sleep(10)


driver.find_element(By.XPATH,  '//b[@class="active"]').click()
sleep(1)

for row in driver.find_elements(By.XPATH,  '//tr[@class="ln rd"]'):
    row.click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//b[@class ="bt" and @title="Выйти из дефекта"]').click()
    sleep(0.3)







# driver.quit()
driver.close()

