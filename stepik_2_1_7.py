from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select






try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_1 = browser.find_element_by_id('num1').text
    x_2 = browser.find_element_by_id('num2').text

    y = int(x_1) + int(x_2)
    z = str(y)
    print(type(z),z)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)  # ищем элемент с текстом "Python"




    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    # browser.quit()