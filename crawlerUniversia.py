from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def ir_paginas_amarillas_web(cadena):
  driver = webdriver.Firefox(executable_path = '/home/jessica/Escritorio/crawlers/geckodriver')
  #Página a la que queremos acceder
  driver.get("https://guiaempresas.universia.es")
  lista_datos = []
  try:
    #Obtenemos la caja de texto de busquedas
    input_nombre = driver.find_element_by_id("search")
    #Enviamos la cadena que estamos buscando
    input_nombre.send_keys(cadena)
    input_nombre.send_keys(Keys.ENTER)

  except:
    #Mostramos este mensaje en caso de que se presente algún problema
    print ("El elemento no está presente")
  try:
    #Si se encuentran resultados la página los muestra en elementos de nombre "textleft"
    #Para ello esperamos que estos elementos se carguen para proceder a consultarlos
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "textleft")))
  except:
    print ('Elementos no encontrados')
    #Obtenemos en una lista los elementos encontrados
  #resultados = driver.find_elements_by_class_name("textleft")
  resultados = driver.find_element_by_partial_link_text(cadena).click()
  #link = driver.find_element_by_tag_name('a')
  #link.click()

  for resultado in resultados:
    #En cada uno de los elementos encontrados buscamos un elemento interno que tiene por nombre box
    try:
      datos = resultado.find_element_by_class_name("td_ficha_univ")
      print ('datos=', datos.text)
    except:
      datos='-'
      print('datos=0')
    print ("==============================\n")

  driver.close()
  return lista_datos

def main():
  print (ir_paginas_amarillas_web('Legalcity'))
main()
