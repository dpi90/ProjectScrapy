import requests
from bs4 import BeautifulSoup

# Extraer las url de todo los trabajos publicados en la pagina principal de COMPUTRABAJO MEXICO
response = requests.get("https://www.computrabajo.com.mx/ofertas-de-trabajo/")
soup = BeautifulSoup(response.content)
lista_urls = []

b = soup.find_all(class_="js-o-link")
for i in b:
    print("https://www.computrabajo.com.mx/{0}".format(i.get("href")))


def obtener_url_por_pagina(numero_pagina):
    response = requests.get("https://www.computrabajo.com.mx/ofertas-de-trabajo/?p={0}".format(numero_pagina))
    soup = BeautifulSoup(response.content)
    lista_links = []
    links = soup.find_all(class_="js-o-link")
    for link in links:
        lista_links.append("https://www.computrabajo.com.mx/{0}".format(link.get("href")))
    return lista_links


pagina = 0
lista_urls = []

while True:
    lista_urls = lista_urls + obtener_url_por_pagina(pagina)
    if len(lista_urls) <= 0:
        break
    pagina = pagina + 1
    if pagina > 10:
        break

archivo = open("lista_url_mx.txt", "w")
for link in lista_urls:
    archivo.write(link + "\n")
archivo.close()
lista_urls[1:3]
obtener_url_por_pagina(2)
# Extraer los datos de las paginas de las publicaciones
# responseUnica = requests.get("https://www.computrabajo.com.pe//ofertas-de-trabajo/oferta-de-trabajo-de-sales-specialist-en-san-isidro-C6666C58CBCEAABB61373E686DCF3405")
# responseUnica = requests.get("https://www.computrabajo.com.pe//ofertas-de-trabajo/oferta-de-trabajo-de-analista-de-admision-de-riesgos-sede-quillabamba-en-santa-ana-51F2738B25C177FA61373E686DCF3405")
# responseUnica = requests.get("https://www.computrabajo.com.pe//ofertas-de-trabajo/oferta-de-trabajo-de-colaborador-multifuncional-full-time-av-colonial-en-surco-098EA1300320A2EE61373E686DCF3405")
responseUnica = requests.get("https://www.computrabajo.com.mx//ofertas-de-trabajo/oferta-de-trabajo-de-cajero-medio-tiempo-ciudad-guzman-en-zapotlan-el-grande-394524634B324BFE61373E686DCF3405")
soupPagina = BeautifulSoup(responseUnica.content)






# WebScrapy - Computrabajo
### Tomas las url principal
### Obtiene los datos de las url
### escribe en un archivo final
import re
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Extraer las url de todo los trabajos publicados en la pagina principal de COMPUTRABAJO MEXICO
response = requests.get('https://www.computrabajo.com.mx/ofertas-de-trabajo/')
soup = BeautifulSoup(response.content)
lista_urls = []

b = soup.find_all(class_="js-o-link")
for i in b:
    print("https://www.computrabajo.com.mx/{0}".format(i.get("href")))


def obtener_url_por_pagina(numero_pagina):
    response = requests.get("https://www.computrabajo.com.mx/ofertas-de-trabajo/?p={0}".format(numero_pagina))
    soup = BeautifulSoup(response.content)
    lista_links = []
    links = soup.find_all(class_="js-o-link")
    for link in links:
        lista_links.append("https://www.computrabajo.com.mx/{0}".format(link.get("href")))
    return lista_links


pagina = 0
lista_urls = []

while True:
    lista_urls = lista_urls + obtener_url_por_pagina(pagina)
    if len(lista_urls) <= 0:
        break
    pagina = pagina + 1
    if pagina > 10:
        break

archivo = open("lista_url_mx.txt", "w")
for link in lista_urls:
    archivo.write(link + "\n")
archivo.close()
lista_urls[1:3]
obtener_url_por_pagina(2)

responseUnica = requests.get ('https://www.computrabajo.com.mx//ofertas-de-trabajo/oferta-de-trabajo-de-cajero-medio-tiempo-ciudad-guzman-en-zapotlan-el-grande-394524634B324BFE61373E686DCF3405')
soupPagina = BeautifulSoup(responseUnica.content)



