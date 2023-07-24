from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("http://localhost/typing-test")

input_element = driver.find_element_by_css_selector(".word-input")

finished = False
while not finished:
    
    first_word_element = driver.find_element_by_css_selector("tbody tr:first-child td:first-child")
    first_word = first_word_element.get_attribute("innerText")
    letters = list(first_word)

    for letter in letters:
        input_element.send_keys(letter)
    input_element.send_keys(Keys.SPACE)

    try:
        result_element = driver.find_element_by_css_selector(".result p")
        finished = True
    except:
        pass