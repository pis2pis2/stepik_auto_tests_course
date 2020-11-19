from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
# browser = webdriver.Chrome()
# browser.get(link)
a=os.getcwd()
print(a)
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input[placeholder="Enter first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[placeholder="Enter last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[placeholder="Enter email"]')
    input3.send_keys("ivanpetrov@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = ("C:/file.txt")
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input4 = browser.find_element_by_css_selector('input[type="file"]')
    input4.send_keys(file_path)



    # print(os.path.abspath(os.path.dirname(__file__)))
    # print(os.path.dirname(__file__))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манип

