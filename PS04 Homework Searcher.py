from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Функция для поиска статьи на Википедии по запросу
def search_wikipedia(query):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"https://ru.wikipedia.org/wiki/{query}")
    return driver
    time.sleep(50)


# Функция для отображения параграфов текущей статьи
def list_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, para in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {para.text[:200]}...")  # Отображаем первые 200 символов
        if (i + 1) % 5 == 0:  # Пауза каждые 5 параграфов
            cont = input("Продолжить листать параграфы? (да/нет): ")
            if cont.lower() != 'да':
                break


# Функция для отображения связанных ссылок
def list_internal_links(driver):
    links = driver.find_elements(By.XPATH, "//div[@id='bodyContent']//a[@href and not(@class)]")
    internal_links = [(link.text, link.get_attribute('href')) for link in links if
                      link.get_attribute('href').startswith("https://ru.wikipedia.org/wiki/")]
    return internal_links


# Основная функция программы
def main():
    initial_query = input("Введите ваш первоначальный запрос: ")
    driver = search_wikipedia(initial_query)

    while True:
        action = input("Выберите действие: \n1. Листать параграфы\n2. Перейти на внутреннюю ссылку\n3. Выйти\n")

        if action == '1':
            list_paragraphs(driver)
        elif action == '2':
            internal_links = list_internal_links(driver)
            for i, (text, link) in enumerate(internal_links):
                print(f"{i + 1}. {text}: {link}")
            link_choice = int(input("Выберите номер ссылки для перехода: ")) - 1
            if 0 <= link_choice < len(internal_links):
                driver.get(internal_links[link_choice][1])
            else:
                print("Неверный выбор")
        elif action == '3':
            print("Выход из программы")
            driver.quit()
            break
        else:
            print("Неверное действие, пожалуйста, попробуйте снова")


if __name__ == "__main__":
    main()