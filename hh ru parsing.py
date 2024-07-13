import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = 'https://ufa.hh.ru/vacancies/programmist'
driver.get(url)

wait = WebDriverWait(driver, 10)

parsed_data = []

while True:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')))
    vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')

    for vacancy in vacancies:
        try:
            title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
            company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text

            # Проверка наличия элемента с зарплатой
            try:
                salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--kTJ0_rp54B2vNeZ3CTt2').text
            except:
                salary = 'Не указана'

            link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
        except Exception as e:
            print(f'Произошла ошибка при парсинге: {e}')
            continue

        parsed_data.append([title, company, salary, link])

    # Попробуем найти кнопку "Следующая страница"
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-qa="pager-next"]')))
        driver.execute_script("arguments[0].click();", next_button)  # Используем execute_script для клика
        time.sleep(3)  # Ждем загрузки следующей страницы
    except Exception as e:
        print(f"Следующая страница не найдена, парсинг завершен. Ошибка: {e}")
        break

driver.quit()

with open('hh.csv', "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка'])
    writer.writerows(parsed_data)