def obtener_url_por_pagina(numero_pagina):
    # response = requests.get("https://www.computrabajo.com.pe/ofertas-de-trabajo/?p={0}".format(numero_pagina))
    response = requests.get('https://www.computrabajo.com.mx/empleos-jornada-por-horas?p={0}'.format(numero_pagina))
    soup = BeautifulSoup(response.content)
    lista_links = []
    links = soup.find_all(class_="js-o-link")
    for link in links:
        lista_links.append("https://www.computrabajo.com.mx/{0}".format(link.get("href")))
    return lista_links


def obtener_datos(link):
    responseUnica = requests.get(link)
    soupPagina = BeautifulSoup(responseUnica.content)
    # revisar
    try:
        nombre_empresa = soupPagina.find(class_="tooltip_sello_icon w_100i").find('a').get_text().strip()
    except:
        nombre_empresa = ""
    nombre_empleo = soupPagina.title.string.strip()
    # descripcion_empleo=soupPagina.find(class_="cm-12 box_i bWord").get_text().strip()
    try:
        # lugar=soupPagina.find("header").find_all("span")[0].text.strip()
        lugar = soupPagina.find("header").find(class_="w_70 fl mb10 w100_r mb0_r").text.strip()
    except:
        lugar = ""
    try:
        ultima_actualizacion = soupPagina.find("header").find(class_="w_70 fl mb10 w100_r mb0_r").text.strip()
    except:
        ultima_actualizacion = ""
    try:
        fecha = soupPagina.find("header").find(class_="w_70 fl mb10 w100_r mb0_r").text.strip()
    except:
        fecha = ""
    # resumen_empleo =soupPagina.find(class_="box box_r").find('ul').text

    #  try:
    #    nombre_empleo=soupPagina.find(class_="box box_r").find_all("li")[0].text.strip()
    #  except:
    #    nombre_empleo =""
    #  try:
    #    nombre_empresa=soupPagina.find(class_="box box_r").find_all("li")[1].p.text.strip()
    #  except:
    #    nombre_empresa=""
    #  try:
    #    localizacion = soupPagina.find(class_="box box_r").find_all("li")[2].p.text.strip()
    #  except:
    #    localizacion=""
    #  try:
    #    jornada = soupPagina.find(class_="box box_r").find_all("li")[3].p.text.strip()
    #  except:
    #    jornada=""
    #  try:
    #    tipo_contrato = soupPagina.find(class_="box box_r").find_all("li")[4].p.text.strip()
    #  except:
    #    tipo_contrato =""
    #  try:
    #    salario = soupPagina.find(class_="box box_r").find_all("li")[5].p.text.strip()
    #  except:
    #    salario=""

    salario = ""
    tipo_contrato = ""
    jornada = ""
    localizacion = ""
    nombre_empresa = ""

    for registro in soupPagina.find(class_="box box_r").find_all("li"):
        try:
            salario = registro.find('h3', string=re.compile("Salario")).parent.text.strip().replace("\t", " ").replace(
                "\r", " ").replace("\n", " ")
        except:
            pass
        try:
            tipo_contrato = registro.find('h3', string=re.compile("Tipo\sde\scontrato")).parent.text.strip().replace(
                "\t", " ").replace("\r", " ").replace("\n", " ")
        except:
            pass
        try:
            jornada = registro.find('h3', string=re.compile("Jornada")).parent.text.strip().replace("\t", " ").replace(
                "\r", " ").replace("\n", " ")
        except:
            pass
        try:
            localizacion = registro.find('h3', string=re.compile("Localización")).parent.text.strip().replace("\t",
                                                                                                              " ").replace(
                "\r", " ").replace("\n", " ")
        except:
            pass
        try:
            nombre_empresa = registro.find('h3', string=re.compile("Empresa")).parent.text.strip().replace("\t",
                                                                                                           " ").replace(
                "\r", " ").replace("\n", " ")
        except:
            pass

    salario = "".join([i if i != "" else "" for i in salario.split("  ")])
    tipo_contrato = "".join([i if i != "" else "" for i in tipo_contrato.split("  ")])
    jornada = "".join([i if i != "" else "" for i in jornada.split("  ")])
    nombre_empresa = "".join([i if i != "" else "" for i in nombre_empresa.split("  ")])
    localizacion = "".join([i if i != "" else "" for i in localizacion.split("  ")])

    try:
        descripcion_empleo = soupPagina.find(class_="cm-12 box_i bWord").find_all('li')[1].get_text().strip().replace(
            "^", " ")
    except:
        descripcion_empleo = ""
    try:
        requisito_educacion = soupPagina.find(class_="cm-12 box_i bWord").find('li', string=re.compile(
            'Educación')).text.strip()
    except:
        requisito_educacion = ""
    try:
        requisito_disponibilidad_viajar = soupPagina.find(class_="cm-12 box_i bWord").find('li', string=re.compile(
            'Disponibilidad\sde\sviajar')).text.strip()
    except:
        requisito_disponibilidad_viajar = ""
    try:
        requisito_disponibilidad_cambio_residencia = soupPagina.find(class_="cm-12 box_i bWord").find('li',
                                                                                                      string=re.compile(
                                                                                                          'Disponibilidad\sde\scambio\sde\sresidencia')).text.strip()
    except:
        requisito_disponibilidad_cambio_residencia = ""
    try:
        requisito_edad = soupPagina.find(class_="cm-12 box_i bWord").find('li', string=re.compile('Edad')).text.strip()
    except:
        requisito_edad = ""
    try:
        requisito_idiomas = soupPagina.find(class_="cm-12 box_i bWord").find('li',
                                                                             string=re.compile('Idiomas')).text.strip()
    except:
        requisito_idiomas = ""
    try:
        requisitos_anios_experiencia = soupPagina.find(class_="cm-12 box_i bWord").find('li', string=re.compile(
            'Años\sde\sexperiencia')).text.strip()
    except:
        requisitos_anios_experiencia = ""
    try:
        cantidad_vacantes = soupPagina.find(class_="cm-12 box_i bWord").find('li', string=re.compile(
            'Cantidad\sde\svacantes')).text.strip()
    except:
        cantidad_vacantes = ""
    try:
        fecha_contratacion = soupPagina.find(class_="cm-12 box_i bWord").find('li', string=re.compile(
            'Fecha\sde\scontratación')).text.strip()
    except:
        fecha_contratacion = ""
    cadena = "{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}{0}{7}{0}{8}{0}{9}{0}{10}{0}{11}{0}{12}{0}{13}{0}{14}{0}{15}{0}{16}{0}{17}{0}{18}{0}{19}"
    cadena = cadena.format("^", nombre_empresa, nombre_empleo, lugar, fecha, localizacion, jornada, tipo_contrato,
                           salario, cantidad_vacantes
                           , fecha_contratacion, descripcion_empleo, requisito_educacion,
                           requisito_disponibilidad_viajar, requisito_disponibilidad_cambio_residencia
                           , requisito_edad, requisito_idiomas, requisitos_anios_experiencia, link,
                           ultima_actualizacion)
    return cadena


