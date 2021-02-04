from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def ir_facebook(name):
  driver = webdriver.Firefox(executable_path = '/home/jessica/Escritorio/crawlers/geckodriver')
  #Página a la que queremos acceder
  driver.get("https://www.facebook.com/")

  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
  input_email = driver.find_element_by_id("email")
  input_email.send_keys('personafinder.lasalle@gmail.com')

  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
  input_password = driver.find_element_by_id("pass")
  input_password.send_keys('lasalletfm')

  boton = driver.find_element_by_id("loginbutton")
  boton.click()

  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
  input_person = driver.find_element_by_name("q")
  input_person.send_keys(name)
  input_person.send_keys(Keys.ENTER)

  #buscar = driver.find_element_by_name('Buscar')
  #buscar.click()
  #buscar = driver.find_element_by_css_selector('a._19bs')
  #buscar.click()

 # //*[@id="js_2"]/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[1]

def main():
  print (ir_facebook('Jessica Cañas'))
main()