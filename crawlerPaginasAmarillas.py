from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ir_paginas_amarillas_web(cadena, city):
  driver = webdriver.Firefox(executable_path = '/home/jessica/Escritorio/crawlers/geckodriver')
  #Página a la que queremos acceder
  driver.get("https://www.paginasamarillas.es/")
  lista_datos = []
  try:
    #Verificamos si el elemento con ID="whatInput" ya está cargado, este elemento es la caja de texto donde se hacen las busquedas
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "whatInput")))
    #Obtenemos la caja de texto de busquedas
    input_nombre = driver.find_element_by_id("whatInput")
    #Enviamos la cadena que estamos buscando
    input_nombre.send_keys(cadena)
    #Verificamos si el elemento con ID="whereInput" ya está cargado, este elemento es la caja de lugar donde se hacen las busquedas
    input2_nombre = driver.find_element_by_id("where")
    #Enviamos la ciudad que estamos buscando
    input2_nombre.send_keys(city)
    #Obtenemos el botón que ejecuta la búsqueda
    boton = driver.find_element_by_id("submitBtn")
    #Damos click al botón
    boton.click()
  except:
    #Mostramos este mensaje en caso de que se presente algún problema
    print ("El elemento no está presente")
  try:
    #Si se encuentran resultados la página los muestra en elementos de nombre "listado-item"
    #Para ello esperamos que estos elementos se carguen para proceder a consultarlos
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listado-item")))
  except:
    print ('Elementos no encontrados')
    #Obtenemos en una lista los elementos encontrados
  resultados = driver.find_elements_by_class_name("listado-item")
  telefono = driver.find_element_by_css_selector("div.llama-desplegable")
  telefono.click()
  for resultado in resultados:
    #En cada uno de los elementos encontrados buscamos un elemento interno que tiene por nombre box
    try:
      datos = resultado.find_element_by_class_name("box")
      print ('datos=', datos.text)
    except:
      datos='-'
      print('datos=0')
    print ("==============================\n")

  driver.close()
  return lista_datos

def main():
  print (ir_paginas_amarillas_web('Legalcity','Barcelona'))
main()
