"""
OBJETIVO: 
    - Extraer informacion sobre los productos en la pagina de Mercado Libre Mascotas
    - Aprender a realizar extracciones verticales y horizontales utilizando reglas
CREADO POR: LEONARDO KUFFO
ULTIMA VEZ EDITADO: 2 marzo 2021
"""
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

# Clase donde se colocará lo que queremos extraer de la web
class oportunidad_laboral(Item):
    empresa = Field()
  #  cargo = Field()
    salario = Field()
    descripcion = Field()
  #  tipo_contrato = Field()
    ubicacion = Field()
  #  duracion_contrato = Field()
   # fecha_publicacion = Field()

#parsearemos los nombres 

class occCrawler(CrawlSpider):
    name = 'occ'  #se nombra al scrawler
    
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 60 # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
    }

    # Utilizamos 2 dominios permitidos, ya que los articulos utilizan un dominio diferente
  #  allowed_domains = ['www.occ.com.mx/empleosc', 'www.occ.com.mx/empleo/oferta/']  # Solo ingresaran a los dominios que esten dentro del parametro

    start_urls = ['https://www.occ.com.mx/empleos/']

    download_delay = 1  #Tiempo que se demora por requerimiento.

    # Tupla de reglas
    rules = (
        Rule( # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(
                allow=r'/tipo-home-office-mixto?med=home-office&page=\d+&src=curated_search' # Patron en donde se utiliza "\d+", expresion que puede tomar el valor de cualquier combinacion de numeros
            ), follow=True),
        Rule( # REGLA #2 => VERTICALIDAD AL DETALLE DE LOS PRODUCTOS
            LinkExtractor(     #Obtener todos los url que tengan
                allow=r'/empleo/oferta/' 
            ), follow=True, callback='parse_items'), # Al entrar al detalle de los productos, se llama al callback con la respuesta al requerimiento (Nombre de la funcion que se va a definir)
        )
    

    def parse_items(self, response):  # Self: donde esta la clase, response: donde esta el árbol de la paginación

        item = ItemLoader(oportunidad_laboral(), response)
        
        # Utilizo Map Compose con funciones anonimas
        # PARA INVESTIGAR: Que son las funciones anonimas en Python?
      #  item.add_xpath('titulo', '//h1/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
      #  item.add_xpath('descripcion', '//div[@class="item-description__text"]/p/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        item.add_xpath ('empresa','//h1/text()')
       # item.add_xpath ('cargo' ) 
       # item.add_xpath ('salario','//[@id="salary"]/p/text()' ) 
        item.add_xpath ('descripcion','//[@id="jobbody"]/p/text()' )
       # item.add_xpath ('tipo_contrato' )
        item.add_xpath ('ubicacion','//a[@id="citylink"]' , '//[@id="statelink"]/a/text()' )
      # item.add_xpath ('duracion_contrato' )
       # item.add_xpath ('fecha_publicacion' )


      #  soup = BeautifulSoup(response.body)
      #  precio = soup.find(class_="price-tag ui-pdp-price__part")
     #   precio_completo = precio.text.replace('\n', ' ').replace('\r', ' ').replace(' ', '') # texto de todos los hijos
      #  item.add_value('precio', precio_completo)

        yield item.load_item()

# EJECUCION
# scrapy runspider 2_mercadolibre.py -o mercado_libre.json -t json