"""
 Proceso principal:
 Obtiene lista de urls a recorrer y obtener los datos de los empleos.
"""
pagina = 0
lista_urls = []

print("[INFO]> Inicio de Proceso {0}".format(datetime.now().strftime("%Y%m%d %H:%M:%S")))
while True:
    lista_urls = lista_urls + obtener_url_por_pagina(pagina)
    if len(lista_urls) <= 0:
        break
    pagina = pagina + 1
    # Test con 15 paginas
    if pagina > 150:
        break

"""
  Obtener los datos de las urls obtenidos
"""
lista_registros = []
print("[INFO]> Obteniendo datos de las {0} urls ".format(len(lista_urls)))
for index, url in enumerate(lista_urls):
    lista_registros.append(obtener_datos(url))
    # if index>100:
    # break

"""
  Escribir el archivo en base a los datos obtenidos
"""
archivo = open("empleos.txt", "w")
for index, registro in enumerate(lista_registros):
    if index == 0:
        cadena = "{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}{0}{7}{0}{8}{0}{9}{0}{10}{0}{11}{0}{12}{0}{13}{0}{14}{0}{15}{0}{16}{0}{17}{0}{18}{0}{19}"
        cadena = cadena.format("^", "nombre_empresa", "nombre_empleo", "lugar", "fecha", "localizacion", "jornada",
                               "tipo_contrato", "salario", "cantidad_vacantes"
                               , "fecha_contratacion", "descripcion_empleo", "requisito_educacion",
                               "requisito_disponibilidad_viajar", "requisito_disponibilidad_cambio_residencia"
                               , "requisito_edad", "requisito_idiomas", "requisitos_anios_experiencia", "link",
                               "ultima_actualizacion")
        archivo.write(cadena + "\n")
    archivo.write(registro + "\n")
