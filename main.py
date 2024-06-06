from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.youtube.com/")

driver.maximize_window()

def test_busca(input):
    time.sleep(1)
    search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'search_query')))
    search_input.send_keys(input)
    time.sleep(1)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.back()
    search_input.clear()

for input in ["abcABC123", "!@#$$%^&*()", "你Д가あ", "abcABC123!@#$$%^&*()", "abcABC123!@#$$%^&*()你Д가あ"]:
    test_busca(input)

def test_email():
    driver.get("https://www.youtube.com/")

    login_bt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')))
    login_bt.click()
    create_acc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button/span')))
    create_acc.click()

    personal_use = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[3]')))
    personal_use.click()

    first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName')))
    first_name.send_keys("dada")

    second_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'lastName')))
    second_name.send_keys("dasdas")

    submit_bt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collectNameNext"]/div/button/span')))
    submit_bt.click()

    day = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'day')))
    day.send_keys("5")

    time.sleep(1)
    year = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'year')))
    year.send_keys("2000")

    time.sleep(1)
    month = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'month')))
    select_month = Select(month)
    select_month.select_by_value('1')

    time.sleep(1)
    gender = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'gender')))
    select_gender = Select(gender)
    select_gender.select_by_value('1')

    submit_bt_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthdaygenderNext"]/div/button/span')))
    submit_bt_2.click()

    for email_adress in ['', 'mateus.f.2804@gmail.com', 'mateus']:
        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Username')))
        email.send_keys(email_adress)
        time.sleep(3)

        send_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="next"]/div/button/span')))
        send_email.click()
        time.sleep(2)
        email.clear()

test_email()


def test_img_size():
    driver.get("https://www.youtube.com/watch?v=VpeR2uGcAAM")

    time.sleep(1)
    body = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body')))
    body.send_keys('f')
    time.sleep(5)
    body.send_keys('t')
    time.sleep(5)
    body.send_keys('i')
    time.sleep(5)
    driver.back()
    body.send_keys('t')


test_img_size()











