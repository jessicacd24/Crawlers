from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ir_paginas_blancas_web(name, lastname, city):
  driver = webdriver.Firefox(executable_path = '/home/jessica/Escritorio/crawlers/geckodriver')
  #Página a la que queremos acceder
  driver.get("http://blancas.paginasamarillas.es")
  lista_datos = []
  try:
    #Verificamos si el elemento con ID="whatInput" ya está cargado, este elemento es la caja de texto donde se hacen las busquedas
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "no")))
    #Obtenemos la caja de texto de busquedas
    #input_nombre = driver.find_element_by_xpath("//*[@id='particulares']/fieldset[1]/fieldset[1]/input")
    input_nombre = driver.find_element_by_name("no")
    #Enviamos la cadena que estamos buscando
    input_nombre.send_keys(name)
    #Verificamos si el elemento con ID="whereInput" ya está cargado, este elemento es la caja de lugar donde se hacen las busquedas
    input2_nombre = driver.find_element_by_name("ap1")
    #Enviamos el apellido que estamos buscando
    input2_nombre.send_keys(lastname)
    #Verificamos si el elemento con ID="whereInput" ya está cargado, este elemento es la caja de lugar donde se hacen las busquedas
    input_provincia = driver.find_element_by_name("sec")
    #Enviamos la provincia que estamos buscando
    input_provincia.send_keys(city)
    #Obtenemos el botón que ejecuta la búsqueda
    boton = driver.find_element_by_name("encontrar")
    #Damos click al botón
    boton.click()
  except:
    #Mostramos este mensaje en caso de que se presente algún problema
   print ("El elemento no está presente")
  #try:
    #Si se encuentran resultados la página los muestra en elementos de nombre "listado-item"
    #Para ello esperamos que estos elementos se carguen para proceder a consultarlos
   # WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listado-item")))
  #except:
  #  print ('Elementos no encontrados')
  #Obtenemos en una lista los elementos encontrados
  resultados = driver.find_elements_by_class_name("PPAL")
  #resultados = driver.find_elements_by_class_name("telef")
  #telefono = driver.find_element_by_class_name("telef")
  #print(resultados)
  #telefono.click()
  for resultado in resultados:
   #En cada uno de los elementos encontrados buscamos un elemento interno
   try:
     #datos = resultado.find_elements_by_xpath('//*[@id="PPAL"]/div')
     datos = resultado.find_elements_by_class_name("resul")
     print ('datos=', datos.text)
   except:
     datos='-'
     print('datos=0')
     print ("==============================\n")

  driver.close()
  return lista_datos

def main():
  print (ir_paginas_blancas_web('Jessica', 'Alonso', 'Barcelona'))
main()
