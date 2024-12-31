import streamlit as st # type: ignore
import folium # type: ignore
from streamlit_folium import st_folium # type: ignore
from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time

chrome_options = Options() # type: ignore
chrome_options.add_argument("--headless") # type: ignore
chrome_options.add_argument("--no-sandbox") # type: ignore
chrome_options.add_argument("--disable-dev-shm-usage") # type: ignore

# Configurar el controlador de Selenium para Chrome
driver = webdriver.Chrome()

# URL de la página
url = "https://tempo.inmet.gov.br/AnaliseSituacaoAtual"

# Abrir la página
driver.get(url)

# Esperar a que la imagen específica se cargue (ajusta el selector según sea necesario)
try:
    # Esperar hasta que la imagen con el atributo 'alt' específico esté presente
    img_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='Carta da Análise Sinótica']"))
    )
    
    # Obtener la URL de la imagen
    img_url = img_element.get_attribute('src')
    print(f"Image URL: {img_url}")

except Exception as e:
    print("Error: ", e)
    img_url = None

finally:
    # Cerrar el navegador
    driver.quit()

st.set_page_config(layout="wide")
# st.sidebar.title("División de Mapa")
st.title("Comparación Cartas Sinópticas")

# Crear mapa base
m = folium.Map(location=[10, -80], zoom_start=3)

# Agregar las imágenes como capas
folium.raster_layers.ImageOverlay(
    name="18Z Image",
    image="https://www.nhc.noaa.gov/tafb/USA_18Z.gif",
    bounds=[[-36.50, -169.0], [59.00, 4.7]],
    opacity=0.6,
).add_to(m)

folium.raster_layers.ImageOverlay(
    name="00Z Image",
    image="https://www.nhc.noaa.gov/tafb/USA_00Z.gif",
    bounds=[[-36.50, -169.0], [59.00, 4.7]],
    opacity=0.6,
).add_to(m)

# Añadir la primera imagen GIF como capa de imagen si se obtuvo la URL
if img_url:
    folium.raster_layers.ImageOverlay(
        name='INMET',
        image=img_url,
        bounds=[[-60.00, -94.5], [31.70, -19.5]],
        opacity=0.6
    ).add_to(m)


# Añadir control de capas
folium.LayerControl().add_to(m)

# Mostrar el mapa en Streamlit
st_folium(m, height=700, width=1400)