archivo.close()
print("[INFO]> Fin de Proceso {0}".format(datetime.now().strftime("%Y%m%d %H:%M:%S")))

import re

# soupPagina.find(class_="box box_r").find_all("li")#[2].p.text.strip()
# soupPagina.find(class_="box box_r").find_all("li")[5].find('p',string=re.compile('Localizaci'))
# soupPagina.find(class_="box box_r").find_all("li")[1].find('h3').parent#.find('h3',string=re.compile("mpresa"))
soupPagina.find(class_="box box_r").find_all("li")[1].find('h3', string=re.compile("Empresa")).parent

soupPagina.find(class_="box box_r").find_all("li")[2].find('h3', string=re.compile("Localización")).parent

soupPagina.find(class_="box box_r").find_all("li")[3].find('h3', string=re.compile("Jornada")).parent

soupPagina.find(class_="box box_r").find_all("li")[4].find('h3', string=re.compile("Tipo\sde\scontrato")).parent

soupPagina.find(class_="box box_r").find_all("li")[5].find('h3', string=re.compile("Salario")).parent

salario = ""
tipo_contrato = ""
jornada = ""
localizacion = ""
empresa = ""

for registro in soupPagina.find(class_="box box_r").find_all("li"):
    try:
        salario = registro.find('h3', string=re.compile("Salario")).parent.text.strip().replace("\t", " ").replace("\r",
                                                                                                                   " ").replace(
            "\n", " ")
    except:
        pass
    try:
        tipo_contrato = registro.find('h3', string=re.compile("Tipo\sde\scontrato")).parent.text.strip().replace("\t",
                                                                                                                 " ").replace(
            "\r", " ").replace("\n", " ")
    except:
        pass
    try:
        jornada = registro.find('h3', string=re.compile("Jornada")).parent.text.strip().replace("\t", " ").replace("\r",
                                                                                                                   " ").replace(
            "\n", " ")
    except:
        pass
    try:
        localizacion = registro.find('h3', string=re.compile("Localización")).parent.text.strip().replace("\t",
                                                                                                          " ").replace(
            "\r", " ").replace("\n", " ")
    except:
        pass
    try:
        empresa = registro.find('h3', string=re.compile("Empresa")).parent.text.strip().replace("\t", " ").replace("\r",
                                                                                                                   " ").replace(
            "\n", " ")
    except:
        pass

print("".join([i if i != "" else "" for i in salario.split("  ")]))
print("".join([i if i != "" else "" for i in tipo_contrato.split("  ")]))
print("".join([i if i != "" else "" for i in jornada.split("  ")]))
print("".join([i if i != "" else "" for i in empresa.split("  ")]))
print("".join([i if i != "" else "" for i in localizacion.split("  ")]))

# [i if i!="" else "" for i in salario.split("  ")]
# "".join([i if i!="" else "" for i in tipo_contrato.split("  ")])

print(soupPagina.find("header").prettify())

soupPagina.find("header").find(class_="fc80 fs14 fl w_100").text.strip()

for m in soupPagina.find("header").find_all("span"):
    print(m.prettify())

localizacion = soupPagina.find("header").p.find_all('span')[0].text.strip()

ultima_actualizacion = soupPagina.find("header").p.find_all('span')[1].text.strip()
ultima_actualizacion
