import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://www.saucedemo.com/"

# добавить опции
options = webdriver.ChromeOptions()

# оставить браузер открытым
options.add_experimental_option("detach", True)

# открытие браузера в headless режиме
# options.add_argument("--headless")

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере
driver_chrome.get(base_url)

# команда для открытия окна в максимальном для монитора разрешении
driver_chrome.maximize_window()

# найти на странице элемент под id "user-name"
user_name = driver_chrome.find_element(By.ID, "user-name")

# пауза 2 секунды
time.sleep(2)

# установить в поле значение "standard_user"
user_name.send_keys("standard_user")
print("Ввод логина.")

# найти на странице элемент под id "password"
password = driver_chrome.find_element(By.ID, "password")

# пауза 2 секунды
time.sleep(2)

# установить в поле некорректный пароль
password.send_keys("incorrect_password")
print("Ввод некорректного пароля.")

# пауза 2 секунды
time.sleep(2)

# найти на странице элемент под id "login-button"
login_button = driver_chrome.find_element(By.ID, "login-button")
# нажать на кнопку
login_button.click()
print("Нажатие на кнопку Login.")

# пауза 2 секунды
time.sleep(2)

# найти на странице всплывающее уведомление с текстом об ошибке
warning_text = driver_chrome.find_element(
    By.XPATH,
    "//h3[@data-test='error']"
)
# сохранить текст об ошибке в переменную
value_warning_text = warning_text.text

# проверка наличия уведомления с текстом об ошибке
assert value_warning_text == ("Epic sadface: Username and password do not"
                              " match any user in this service"), \
    "Ошибка: Уведомление об ошибке отсутствует!"
print("Сообщение об ошибке присутствует, корректно.")

# найти на странице кнопку для закрытия уведомления об ошибке
error_button = driver_chrome.find_element(
    By.XPATH,
    "//button[@class='error-button']"
)
# нажать на кнопку закрытия уведомления
error_button.click()
print("Уведомление закрыто.")

# пауза 2 секунды
time.sleep(2)

# закрыть окно браузера
driver_chrome.close()
