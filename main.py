from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# modo per aprire il web driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# apri il browser ed indichi dove navigare
driver.get("https://www.amazon.it/")

time.sleep(4)

try:
    if driver.find_element(By.CSS_SELECTOR, "#sp-cc-accept") is not None:
        accetta_cookie = driver.find_element(By.CSS_SELECTOR, "#sp-cc-accept")
        accetta_cookie.click()
except:
    print('elemento non presente')

time.sleep(2)

tasto_offerte = driver.find_element(By.CSS_SELECTOR, "a[class = 'nav-a  '][href = '/deals?ref_=nav_cs_gb']")
tasto_offerte.click()

time.sleep(2)

select_ordina_per = driver.find_element(By.CSS_SELECTOR, "#sorting_dropdown0")
select_ordina_per.click()

time.sleep(2)

prezzo_decrescente = driver.find_element(By.CSS_SELECTOR, "#native_sorting_dropdown0_4")
prezzo_decrescente.click()

time.sleep(2)

lista_prodotti = driver.find_elements(By.CSS_SELECTOR, "div[class='DealGridItem"
                                                       "-module__dealItemDisplayGrid_e7RQVFWSOrwXBX4i24Tqg "
                                                       "DealGridItem-module__withBorders_2jNNLI6U1oDls7Ten3Dttl "
                                                       "DealGridItem"
                                                       "-module__withoutActionButton_2OI8DAanWNRCagYDL2iIqN']")
lista_prodotti[0].click()

time.sleep(2)

try:
    list_items = driver.find_elements(By.CSS_SELECTOR, ".a-list-item")


    if len(list_items) != 0:
        obj = {}

    i = 0
    for el in list_items:
        obj.update({'prezzo' + str(i): driver.fin})

except:
    print("lista non trovata")


driver.close()


