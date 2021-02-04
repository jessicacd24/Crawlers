from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def ir_Linkedin(name):
  driver = webdriver.Firefox(executable_path = '/home/jessica/Escritorio/crawlers/geckodriver')
  #Página a la que queremos acceder
  driver.get("https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
  input_email = driver.find_element_by_id("username")
  input_email.send_keys('personafinder.lasalle@gmail.com')

  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password")))
  input_password = driver.find_element_by_id("password")
  input_password.send_keys('lasalletfm')
  input_password.send_keys(Keys.ENTER)

  #message = driver.find_element_by_xpath('//*[@id="msg-overlay"]/div[1]/header').click()
  #//*[@id="msg-overlay"]/div[1]/header/section[1]

  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ember41"]/input')))
  #boton = driver.find_element_by_partial_link_text('Iniciar').click()
  #WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "search-global-typeahead__input always-show-placeholder")))
  #input_person = driver.find_element_by_css_selector("search-global-typeahead__input")
  input_person = driver.find_element_by_xpath('//*[@id="ember41"]/input')
  #input_person = driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input")
  #input_person = driver.find_elements_by_class_name(".search-global-typeahead__input")
  #/html/body/header/div/form/div/div/div/div/div[1]/div/input
  #//*[@id="ember41"]/input
  input_person.send_keys(name)
  input_person.send_keys(Keys.ENTER)

  #buscar = driver.find_element_by_name('Buscar')
  #buscar.click()
  #buscar = driver.find_element_by_css_selector('a._19bs')
  #buscar.click()

  #informacion de contacto //*[@id="ember637"]/span
  #ventana emergente //*[@id="ember903"]

def main():
  print (ir_Linkedin('Jessica Cañas'))
main()